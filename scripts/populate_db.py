from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

def clear_database():
    """Clear all nodes and relationships"""
    with driver.session() as session:
        session.run("MATCH (n) DETACH DELETE n")
        print("Database cleared")

def populate_database():
    """Populate database with sample CAN data"""
    with driver.session() as session:
        # Create countries
        countries = [
            "Egypt", "Morocco", "Algeria", "Senegal", 
            "Cameroon", "Nigeria", "Tunisia", "Ivory Coast"
        ]
        
        for country in countries:
            session.run("CREATE (:Country {name: $name})", name=country)
        print(f"Created {len(countries)} countries")
        
        # Create stadiums with locations
        stadiums = [
            {"name": "Cairo International Stadium", "city": "Cairo", "capacity": 75000},
            {"name": "Stade Mohammed V", "city": "Casablanca", "capacity": 45000},
            {"name": "Stade du 5 Juillet", "city": "Algiers", "capacity": 64000},
            {"name": "Stade Abdoulaye Wade", "city": "Diamniadio", "capacity": 50000},
        ]
        
        for stadium in stadiums:
            session.run(
                "CREATE (:Stadium {name: $name, city: $city, capacity: $capacity})",
                **stadium
            )
        print(f"Created {len(stadiums)} stadiums")
        
        # Assign countries to stadiums (where they will play)
        matches = [
            ("Egypt", "Cairo International Stadium"),
            ("Algeria", "Cairo International Stadium"),
            ("Morocco", "Stade Mohammed V"),
            ("Tunisia", "Stade Mohammed V"),
            ("Senegal", "Stade Abdoulaye Wade"),
            ("Cameroon", "Stade Abdoulaye Wade"),
            ("Nigeria", "Stade du 5 Juillet"),
            ("Ivory Coast", "Stade du 5 Juillet"),
        ]
        
        for country, stadium in matches:
            session.run(
                """
                MATCH (c:Country {name: $country})
                MATCH (s:Stadium {name: $stadium})
                CREATE (c)-[:PLAYS_AT]->(s)
                """,
                country=country,
                stadium=stadium
            )
        print(f"Created {len(matches)} PLAYS_AT relationships")
        
        # Create hotels near each stadium
        hotels_data = [
            # Near Cairo International Stadium
            {"name": "Cairo Marriott Hotel", "price": 150.0, "rating": 4.5, "stadium": "Cairo International Stadium", "distance": 5.2},
            {"name": "Ramses Hilton", "price": 120.0, "rating": 4.2, "stadium": "Cairo International Stadium", "distance": 6.8},
            {"name": "Le Meridien Cairo", "price": 180.0, "rating": 4.7, "stadium": "Cairo International Stadium", "distance": 3.5},
            {"name": "Budget Inn Cairo", "price": 50.0, "rating": 3.5, "stadium": "Cairo International Stadium", "distance": 8.0},
            
            # Near Stade Mohammed V
            {"name": "Hyatt Regency Casablanca", "price": 160.0, "rating": 4.6, "stadium": "Stade Mohammed V", "distance": 4.5},
            {"name": "Kenzi Tower Hotel", "price": 140.0, "rating": 4.3, "stadium": "Stade Mohammed V", "distance": 5.0},
            {"name": "Ibis Casa Voyageurs", "price": 70.0, "rating": 3.8, "stadium": "Stade Mohammed V", "distance": 6.5},
            
            # Near Stade du 5 Juillet
            {"name": "Sheraton Algiers", "price": 170.0, "rating": 4.4, "stadium": "Stade du 5 Juillet", "distance": 4.0},
            {"name": "Sofitel Algiers", "price": 200.0, "rating": 4.8, "stadium": "Stade du 5 Juillet", "distance": 3.0},
            {"name": "Hotel Aurassi", "price": 90.0, "rating": 3.9, "stadium": "Stade du 5 Juillet", "distance": 7.0},
            
            # Near Stade Abdoulaye Wade
            {"name": "Radisson Blu Dakar", "price": 155.0, "rating": 4.5, "stadium": "Stade Abdoulaye Wade", "distance": 8.0},
            {"name": "King Fahd Palace", "price": 250.0, "rating": 4.9, "stadium": "Stade Abdoulaye Wade", "distance": 9.0},
            {"name": "Dakar Budget Hotel", "price": 60.0, "rating": 3.6, "stadium": "Stade Abdoulaye Wade", "distance": 12.0},
        ]
        
        for hotel in hotels_data:
            # Create hotel
            session.run(
                "CREATE (:Hotel {name: $name, price: $price, rating: $rating})",
                name=hotel["name"],
                price=hotel["price"],
                rating=hotel["rating"]
            )
            
            # Create relationship with stadium
            session.run(
                """
                MATCH (s:Stadium {name: $stadium})
                MATCH (h:Hotel {name: $hotel_name})
                CREATE (s)-[:HAS_NEARBY_HOTEL {distance_km: $distance}]->(h)
                """,
                stadium=hotel["stadium"],
                hotel_name=hotel["name"],
                distance=hotel["distance"]
            )
        
        print(f"Created {len(hotels_data)} hotels with relationships")

def verify_data():
    """Verify the data was created correctly"""
    with driver.session() as session:
        # Count nodes
        result = session.run("MATCH (n) RETURN labels(n) as label, count(n) as count")
        print("\nNode counts:")
        for record in result:
            print(f"  {record['label'][0]}: {record['count']}")
        
        # Count relationships
        result = session.run("MATCH ()-[r]->() RETURN type(r) as type, count(r) as count")
        print("\nRelationship counts:")
        for record in result:
            print(f"  {record['type']}: {record['count']}")

if __name__ == "__main__":
    print("Starting database population...")
    clear_database()
    populate_database()
    verify_data()
    driver.close()
    print("\nDatabase populated successfully!")
