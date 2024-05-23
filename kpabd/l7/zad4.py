from neo4j import GraphDatabase
from secret import URI, USERNAME, PASSWORD

query = "MATCH (p:Person) RETURN p.name AS Name"

with GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD)) as driver:
    with driver.session() as session:
        query_result = [record.data() for record in session.run(query)]

for person in query_result:
    print(person)
