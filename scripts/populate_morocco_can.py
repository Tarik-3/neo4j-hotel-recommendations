"""
Populate Neo4j database with Africa Cup of Nations (CAN) 2025 Morocco data
This script creates countries, stadiums, hotels, and their relationships.
"""

from app.database import get_session
import random

def clear_database():
    """Clear all nodes and relationships from the database"""
    with get_session() as session:
        session.run("MATCH (n) DETACH DELETE n")
    print("✓ Database cleared")

def create_countries():
    """Create participating countries"""
    countries = [
        "Nigeria",
        "Morocco", 
        "Senegal",
        "Egypt",
        "Cameroon",
        "Algeria",
        "Tunisia",
        "Ivory Coast"
    ]
    
    with get_session() as session:
        for country in countries:
            session.run(
                "CREATE (:Country {name: $name})",
                name=country
            )
    print(f"✓ Created {len(countries)} countries")
    return countries

def create_stadiums():
    """Create stadiums in Morocco"""
    stadiums = [
        {"name": "Mohammed V Stadium", "city": "Casablanca", "capacity": 45891},
        {"name": "Prince Moulay Abdellah Stadium", "city": "Rabat", "capacity": 52000},
        {"name": "Grand Stade de Marrakech", "city": "Marrakech", "capacity": 45240},
        {"name": "Ibn Battuta Stadium", "city": "Tangier", "capacity": 45000},
        {"name": "Adrar Stadium", "city": "Agadir", "capacity": 45480}
    ]
    
    with get_session() as session:
        for stadium in stadiums:
            session.run(
                """
                CREATE (:Stadium {
                    name: $name, 
                    city: $city, 
                    capacity: $capacity
                })
                """,
                name=stadium["name"],
                city=stadium["city"],
                capacity=stadium["capacity"]
            )
    print(f"✓ Created {len(stadiums)} stadiums in Morocco")
    return stadiums

def create_hotels():
    """Create hotels in Moroccan cities"""
    hotels = [
        # Casablanca Hotels
        {"name": "Hotel Atlas", "city": "Casablanca", "price": 120, "rating": 3.8, "capacity": 200},
        {"name": "Hyatt Regency Casablanca", "city": "Casablanca", "price": 150, "rating": 4.5, "capacity": 300},
        {"name": "Ibis Casa Voyageurs", "city": "Casablanca", "price": 80, "rating": 3.6, "capacity": 150},
        {"name": "Kenzi Tower Hotel", "city": "Casablanca", "price": 135, "rating": 4.2, "capacity": 250},
        
        # Rabat Hotels
        {"name": "Sofitel Rabat Jardin des Roses", "city": "Rabat", "price": 200, "rating": 4.7, "capacity": 250},
        {"name": "Hotel Le Diwan Rabat", "city": "Rabat", "price": 130, "rating": 4.0, "capacity": 180},
        {"name": "Riad Dar Rabat", "city": "Rabat", "price": 90, "rating": 3.9, "capacity": 100},
        {"name": "Movenpick Hotel Mansour Eddahbi", "city": "Rabat", "price": 165, "rating": 4.4, "capacity": 220},
        
        # Marrakech Hotels
        {"name": "Kenzi Menara Palace", "city": "Marrakech", "price": 160, "rating": 4.3, "capacity": 220},
        {"name": "La Mamounia", "city": "Marrakech", "price": 300, "rating": 4.9, "capacity": 150},
        {"name": "Riad Marrakech Medina", "city": "Marrakech", "price": 70, "rating": 3.7, "capacity": 80},
        {"name": "Palais Namaskar", "city": "Marrakech", "price": 280, "rating": 4.8, "capacity": 120},
        {"name": "Hotel Les Jardins de la Koutoubia", "city": "Marrakech", "price": 145, "rating": 4.1, "capacity": 200},
        
        # Tangier Hotels
        {"name": "Hilton Garden Inn Tangier City Center", "city": "Tangier", "price": 140, "rating": 4.2, "capacity": 200},
        {"name": "Hotel El Minzah", "city": "Tangier", "price": 120, "rating": 4.0, "capacity": 150},
        {"name": "Ibis Tangier", "city": "Tangier", "price": 85, "rating": 3.5, "capacity": 100},
        {"name": "Farah Tanger Hotel", "city": "Tangier", "price": 110, "rating": 3.8, "capacity": 180},
        {"name": "Hotel Tanger With Spa", "city": "Tangier", "price": 160, "rating": 4.3, "capacity": 200},
        {"name": "Riad Tangier Medina", "city": "Tangier", "price": 95, "rating": 3.9, "capacity": 120},
        
        # Agadir Hotels
        {"name": "Royal Atlas Hotel", "city": "Agadir", "price": 150, "rating": 4.3, "capacity": 250},
        {"name": "Sofitel Agadir Thalassa Sea & Spa", "city": "Agadir", "price": 220, "rating": 4.7, "capacity": 200},
        {"name": "Ibis Agadir", "city": "Agadir", "price": 75, "rating": 3.6, "capacity": 120},
        {"name": "Atlantic Palace Resort", "city": "Agadir", "price": 180, "rating": 4.4, "capacity": 300},
        {"name": "Club Med Agadir", "city": "Agadir", "price": 250, "rating": 4.6, "capacity": 400},
        {"name": "Oasis Agadir Hotel", "city": "Agadir", "price": 130, "rating": 4.1, "capacity": 180},
        
        # Additional Casablanca Hotels
        {"name": "Sheraton Casablanca", "city": "Casablanca", "price": 170, "rating": 4.6, "capacity": 350},
        {"name": "Royal Mansour Casablanca", "city": "Casablanca", "price": 210, "rating": 4.8, "capacity": 200},
        
        # Additional Marrakech Hotels
        {"name": "Bahia Palace Riad", "city": "Marrakech", "price": 110, "rating": 4.0, "capacity": 100},
    ]
    
    with get_session() as session:
        for hotel in hotels:
            session.run(
                """
                CREATE (:Hotel {
                    name: $name,
                    city: $city,
                    price: $price,
                    rating: $rating,
                    capacity: $capacity
                })
                """,
                name=hotel["name"],
                city=hotel["city"],
                price=hotel["price"],
                rating=hotel["rating"],
                capacity=hotel["capacity"]
            )
    print(f"✓ Created {len(hotels)} hotels across Morocco")
    return hotels

