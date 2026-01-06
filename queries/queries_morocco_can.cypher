// ================================================================
// Neo4j Cypher Queries for CAN 2025 Morocco
// Copy and paste these queries into Neo4j Browser (http://localhost:7474)
// ================================================================

// ---------------------------------
// 1. VIEW ALL DATA
// ---------------------------------

// View all nodes and relationships
MATCH (n)
RETURN n
LIMIT 100;

// ---------------------------------
// 2. COUNT STATISTICS
// ---------------------------------

// Count all node types
MATCH (c:Country) WITH count(c) AS countries
MATCH (s:Stadium) WITH countries, count(s) AS stadiums
MATCH (h:Hotel) WITH countries, stadiums, count(h) AS hotels
RETURN countries, stadiums, hotels;

// ---------------------------------
// 3. COUNTRY QUERIES
// ---------------------------------

// List all countries
MATCH (c:Country)
RETURN c.name AS country
ORDER BY c.name;

// Show where each country plays
MATCH (c:Country)-[:PLAYS_AT]->(s:Stadium)
RETURN c.name AS country, 
       collect(s.name) AS stadiums
ORDER BY c.name;

// ---------------------------------
// 4. STADIUM QUERIES
// ---------------------------------

// List all stadiums with details
MATCH (s:Stadium)
RETURN s.name AS stadium, 
       s.city AS city, 
       s.capacity AS capacity
ORDER BY s.capacity DESC;

// Show which countries play at each stadium
MATCH (c:Country)-[:PLAYS_AT]->(s:Stadium)
RETURN s.name AS stadium,
       s.city AS city,
       collect(c.name) AS countries
ORDER BY s.city;

// ---------------------------------
// 5. HOTEL QUERIES
// ---------------------------------

// List all hotels
MATCH (h:Hotel)
RETURN h.name AS hotel,
       h.city AS city,
       h.price AS price,
       h.rating AS rating,
       h.capacity AS capacity
ORDER BY h.city, h.price;

// Hotels by city
MATCH (h:Hotel)
RETURN h.city AS city,
       count(h) AS hotel_count,
       avg(h.price) AS avg_price,
       avg(h.rating) AS avg_rating
ORDER BY hotel_count DESC;

// Most affordable hotels
MATCH (h:Hotel)
RETURN h.name AS hotel,
       h.city AS city,
       h.price AS price,
       h.rating AS rating
ORDER BY h.price ASC
LIMIT 5;

// Best rated hotels
MATCH (h:Hotel)
RETURN h.name AS hotel,
       h.city AS city,
       h.price AS price,
       h.rating AS rating
ORDER BY h.rating DESC
LIMIT 5;

// ---------------------------------
// 6. HOTEL RECOMMENDATIONS
// ---------------------------------

// Best hotels for Nigeria
MATCH (c:Country {name:"Nigeria"})-[:PLAYS_AT]->(s:Stadium)
      -[r:HAS_NEARBY_HOTEL]->(h:Hotel)
WITH h, r, s,
     (h.price * 0.4 + r.distance_km * 0.4 - h.rating * 0.2) AS score
RETURN h.name AS hotel,
       s.name AS stadium,
       s.city AS city,
       h.price AS price,
       h.rating AS rating,
       r.distance_km AS distance_km,
       r.travel_time_min AS travel_time_min,
       round(score, 2) AS score
ORDER BY score ASC
LIMIT 5;

// Best hotels for Morocco
MATCH (c:Country {name:"Morocco"})-[:PLAYS_AT]->(s:Stadium)
      -[r:HAS_NEARBY_HOTEL]->(h:Hotel)
WITH h, r, s,
     (h.price * 0.4 + r.distance_km * 0.4 - h.rating * 0.2) AS score
RETURN h.name AS hotel,
       s.name AS stadium,
       s.city AS city,
       h.price AS price,
       h.rating AS rating,
       r.distance_km AS distance_km,
       round(score, 2) AS score
ORDER BY score ASC
LIMIT 5;

// Best hotels for Egypt
MATCH (c:Country {name:"Egypt"})-[:PLAYS_AT]->(s:Stadium)
      -[r:HAS_NEARBY_HOTEL]->(h:Hotel)
