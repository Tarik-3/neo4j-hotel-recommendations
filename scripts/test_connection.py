from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

print(f"Testing connection to: {NEO4J_URI}")
print(f"User: {NEO4J_USER}")
print(f"Password: {'*' * len(NEO4J_PASSWORD)}")

try:
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    with driver.session() as session:
        result = session.run("RETURN 'Connection successful!' as message")
        record = result.single()
        print(f"\n✓ {record['message']}")
        
        # Check existing data
        result = session.run("MATCH (n) RETURN count(n) as count")
        count = result.single()["count"]
        print(f"✓ Found {count} nodes in database")
        
    driver.close()
except Exception as e:
    print(f"\n✗ Connection failed: {e}")
    print("\nPlease ensure:")
    print("1. Neo4j is running (check with: neo4j status)")
    print("2. Credentials in .env file are correct")
    print("3. Neo4j is listening on port 7687")
