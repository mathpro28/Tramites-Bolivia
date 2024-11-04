import os
import torch
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

# Configuración de la aplicación FastAPI
app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de datos
class UserPrompt(BaseModel):
    prompt: str

# Reemplaza 'pabloRiva/llama-2-finetune-tramites' con el nombre de tu modelo fine-tuneado
model_name = "pabloRiva/llama-2-finetune-tramites"

# Configuración de Bits and Bytes
use_4bit = True
bnb_4bit_compute_dtype = "float16"
bnb_4bit_quant_type = "nf4"

# Verifica si hay GPU disponible
device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using device:", device)

# Carga el modelo base con Bits and Bytes
compute_dtype = getattr(torch, bnb_4bit_compute_dtype)

bnb_config = BitsAndBytesConfig(
    load_in_4bit=use_4bit,
    bnb_4bit_quant_type=bnb_4bit_quant_type,
    bnb_4bit_compute_dtype=compute_dtype,
)

# Carga el modelo y el tokenizador
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    # quantization_config=bnb_config,
    device_map={"": 0}
)

# Configuración del tokenizador
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"

# Ejecuta un pipeline para generación de texto
pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer, max_length=200, truncation=True)  # Agrega truncation=True

def is_knowledge_graph_query(prompt):
    keywords = [
        "url", "sitio web", "dónde", "donde",
        "organización", "entidad", "procedimiento", "denominación", 
        "sigla", "mae"
    ]
    return any(keyword in prompt.lower() for keyword in keywords) and "trámite" not in prompt.lower()

def generate_finetuned_prompt(prompt):
    if "pasos" in prompt:
        question_type = "¿Qué pasos debo seguir para realizar el trámite"
    elif "duración" in prompt or "duracion" in prompt:
        question_type = "¿Qué duración tiene el trámite"
    elif "costo" in prompt:
        question_type = "¿Qué costo tiene el trámite"
    elif "objetivo" in prompt:
        question_type = "¿Cuál es el objetivo del trámite"
    else:
        question_type = "Pregunta no reconocida"

    if "trámite" in prompt or "tramite" in prompt:
        entity = prompt.split("trámite", 1)[1].strip() if "trámite" in prompt else prompt.split("tramite", 1)[1].strip()
    else:
        entity = "especificado"

    return f"<s>[INST] {question_type} {entity}? [/INST]"

def generate_sparql_query(entity):
    sparql_query = f"""
    PREFIX ontology: <http://example.org/ontology#>
    SELECT ?urlSitioWeb
    WHERE {{
      ?organization ontology:denominacion "{entity}" .
      ?organization ontology:urlSitioWeb ?urlSitioWeb .
    }}
    """
    print("SPARQL Query generada:", sparql_query)
    return "URL del sitio web simulada para el knowledge graph."

@app.post("/ask")
def ask(user_prompt: UserPrompt):
    prompt = user_prompt.prompt
    finetuned_prompt = ""

    if is_knowledge_graph_query(prompt):
        entity = prompt.split()[-1]
        print("Consulta detectada para el Knowledge Graph")
        response = generate_sparql_query(entity)
    else:
        print("Consulta detectada para el modelo Fine-Tuneado")
        finetuned_prompt = generate_finetuned_prompt(prompt)
        # Llama al pipeline del modelo
        result = pipe(finetuned_prompt)  # Genera la respuesta usando el modelo
        response = result[0]['generated_text']  # Captura la respuesta generada
        print("Prompt formateado para el modelo:", finetuned_prompt)

    return JSONResponse(content={"response": response})  # Retorna la respuesta generada


# Ejecuta el servidor si el script se ejecuta directamente
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)