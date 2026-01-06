from app.database import get_session

def get_best_hotels(country: str, max_price: float = None, limit: int = 5):
    query = """
    MATCH (c:Country {name:$country})-[:PLAYS_AT]->(s:Stadium)
          -[r:HAS_NEARBY_HOTEL]->(h:Hotel)
    WHERE ($max_price IS NULL OR h.price <= $max_price)
    WITH h, r, s,
         (h.price * 0.4 + r.distance_km * 0.4 - h.rating * 0.2) AS score
    RETURN h.name AS name,
           s.name AS stadium_name,
           h.city AS city,
           h.price AS price,
           h.rating AS rating,
           r.distance_km AS distance_km,
           score
    ORDER BY score ASC
    LIMIT $limit
    """

    with get_session() as session:
        result = session.run(
            query,
            country=country,
            max_price=max_price,
            limit=limit
        )
        return [record.data() for record in result]