def create_country_stadium_relationships(countries, stadiums):
    """Create PLAYS_AT relationships between countries and stadiums"""
    # Map countries to stadiums (each country plays at specific stadiums)
    assignments = [
        ("Nigeria", "Mohammed V Stadium"),
        ("Nigeria", "Prince Moulay Abdellah Stadium"),
        ("Morocco", "Mohammed V Stadium"),
        ("Morocco", "Grand Stade de Marrakech"),
        ("Senegal", "Ibn Battuta Stadium"),
        ("Senegal", "Mohammed V Stadium"),
        ("Egypt", "Prince Moulay Abdellah Stadium"),
        ("Egypt", "Grand Stade de Marrakech"),
        ("Cameroon", "Adrar Stadium"),
        ("Cameroon", "Ibn Battuta Stadium"),
        ("Algeria", "Mohammed V Stadium"),
        ("Algeria", "Adrar Stadium"),
        ("Tunisia", "Grand Stade de Marrakech"),
        ("Tunisia", "Prince Moulay Abdellah Stadium"),
        ("Ivory Coast", "Ibn Battuta Stadium"),
        ("Ivory Coast", "Adrar Stadium"),
    ]
    
    with get_session() as session:
        for country_name, stadium_name in assignments:
            session.run(
                """
                MATCH (c:Country {name: $country}), (s:Stadium {name: $stadium})
                MERGE (c)-[:PLAYS_AT]->(s)
                """,
                country=country_name,
                stadium=stadium_name
            )
    print(f"✓ Created {len(assignments)} PLAYS_AT relationships")
    return len(assignments)

