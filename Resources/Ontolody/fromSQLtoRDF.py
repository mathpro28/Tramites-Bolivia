from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, RDFS, XSD

# Create the graph
g = Graph()

# Define namespaces
ex = Namespace("http://example.org/ontology#")

# Add namespace prefixes
g.bind("ex", ex)
g.bind("rdfs", RDFS)
g.bind("xsd", XSD)

# List of organizations with details
organizations = [
    {"id": "1", "denominacion": "Ministerio de Educación de Bolivia", "sigla": "MINEDU", "objetivo": "Diseñar, implementar y ejecutar políticas educativas inclusivas y equitativas.", "url": "http://www.minedu.gob.bo"},
    {"id": "2", "denominacion": "Servicio Nacional de Propiedad Intelectual", "sigla": "SENAPI", "objetivo": "Administrar y proteger la propiedad intelectual de manera eficaz.", "url": "http://www.senapi.gob.bo"},
    {"id": "3", "denominacion": "Ministerio de Salud", "sigla": "MINSA", "objetivo": "Garantizar el acceso a salud pública para todos.", "url": "http://www.minsa.gob.bo"},
    {"id": "4", "denominacion": "Ministerio de Obras Públicas", "sigla": "MOP", "objetivo": "Mejorar la infraestructura vial en Bolivia.", "url": "http://www.mop.gob.bo"},
    {"id": "5", "denominacion": "Ministerio de Justicia", "sigla": "MINJUS", "objetivo": "Promover el acceso a la justicia.", "url": "http://www.minjus.gob.bo"},
    {"id": "6", "denominacion": "Ministerio de Trabajo", "sigla": "MITRABAJO", "objetivo": "Regular las políticas laborales en Bolivia.", "url": "http://www.mitrabajo.gob.bo"},
    {"id": "7", "denominacion": "Ministerio de Desarrollo Rural", "sigla": "MDRYT", "objetivo": "Impulsar el desarrollo rural y agropecuario.", "url": "http://www.mdryt.gob.bo"},
    {"id": "8", "denominacion": "Ministerio de Defensa", "sigla": "MINDEF", "objetivo": "Proteger la soberanía nacional.", "url": "http://www.mindef.gob.bo"},
    {"id": "9", "denominacion": "Ministerio de Medio Ambiente", "sigla": "MMAyA", "objetivo": "Conservar el medio ambiente y los recursos naturales.", "url": "http://www.mmaya.gob.bo"},
    {"id": "10", "denominacion": "Ministerio de Economía", "sigla": "MINECO", "objetivo": "Administrar las finanzas públicas del país.", "url": "http://www.mineco.gob.bo"},
    {"id": "11", "denominacion": "Gobierno Autónomo Municipal de La Paz", "sigla": "GAMLP", "objetivo": "Gestionar los recursos y servicios públicos en La Paz.", "url": "http://www.lapaz.bo"},
    {"id": "12", "denominacion": "Gobierno Autónomo Departamental de Santa Cruz", "sigla": "GADSC", "objetivo": "Impulsar el desarrollo regional en Santa Cruz.", "url": "http://www.santacruz.gob.bo"},
    {"id": "13", "denominacion": "Ministerio de Planificación del Desarrollo", "sigla": "MPD", "objetivo": "Planificar el desarrollo económico del país.", "url": "http://www.mpd.gob.bo"},
    {"id": "14", "denominacion": "Autoridad de Regulación y Fiscalización de Telecomunicaciones", "sigla": "ATT", "objetivo": "Regular las telecomunicaciones en Bolivia.", "url": "http://www.att.gob.bo"},
    {"id": "15", "denominacion": "Autoridad de Fiscalización de Empresas", "sigla": "AEMP", "objetivo": "Regular y fiscalizar las empresas públicas y privadas.", "url": "http://www.aemp.gob.bo"},
    {"id": "16", "denominacion": "Ministerio de Hidrocarburos", "sigla": "MH", "objetivo": "Gestionar los recursos hidrocarburíferos del país.", "url": "http://www.hidrocarburos.gob.bo"},
    {"id": "17", "denominacion": "Ministerio de Energía", "sigla": "MENERGIA", "objetivo": "Administrar el sistema energético nacional.", "url": "http://www.energia.gob.bo"},
    {"id": "18", "denominacion": "Ministerio de Culturas", "sigla": "MCULTURAS", "objetivo": "Promover la diversidad cultural del país.", "url": "http://www.culturas.gob.bo"},
    {"id": "19", "denominacion": "Ministerio de Deportes", "sigla": "MDEPORTES", "objetivo": "Fomentar la práctica deportiva en Bolivia.", "url": "http://www.mdeportes.gob.bo"},
    {"id": "20", "denominacion": "Autoridad de Supervisión del Sistema Financiero", "sigla": "ASFI", "objetivo": "Supervisar el sistema financiero del país.", "url": "http://www.asfi.gob.bo"}
]

# Add organizations to the graph
for org in organizations:
    org_uri = URIRef(f"http://example.org/ontology#Organization{org['id']}")
    g.add((org_uri, RDF.type, ex.Organization))
    g.add((org_uri, ex.denominacion, Literal(org["denominacion"], datatype=XSD.string)))
    g.add((org_uri, ex.sigla, Literal(org["sigla"], datatype=XSD.string)))
    g.add((org_uri, ex.objetivoEntidad, Literal(org["objetivo"], datatype=XSD.string)))
    g.add((org_uri, ex.urlSitioWeb, Literal(org["url"], datatype=XSD.anyURI)))

# Print out the RDF graph in turtle format
print(g.serialize(format="turtle").decode("utf-8"))
