import os
import torch
import requests
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    pipeline,
)
from peft import LoraConfig

# fastAPI setup
app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# dataset model
class UserPrompt(BaseModel):
    prompt: str

# fine tuned model
model_name = "pabloRiva/llama-2-finetune-tramites"

# Bits and Bytes setup
use_4bit = True
bnb_4bit_compute_dtype = "float16"
bnb_4bit_quant_type = "nf4"

# checks cpu availability
device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using device:", device)

# loads model using bits and bytes
compute_dtype = getattr(torch, bnb_4bit_compute_dtype)

bnb_config = BitsAndBytesConfig(
    load_in_4bit=use_4bit,
    bnb_4bit_quant_type=bnb_4bit_quant_type,
    bnb_4bit_compute_dtype=compute_dtype,
)

# loads model and tokenizer
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=bnb_config,
    device_map={"": 0}
)

# tokenizer setup
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"

# runs pipeline
pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer, max_length=200, truncation=True)  # Agrega truncation=True

# function to handle knowledge graph
def is_knowledge_graph_query(prompt):
    # keywords for knowledge graph
    knowledge_keywords = {
        "urlSitioWeb": ["url", "sitio web", "dónde", "donde"],
        "sigla": ["sigla", "siglas"],
        "objetivo": ["objetivo"] 
    }
    
    # check keywords in promt
    for key, keywords in knowledge_keywords.items():
        if any(keyword in prompt.lower() for keyword in keywords):
            return key
            
    return None


def generate_finetuned_prompt(prompt):
    if "pasos" in prompt:
        question_type = "¿Qué pasos debo seguir para realizar el trámite"
    elif "duración" in prompt or "duracion" in prompt:
        question_type = "¿Qué duración tiene el trámite"
    elif "costo" in prompt:
        question_type = "¿Qué costo tiene el trámite"
    elif "objetivo" in prompt and "tramite" in prompt:
        question_type = "¿Cuál es el objetivo del trámite"
    else:
        question_type = "Pregunta no reconocida"

    if "trámite" in prompt or "tramite" in prompt:
        entity = prompt.split("trámite", 1)[1].strip() if "trámite" in prompt else prompt.split("tramite", 1)[1].strip()
    else:
        entity = "especificado"

    return f"<s>[INST] {question_type} {entity}? [/INST]"

# sparql queries generator
def generate_dynamic_sparql_query(prompt, entity_type):
    entity = ""

    if entity_type == "urlSitioWeb":
        entity = prompt.replace("¿Cuál es la URL del sitio web de la organización ", "").replace("?", "").strip()
    
    elif entity_type == "sigla":
        entity = prompt.replace("¿Cuál es la sigla de la organización ", "").replace("?", "").strip()
    
    elif entity_type == "objetivo":
        entity = prompt.replace("¿Cuál es el objetivo de la organización ", "").replace("?", "").strip()

    
    if entity_type == "urlSitioWeb":
        sparql_query = f"""
        PREFIX ontology: <http://example.org/ontology#>
        SELECT ?urlSitioWeb
        WHERE {{
          ?organization ontology:denominacion "{entity}" .
          ?organization ontology:urlSitioWeb ?urlSitioWeb .
        }}
        """
    elif entity_type == "sigla":
        sparql_query = f"""
        PREFIX ontology: <http://example.org/ontology#>
        SELECT ?sigla
        WHERE {{
          ?organization ontology:denominacion "{entity}" .
          ?organization ontology:sigla ?sigla .
        }}
        """
    elif entity_type == "objetivo":
        sparql_query = f"""
        PREFIX ontology: <http://example.org/ontology#>
        SELECT ?objetivo
        WHERE {{
          ?organization ontology:denominacion "{entity}" .
          ?organization ontology:objetivoEntidad ?objetivo .
        }}
        """
    else:
        # No se debería llegar aquí si se valida correctamente antes
        print("Tipo de entidad no permitido.")
        return None

    print("SPARQL Query generada:", sparql_query)
    return sparql_query




# Función para ejecutar la consulta SPARQL en GraphDB
def execute_sparql(query):
    endpoint = "http://CrispinPompin:7200/repositories/KnowldegeGraph"
    headers = {
        "Content-Type": "application/sparql-query",
        "Accept": "application/json"
    }
    response = requests.post(endpoint, data=query, headers=headers)
    if response.status_code == 200:
        results = response.json().get('results', {}).get('bindings', [])
        print("Resultados de SPARQL:", results)  # Imprime los resultados
        return results
    else:
        print("Error en consulta SPARQL:", response.status_code, response.text)  # Imprime error
        return {"error": "Error ejecutando la consulta SPARQL"}


@app.post("/ask")
def ask(user_prompt: UserPrompt):
    prompt = user_prompt.prompt

    # Detecta si es una consulta para el KG y define el tipo de entidad
    entity_type = is_knowledge_graph_query(prompt)

    if entity_type:
        print("Consulta detectada para el Knowledge Graph")
        sparql_query = generate_dynamic_sparql_query(prompt, entity_type)
        kg_response = execute_sparql(sparql_query)

        # Formatea la respuesta para que sea más legible en la UI
        if kg_response and isinstance(kg_response, list):
            if entity_type == "urlSitioWeb":
                formatted_response = "Resultados encontrados:\n" + "\n".join(
                    [f"URL: {result.get('urlSitioWeb', {}).get('value', 'N/A')}" for result in kg_response]
                )
            elif entity_type == "sigla":
                formatted_response = "Resultados encontrados:\n" + "\n".join(
                    [f"Sigla: {result.get('sigla', {}).get('value', 'N/A')}" for result in kg_response]
                )
            elif entity_type == "mae":
                formatted_response = "Resultados encontrados:\n" + "\n".join(
                    [f"Autoridad Máxima Ejecutiva: {result.get('autoridad', {}).get('value', 'N/A')}" for result in kg_response]
                )
            elif entity_type == "objetivo":
                formatted_response = "Resultados encontrados:\n" + "\n".join(
                    [f"Objetivo: {result.get('objetivo', {}).get('value', 'N/A')}" for result in kg_response]
                )
        else:
            formatted_response = "No se encontraron resultados."

        response = formatted_response  # Aquí asignas la respuesta formateada
    else:
        print("Consulta detectada para el modelo Fine-Tuneado")
        finetuned_prompt = generate_finetuned_prompt(prompt)
        result = pipe(finetuned_prompt)
        response = result[0]['generated_text']
        print("Prompt formateado para el modelo:", finetuned_prompt)

    return JSONResponse(content={"response": response})

# Ejecuta el servidor si el script se ejecuta directamente
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5002)
