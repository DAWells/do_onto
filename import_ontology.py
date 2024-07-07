"""
Use neo4j python driver to import the `disease ontology`
ontology.
"""
from neo4j import GraphDatabase
from neo4j import exceptions

URI = "bolt://localhost:7687"
AUTH = ("neo4j", "123456789")

# with GraphDatabase.driver(URI, auth=AUTH) as driver:
#     driver.verify_connectivity()

def config_init(tx):
    results = tx.run(
        'CALL n10s.graphconfig.init({ handleVocabUris: "IGNORE" });',
        database="neo4j"
    )
    return list(results)

def set_constraint(tx):
    results = tx.run(
        "CREATE CONSTRAINT n10s_unique_uri FOR (r:Resource)"
        "REQUIRE r.uri IS UNIQUE;"
    )
    return results

def fetch_ontology(tx):
    ontology = tx.run(
        "CALL n10s.onto.import.fetch($url,$format);",
        url="http://purl.obolibrary.org/obo/doid.owl",
        format="RDF/XML"
    )
    return list(ontology)

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()
    with driver.session(database="neo4j") as session:
        config_results = session.execute_write(
            config_init
        )
        try:
            constraint_results = session.execute_write(
                set_constraint
            )
        except exceptions.ClientError:
            print("Could not set constraints, do they already exist?")
        ontology_results = session.execute_write(
            fetch_ontology
        )


# CREATE CONSTRAINT n10s_unique_uri ON (r:Resource)
# ASSERT r.uri IS UNIQUE;

## CALL n10s.rdf.preview.fetch("http://purl.obolibrary.org/obo/doid.owl","RDF/XML");
# CALL n10s.onto.preview.fetch("http://purl.obolibrary.org/obo/doid.owl","RDF/XML");

