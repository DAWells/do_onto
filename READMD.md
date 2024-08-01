# DO ontology
Visualise mortality rates and improvements in them for different
cancers showing clustering of cancer types.

Using disease ontology generate graph embeddings to view clustering of
cancer types. Additional information on the cancer type can also be
viewed in this way.

## Set up neo4j with docker 
Pull the official neo4j docker image.
`docker pull neo4j`

Spin up a container using that image, setting the ports
and log-in details. See the neo4j [docs](https://neo4j.com/docs/operations-manual/current/docker/introduction/)
for more info.

docker run \
    -it --rm \
    --publish=7474:7474 --publish=7687:7687 \
    --env NEO4J_AUTH=neo4j/123456789 \
    --env NEO4J_PLUGINS='["graph-data-science","apoc","n10s"]' \
    neo4j:5.17.0


Will not install plug ins on windows in docker. Solution may be related to
    --env=NEO4J_dbms_security_procedures_unrestricted="gds.*,apoc.\\\*" ^


## Set up python environment
Create a virtual environment
`python3 -m venv .venv`

Activate that environment with `. .venv/bin/activate` or `.venv\bin\Activate.bat`
if you're on linux or windows.

Install the needed packages with `pip install -r requirements.txt`.

- neo4j
- pandas
- umap

## Import ontology
Import the "Disease Ontology" ontology with uniqueness constraints
and simple name config.

## Encode nodes
Generate graph embeddings and louvain clusters for cancer types.

## Plot
View embedding structure in 2D using t-SNE coloured by louvain cluster.

# cancer rates
https://doi.org/10.3322/caac.21660

https://doi.org/10.3322/caac.21834

