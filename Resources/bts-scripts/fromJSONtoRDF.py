from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import RDF, RDFS, XSD
import json

def json_to_rdf(json_file, output_file):
    try:
        # Read JSON file
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Create RDF graph
        g = Graph()
        
        # Define namespaces
        ns = Namespace("http://example.org/")
        g.bind("ex", ns)

        # Process each item in the list
        for item in data:  # Changed from data.items() to data
            # Create a URI for each organization
            org_uri = URIRef(ns[f"organization_{item.get('organization_id', '')}"])
            
            # Add triples for each field
            for key, value in item.items():
                if value:  # Only add if value is not empty
                    predicate = URIRef(ns[key])
                    g.add((org_uri, predicate, Literal(value)))

        # Save the RDF graph
        g.serialize(destination=output_file, format='turtle')
        print(f"Successfully created RDF file: {output_file}")

    except FileNotFoundError:
        print(f"Error: Input file '{json_file}' not found")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    json_to_rdf('organization_db-2.json', 'new_datos.ttl')