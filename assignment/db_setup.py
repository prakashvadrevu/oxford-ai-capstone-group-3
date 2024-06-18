from langchain.chains import GraphCypherQAChain
from langchain_community.graphs import Neo4jGraph
from langchain_openai import ChatOpenAI
import os

graph = Neo4jGraph(
  url=os.environ["NEO4J_URI"],
  username=os.environ["NEO4J_USERNAME"],
  password=os.environ["NEO4J_PASSWORD"]
)

def drop_nodes(graph):
  cypher_query = "MATCH (n) DETACH DELETE n"
  graph.query(cypher_query)
  print("Deleted all the existing records")


def load_data(graph):
  # Load Kellys Dataset
  graph.query(
  """
    LOAD CSV WITH HEADERS FROM 'https://docs.google.com/spreadsheets/d/1gxEEnp0NklCS7ywsU-IgM5LAY2X74aVoDH0R4-PdNyI/export?format=csv' AS row
    WITH row,
      apoc.date.parse(row.`Date of Sale`, 'ms', 'MM/dd/yyyy') AS parsedDate
    MERGE (c:Country {name: row.Country})
    MERGE (s:Store {id: toInteger(row.`Store ID`)})
    ON CREATE SET s.country = row.Country
    MERGE (pc:ProductCategory {name: row.`Product Category`})
    MERGE (p:Product {id: toInteger(row.`Product ID`)})
    ON CREATE SET p.category = row.`Product Category`
    MERGE (sale:Sale {id: toInteger(row.ID), unitsSold: toInteger(row.`Units Sold`), date: date(datetime({epochMillis: parsedDate})), price: toFloat(row.`Price Sold`), gdpGrowth: toFloat(row.`GDP Growth Rate`), inflation: toFloat(row.`Inflation Rate`)})
    MERGE (s)-[:LOCATED_IN]->(c)
    MERGE (s)-[:SOLD]->(sale)
    MERGE (sale)-[:OF_PRODUCT]->(p)
    MERGE (p)-[:BELONGS_TO]->(pc)
  """
  )
  print("Loaded Kellys dataset to Neo4J")

drop_nodes(graph)
load_data(graph)

print("created schema:")
print(graph.schema)