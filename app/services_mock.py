"""
Mock service for testing without Neo4j database
Use this to test the API endpoints when database is not available
"""

# Mock data for testing
MOCK_DATA = {
    "Egypt": [
        {"name": "Le Meridien Cairo", "price": 180.0, "rating": 4.7, "distance_km": 3.5, "score": 73.46},
        {"name": "Cairo Marriott Hotel", "price": 150.0, "rating": 4.5, "distance_km": 5.2, "score": 61.18},
        {"name": "Ramses Hilton", "price": 120.0, "rating": 4.2, "distance_km": 6.8, "score": 50.88},
        {"name": "Budget Inn Cairo", "price": 50.0, "rating": 3.5, "distance_km": 8.0, "score": 23.2},
    ],
    "Morocco": [
        {"name": "Hyatt Regency Casablanca", "price": 160.0, "rating": 4.6, "distance_km": 4.5, "score": 66.88},
        {"name": "Kenzi Tower Hotel", "price": 140.0, "rating": 4.3, "distance_km": 5.0, "score": 58.14},
        {"name": "Ibis Casa Voyageurs", "price": 70.0, "rating": 3.8, "distance_km": 6.5, "score": 30.84},
    ],
    "Algeria": [
        {"name": "Sofitel Algiers", "price": 200.0, "rating": 4.8, "distance_km": 3.0, "score": 81.24},
        {"name": "Sheraton Algiers", "price": 170.0, "rating": 4.4, "distance_km": 4.0, "score": 69.72},
        {"name": "Hotel Aurassi", "price": 90.0, "rating": 3.9, "distance_km": 7.0, "score": 39.02},
    ],
    "Senegal": [
        {"name": "Radisson Blu Dakar", "price": 155.0, "rating": 4.5, "distance_km": 8.0, "score": 65.2},
        {"name": "King Fahd Palace", "price": 250.0, "rating": 4.9, "distance_km": 9.0, "score": 103.82},
        {"name": "Dakar Budget Hotel", "price": 60.0, "rating": 3.6, "distance_km": 12.0, "score": 29.28},
    ]
}

def get_best_hotels_mock(country: str, max_price: float = None, limit: int = 5):
    """
    Mock version of get_best_hotels that returns sample data
    Use this when Neo4j database is not available
    """
    hotels = MOCK_DATA.get(country, [])
    
    # Filter by max price if specified
    if max_price:
        hotels = [h for h in hotels if h["price"] <= max_price]
    
    # Sort by score and limit results
    hotels = sorted(hotels, key=lambda x: x["score"])[:limit]
    
    return hotels
