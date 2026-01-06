# Morocco CAN 2025 - Database Setup Guide

## 🎯 What Was Created

### Python Script
**File:** `populate_morocco_can.py`

Comprehensive script that creates:
- ✅ **8 Countries**: Nigeria, Morocco, Senegal, Egypt, Cameroon, Algeria, Tunisia, Ivory Coast
- ✅ **5 Stadiums**: All in Morocco (Casablanca, Rabat, Marrakech, Tangier, Agadir)
- ✅ **21 Hotels**: Distributed across Moroccan cities with realistic data
- ✅ **16 PLAYS_AT relationships**: Countries assigned to stadiums
- ✅ **21 HAS_NEARBY_HOTEL relationships**: Stadiums connected to nearby hotels with distance and travel time

### Cypher Queries
**File:** `queries_morocco_can.cypher`

Ready-to-use queries for:
- Viewing all data
- Counting statistics
- Finding best hotels by country
- Budget and luxury hotel searches
- Location analysis
- Data validation

## 📊 Database Structure

### Countries (8 nodes)
```
Nigeria, Morocco, Senegal, Egypt, Cameroon, Algeria, Tunisia, Ivory Coast
```

### Stadiums (5 nodes in Morocco)
| Stadium | City | Capacity |
|---------|------|----------|
| Mohammed V Stadium | Casablanca | 45,891 |
| Prince Moulay Abdellah Stadium | Rabat | 52,000 |
| Grand Stade de Marrakech | Marrakech | 45,240 |
| Ibn Battuta Stadium | Tangier | 45,000 |
| Adrar Stadium | Agadir | 45,480 |

### Hotels (21 nodes across Morocco)

#### Casablanca (4 hotels)
- Hotel Atlas - $120/night, 3.8★
- Hyatt Regency Casablanca - $150/night, 4.5★
- Ibis Casa Voyageurs - $80/night, 3.6★
- Kenzi Tower Hotel - $135/night, 4.2★

#### Rabat (4 hotels)
- Sofitel Rabat Jardin des Roses - $200/night, 4.7★
- Hotel Le Diwan Rabat - $130/night, 4.0★
- Riad Dar Rabat - $90/night, 3.9★
- Movenpick Hotel Mansour Eddahbi - $165/night, 4.4★

#### Marrakech (5 hotels)
- Kenzi Menara Palace - $160/night, 4.3★
- La Mamounia - $300/night, 4.9★
- Riad Marrakech Medina - $70/night, 3.7★
- Palais Namaskar - $280/night, 4.8★
- Hotel Les Jardins de la Koutoubia - $145/night, 4.1★

#### Tangier (4 hotels)
- Hilton Garden Inn Tangier City Center - $140/night, 4.2★
- Hotel El Minzah - $120/night, 4.0★
- Ibis Tangier - $85/night, 3.5★
- Farah Tanger Hotel - $110/night, 3.8★

#### Agadir (4 hotels)
- Royal Atlas Hotel - $150/night, 4.3★
- Sofitel Agadir Thalassa Sea & Spa - $220/night, 4.7★
- Ibis Agadir - $75/night, 3.6★
- Atlantic Palace Resort - $180/night, 4.4★

### Relationships

#### PLAYS_AT (16 relationships)
Countries assigned to 2 stadiums each for their matches.

Example:
- Nigeria → Mohammed V Stadium (Casablasa)
- Nigeria → Prince Moulay Abdellah Stadium (Rabat)

#### HAS_NEARBY_HOTEL (21 relationships)
Each stadium connected to all hotels in the same city with:
- `distance_km`: Random realistic distance (0.5-8 km)
- `travel_time_min`: Calculated travel time

## 🚀 How to Use

### 1. Populate the Database

```bash
python populate_morocco_can.py
```

**Expected Output:**
```
✓ Database cleared
✓ Created 8 countries
✓ Created 5 stadiums in Morocco
✓ Created 21 hotels across Morocco
✓ Created 16 PLAYS_AT relationships
✓ Created 21 HAS_NEARBY_HOTEL relationships
```

### 2. Start the API Server

```bash
# Option 1: Quick start
start_server.bat

# Option 2: Manual
uvicorn app.main:app --port 8000
```

### 3. Use the Frontend

```bash
# Option 1: One-click
launch.bat

# Option 2: Manual
# Double-click frontend/index.html
```

### 4. Test in Neo4j Browser

1. Open http://localhost:7474
2. Copy queries from `queries_morocco_can.cypher`
3. Paste and execute

## 📋 Sample Queries

### Find Best Hotels for a Country