WITH h, r, s,
     (h.price * 0.4 + r.distance_km * 0.4 - h.rating * 0.2) AS score
RETURN h.name AS hotel,
       s.name AS stadium,
       s.city AS city,
       h.price AS price,
       h.rating AS rating,
       r.distance_km AS distance_km,
       round(score, 2) AS score
ORDER BY score ASC
LIMIT 5;

// ---------------------------------
// 7. BUDGET QUERIES
// ---------------------------------

// Hotels under $100
MATCH (s:Stadium)-[r:HAS_NEARBY_HOTEL]->(h:Hotel)
WHERE h.price < 100
RETURN h.name AS hotel,
       h.city AS city,
       h.price AS price,
       h.rating AS rating,
       r.distance_km AS distance_km
ORDER BY h.price ASC;

// Best value hotels (good rating, low price, close distance)
MATCH (s:Stadium)-[r:HAS_NEARBY_HOTEL]->(h:Hotel)
WHERE h.price < 150 AND h.rating >= 4.0 AND r.distance_km < 5
RETURN h.name AS hotel,
       s.name AS stadium,
       h.city AS city,
       h.price AS price,
       h.rating AS rating,
       r.distance_km AS distance_km
ORDER BY h.price ASC;

// ---------------------------------
// 8. LUXURY HOTELS
// ---------------------------------

// Premium hotels (price > $200 or rating > 4.5)
MATCH (h:Hotel)
WHERE h.price > 200 OR h.rating > 4.5
RETURN h.name AS hotel,
       h.city AS city,
       h.price AS price,
       h.rating AS rating
ORDER BY h.rating DESC, h.price DESC;

// ---------------------------------
// 9. LOCATION ANALYSIS
// ---------------------------------

// Hotels near each stadium
MATCH (s:Stadium)-[r:HAS_NEARBY_HOTEL]->(h:Hotel)
RETURN s.name AS stadium,
       s.city AS city,
       count(h) AS nearby_hotels,
       avg(h.price) AS avg_price,
       avg(r.distance_km) AS avg_distance
ORDER BY nearby_hotels DESC;

// Closest hotels to stadiums
MATCH (s:Stadium)-[r:HAS_NEARBY_HOTEL]->(h:Hotel)
WHERE r.distance_km < 2
RETURN s.name AS stadium,
       h.name AS hotel,
       h.price AS price,
       h.rating AS rating,
       r.distance_km AS distance_km
ORDER BY r.distance_km ASC;

// ---------------------------------
// 10. COMPREHENSIVE RECOMMENDATION
// ---------------------------------

// Best overall recommendations across all countries
MATCH (c:Country)-[:PLAYS_AT]->(s:Stadium)
      -[r:HAS_NEARBY_HOTEL]->(h:Hotel)
WITH c, h, r, s,
     (h.price * 0.4 + r.distance_km * 0.4 - h.rating * 0.2) AS score
ORDER BY c.name, score ASC
RETURN c.name AS country,
       h.name AS hotel,
       s.city AS city,
       h.price AS price,
       h.rating AS rating,
       r.distance_km AS distance,
       round(score, 2) AS score
LIMIT 20;

// ---------------------------------
// 11. DATA VALIDATION
// ---------------------------------

// Check for hotels without stadium connections
MATCH (h:Hotel)
WHERE NOT (h)<-[:HAS_NEARBY_HOTEL]-()
RETURN h.name AS unconnected_hotel, h.city;

// Check for countries without stadium assignments
MATCH (c:Country)
WHERE NOT (c)-[:PLAYS_AT]->()
RETURN c.name AS unassigned_country;

// Verify all relationships
MATCH ()-[r]->()
RETURN type(r) AS relationship_type, count(r) AS count
ORDER BY count DESC;

// ---------------------------------
// 12. DELETE QUERIES (USE WITH CAUTION!)
// ---------------------------------

// Delete everything (WARNING: This will clear all data!)
// MATCH (n) DETACH DELETE n;

// Delete specific country and its relationships
// MATCH (c:Country {name:"SomeCountry"})
// DETACH DELETE c;

// Delete specific hotel
// MATCH (h:Hotel {name:"Hotel Name"})
// DETACH DELETE h;
