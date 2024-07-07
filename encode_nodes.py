
MATCH (cancer:Class {label:"cancer"})<-[:SCO|SCO_RESTRICTION *1..]-(n:Class)
WITH n
MATCH (n)-[:SCO|SCO_RESTRICTION]->(m:Class)
WITH gds.graph.project(
    "proj",
    n,
    m,
    {},
    {undirectedRelationshipTypes: ['*']}
) AS g
RETURN g.graphName AS graph, g.nodeCount AS nodes, g.relationshipCount AS rels


CALL gds.fastRP.stream('proj',
  {
    embeddingDimension: 128,
    randomSeed: 42
  }
)
YIELD nodeId, embedding

CALL gds.fastRP.write('proj',
  {
    embeddingDimension: 128,
    randomSeed: 42,
    writeProperty: 'embedding'
  }
)
YIELD nodePropertiesWritten

CALL gds.louvain.write(
  "proj",
  {
    writeProperty: "louvain"
  }
)
YIELD communityCount

MATCH (cancer:Class {label:"cancer"})<-[:SCO|SCO_RESTRICTION *0..]-(n)
RETURN DISTINCT
  n.label as label,
  n.embedding as embedding,
  n.louvain as louvain