def create_stadium_hotel_relationships():
    """Create HAS_NEARBY_HOTEL relationships with distance and travel time"""
    # Connect stadiums to hotels in the same city
    with get_session() as session:
        # Get all stadiums
        result = session.run("MATCH (s:Stadium) RETURN s.name AS name, s.city AS city")
        stadiums = [{"name": record["name"], "city": record["city"]} for record in result]
        
        relationship_count = 0
        for stadium in stadiums:
            # Get hotels in the same city
            hotels_result = session.run(
                "MATCH (h:Hotel {city: $city}) RETURN h.name AS name",
                city=stadium["city"]
            )
            hotels = [record["name"] for record in hotels_result]
            
            # Create relationships with realistic distances
            for hotel in hotels:
                # Random distance between 0.5 and 8 km
                distance = round(random.uniform(0.5, 8.0), 1)
                # Calculate travel time (assuming 30 km/h average speed in city)
                travel_time = round((distance / 30) * 60, 0)  # Convert to minutes
                # Add some variation
                travel_time = max(5, travel_time + random.randint(-3, 5))
                
                session.run(
                    """
                    MATCH (s:Stadium {name: $stadium}), (h:Hotel {name: $hotel})
                    MERGE (s)-[:HAS_NEARBY_HOTEL {
                        distance_km: $distance,
                        travel_time_min: $travel_time
                    }]->(h)
                    """,
                    stadium=stadium["name"],
                    hotel=hotel,
                    distance=distance,
                    travel_time=travel_time
                )
                relationship_count += 1
        
        print(f"✓ Created {relationship_count} HAS_NEARBY_HOTEL relationships")
        return relationship_count

def display_statistics():
    """Display database statistics"""
    with get_session() as session:
        # Count nodes
        countries = session.run("MATCH (c:Country) RETURN count(c) AS count").single()["count"]
        stadiums = session.run("MATCH (s:Stadium) RETURN count(s) AS count").single()["count"]
        hotels = session.run("MATCH (h:Hotel) RETURN count(h) AS count").single()["count"]
        
        # Count relationships
        plays_at = session.run("MATCH ()-[r:PLAYS_AT]->() RETURN count(r) AS count").single()["count"]
        nearby_hotels = session.run("MATCH ()-[r:HAS_NEARBY_HOTEL]->() RETURN count(r) AS count").single()["count"]
        
        print("\n" + "="*50)
        print("DATABASE STATISTICS")
        print("="*50)
        print(f"\nNodes:")
        print(f"  Countries: {countries}")
        print(f"  Stadiums: {stadiums}")
        print(f"  Hotels: {hotels}")
        print(f"\nRelationships:")
        print(f"  PLAYS_AT: {plays_at}")
        print(f"  HAS_NEARBY_HOTEL: {nearby_hotels}")
        print(f"\nTotal nodes: {countries + stadiums + hotels}")
        print(f"Total relationships: {plays_at + nearby_hotels}")
        print("="*50)

def test_query():
    """Test a sample query"""
    print("\n" + "="*50)
    print("SAMPLE QUERY: Best Hotels for Nigeria")
    print("="*50)
    
    with get_session() as session:
        result = session.run(
            """
            MATCH (c:Country {name: "Nigeria"})-[:PLAYS_AT]->(s:Stadium)
                  -[r:HAS_NEARBY_HOTEL]->(h:Hotel)
            WITH h, r, s,
                 (h.price * 0.4 + r.distance_km * 0.4 - h.rating * 0.2) AS score
            RETURN h.name AS hotel,
                   h.price AS price,
                   h.rating AS rating,
                   r.distance_km AS distance,
                   s.name AS stadium,
                   s.city AS city,
                   score
            ORDER BY score ASC
            LIMIT 5
            """
        )
        
        print("\nTop 5 recommended hotels for Nigeria fans:\n")
        for i, record in enumerate(result, 1):
            print(f"{i}. {record['hotel']}")
            print(f"   Stadium: {record['stadium']} ({record['city']})")
            print(f"   Price: ${record['price']}/night")
            print(f"   Rating: {record['rating']}/5.0")
            print(f"   Distance: {record['distance']} km")
            print(f"   Score: {record['score']:.2f}")
            print()

def main():
    """Main function to populate the database"""
    print("\n" + "="*50)
    print("POPULATING NEO4J DATABASE")
    print("Africa Cup of Nations 2025 - Morocco")
    print("="*50 + "\n")
    
    try:
        # Step 1: Clear existing data
        clear_database()
        
        # Step 2: Create nodes
        countries = create_countries()
        stadiums = create_stadiums()
        hotels = create_hotels()
        
        # Step 3: Create relationships
        create_country_stadium_relationships(countries, stadiums)
        create_stadium_hotel_relationships()
        
        # Step 4: Display statistics
        display_statistics()
        
        # Step 5: Run a test query
        test_query()
        
        print("\n✅ Database populated successfully!")
        print("🌐 You can now start the API server and use the frontend.")
        print("🚀 Run: uvicorn app.main:app --port 8000\n")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Make sure Neo4j is running and .env file has correct credentials.")
        raise

if __name__ == "__main__":
    main()