```cypher
MATCH (c:Country {name:"Nigeria"})-[:PLAYS_AT]->(s:Stadium)
      -[r:HAS_NEARBY_HOTEL]->(h:Hotel)
WITH h, r, s,
     (h.price * 0.4 + r.distance_km * 0.4 - h.rating * 0.2) AS score
RETURN h.name AS hotel,
       s.name AS stadium,
       h.price AS price,
       h.rating AS rating,
       r.distance_km AS distance,
       score
ORDER BY score ASC
LIMIT 5;
```

### Budget Hotels (Under $100)

```cypher
MATCH (s:Stadium)-[r:HAS_NEARBY_HOTEL]->(h:Hotel)
WHERE h.price < 100
RETURN h.name AS hotel,
       h.city AS city,
       h.price AS price,
       h.rating AS rating
ORDER BY h.price ASC;
```

### Luxury Hotels

```cypher
MATCH (h:Hotel)
WHERE h.rating >= 4.5
RETURN h.name AS hotel,
       h.city AS city,
       h.price AS price,
       h.rating AS rating
ORDER BY h.rating DESC;
```

## 🔧 Customization

### Add More Hotels

Edit `populate_morocco_can.py` and add to the `hotels` list:

```python
{"name": "New Hotel", "city": "Casablanca", "price": 140, "rating": 4.2, "capacity": 200}
```

Then re-run: `python populate_morocco_can.py`

### Change Stadium Assignments

Edit the `assignments` list in `create_country_stadium_relationships()`:

```python
("YourCountry", "Stadium Name"),
```

### Adjust Scoring Weights

The scoring formula is in `app/services.py`:

```python
(h.price * 0.4 + r.distance_km * 0.4 - h.rating * 0.2) AS score
```

Adjust the weights (must sum to 1.0):
- Increase price weight if budget is most important
- Increase distance weight if proximity matters most
- Increase rating weight if quality is priority

## 🎯 API Endpoints

### Get Best Hotels
```
GET http://127.0.0.1:8000/best-hotels?country=Nigeria&max_price=150&limit=5
```

**Parameters:**
- `country` (required): Country name
- `max_price` (optional): Maximum price filter
- `limit` (optional): Number of results (default: 5)

### Health Check
```
GET http://127.0.0.1:8000/health
```

### API Documentation
```
http://127.0.0.1:8000/docs
```

## 📈 Database Statistics

After running `populate_morocco_can.py`:

- **Total Nodes**: 34
  - Countries: 8
  - Stadiums: 5
  - Hotels: 21

- **Total Relationships**: 37
  - PLAYS_AT: 16
  - HAS_NEARBY_HOTEL: 21

## 🎨 Frontend Features

The web interface at `frontend/index.html` allows visitors to:

1. **Select a country** from dropdown
2. **Set maximum price** (optional)
3. **Choose number of results** (1-20)
4. **View recommendations** with:
   - Hotel name and rank
   - Price per night
   - Star rating
   - Distance from stadium
   - Overall match score
   - Quality badge (Best Match, Great Choice, Good Option)

## ✅ Validation

### Check Data Integrity

```cypher
// Count all nodes
MATCH (c:Country) WITH count(c) AS countries
MATCH (s:Stadium) WITH countries, count(s) AS stadiums
MATCH (h:Hotel) WITH countries, stadiums, count(h) AS hotels
RETURN countries, stadiums, hotels;

// Check relationships
MATCH ()-[r]->()
RETURN type(r) AS relationship_type, count(r) AS count;

// Verify all hotels have stadium connections
MATCH (h:Hotel)
WHERE NOT (h)<-[:HAS_NEARBY_HOTEL]-()
RETURN h.name AS unconnected_hotel;
```

## 🐛 Troubleshooting

### Script Fails to Run

**Check:**
1. Neo4j is running: Open http://localhost:7474
2. Credentials in `.env` are correct
3. Python dependencies installed: `pip install -r requirements.txt`

### No Hotels Found in API

**Solution:**
```bash
python populate_morocco_can.py
```

### Frontend Shows No Results

**Check:**
1. API server is running on port 8000
2. Database has data: Run `python test_connection.py`
3. Browser console for errors (F12)

## 📚 Files Reference

| File | Purpose |
|------|---------|
| `populate_morocco_can.py` | Main population script |
| `queries_morocco_can.cypher` | Pre-made Cypher queries |
| `frontend/index.html` | Web interface |
| `app/main.py` | FastAPI server |
| `app/services.py` | Query logic |
| `.env` | Database credentials |

## 🎉 Next Steps

1. ✅ Database populated with Morocco data
2. ✅ API server ready to use
3. ✅ Frontend interface available
4. 🎯 **Open frontend and start searching!**

**Quick Launch:**
```bash
launch.bat
```

Or visit: http://127.0.0.1:8000/docs for API testing

---

**Enjoy the Africa Cup of Nations 2025 in Morocco! 🇲🇦⚽🏨**
