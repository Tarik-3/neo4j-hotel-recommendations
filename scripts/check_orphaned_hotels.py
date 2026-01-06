"""Check for hotels not connected to any stadiums"""

from app.database import get_session

with get_session() as session:
    # Check for hotels NOT connected to any stadium
    result = session.run("""
        MATCH (h:Hotel)
        WHERE NOT (h)<-[:HAS_NEARBY_HOTEL]-()
        RETURN h.name AS name, h.city AS city
        ORDER BY h.city, h.name
    """)
    
    orphaned = list(result)
    
    if orphaned:
        print(f"\n❌ Found {len(orphaned)} orphaned hotels (not connected to stadiums):\n")
        for hotel in orphaned:
            print(f"  - {hotel['name']} ({hotel['city']})")
    else:
        print("\n✅ All hotels are connected to stadiums!")
    
    # Show summary by city
    print("\n📊 Hotels per city:")
    result = session.run("""
        MATCH (h:Hotel)
        RETURN h.city AS city, count(h) AS count
        ORDER BY h.city
    """)
    
    for row in result:
        print(f"  {row['city']}: {row['count']} hotels")
    
    # Show summary of relationships
    print("\n🔗 Stadium-Hotel relationships:")
    result = session.run("""
        MATCH (s:Stadium)-[r:HAS_NEARBY_HOTEL]->(h:Hotel)
        RETURN s.city AS city, count(r) AS relationships
        ORDER BY s.city
    """)
    
    for row in result:
        print(f"  {row['city']}: {row['relationships']} relationships")
