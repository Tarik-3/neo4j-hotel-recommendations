# API Response Examples

## New API Response Format

### Example 1: Nigeria Search

**Request:**
```
GET http://127.0.0.1:8000/best-hotels?country=Nigeria&limit=3
```

**Response:**
```json
[
  {
    "name": "Ibis Casa Voyageurs",
    "stadium_name": "Mohammed V Stadium",
    "city": "Casablanca",
    "price": 80.0,
    "rating": 3.6,
    "distance_km": 1.5,
    "score": 31.88
  },
  {
    "name": "Riad Dar Rabat",
    "stadium_name": "Prince Moulay Abdellah Stadium",
    "city": "Rabat",
    "price": 90.0,
    "rating": 3.9,
    "distance_km": 1.6,
    "score": 35.86
  },
  {
    "name": "Hotel Atlas",
    "stadium_name": "Mohammed V Stadium",
    "city": "Casablanca",
    "price": 120.0,
    "rating": 3.8,
    "distance_km": 0.6,
    "score": 47.48
  }
]
```

### Example 2: Morocco Search with Price Filter

**Request:**
```
GET http://127.0.0.1:8000/best-hotels?country=Morocco&max_price=150&limit=5
```

**Response:**
```json
[
  {
    "name": "Riad Marrakech Medina",
    "stadium_name": "Grand Stade de Marrakech",
    "city": "Marrakech",
    "price": 70.0,
    "rating": 3.7,
    "distance_km": 5.3,
    "score": 38.49
  },
  {
    "name": "Ibis Agadir",
    "stadium_name": "Adrar Stadium",
    "city": "Agadir",
    "price": 75.0,
    "rating": 3.6,
    "distance_km": 2.1,
    "score": 39.34
  },
  {
    "name": "Riad Dar Rabat",
    "stadium_name": "Prince Moulay Abdellah Stadium",
    "city": "Rabat",
    "price": 90.0,
    "rating": 3.9,
    "distance_km": 3.2,
    "score": 44.22
  },
  {
    "name": "Bahia Palace Riad",
    "stadium_name": "Grand Stade de Marrakech",
    "city": "Marrakech",
    "price": 110.0,
    "rating": 4.0,
    "distance_km": 4.8,
    "score": 45.28
  },
  {
    "name": "Farah Tanger Hotel",
    "stadium_name": "Ibn Battuta Stadium",
    "city": "Tangier",
    "price": 110.0,
    "rating": 3.8,
    "distance_km": 1.9,
    "score": 45.62
  }
]
```

### Example 3: Egypt Search

**Request:**
```
GET http://127.0.0.1:8000/best-hotels?country=Egypt&limit=3
```

**Response:**
```json
[
  {
    "name": "Ibis Casa Voyageurs",
    "stadium_name": "Mohammed V Stadium",
    "city": "Casablanca",
    "price": 80.0,
    "rating": 3.6,
    "distance_km": 2.8,
    "score": 39.76
  },
  {
    "name": "Riad Marrakech Medina",
    "stadium_name": "Grand Stade de Marrakech",
    "city": "Marrakech",
    "price": 70.0,
    "rating": 3.7,
    "distance_km": 6.5,
    "score": 43.05
  },
  {
    "name": "Hotel Le Diwan Rabat",
    "stadium_name": "Prince Moulay Abdellah Stadium",
    "city": "Rabat",
    "price": 130.0,
    "rating": 4.0,
    "distance_km": 2.9,
    "score": 51.18
  }
]
```

## Response Field Descriptions

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `name` | string | Hotel name | "Ibis Casa Voyageurs" |
| `stadium_name` | string | **[NEW]** Stadium where matches are held | "Mohammed V Stadium" |
| `city` | string | **[NEW]** City where hotel is located | "Casablanca" |
| `price` | float | Price per night in USD | 80.0 |
| `rating` | float | Hotel rating (1-5 stars) | 3.6 |
| `distance_km` | float | Distance from hotel to stadium | 1.5 |
| `score` | float | Recommendation score (lower = better) | 31.88 |

## Frontend Display Mapping

### How the Response Maps to Frontend

```json
API Response:
{
  "name": "Ibis Casa Voyageurs",
  "stadium_name": "Mohammed V Stadium",
  "city": "Casablanca",
  "price": 80.0,
  "rating": 3.6,
  "distance_km": 1.5,
  "score": 31.88
}
```

**Displayed as:**

```
┌─────────────────────────────────────┐
│ #1                                  │  ← index + 1
│ Ibis Casa Voyageurs                 │  ← name
│ 📍 Mohammed V Stadium - Casablanca  │  ← stadium_name - city
│ ┌───────────────────────────────┐   │
│ │ 💰 Price: $80.00              │   │  ← price (formatted)
│ │ ⭐ Rating: ★★★☆☆ 3.6         │   │  ← rating (stars + value)
│ │ 📍 Distance: 1.5 km           │   │  ← distance_km
│ │ 🎯 Score: 31.88 Best Match    │   │  ← score + badge
│ └───────────────────────────────┘   │
└─────────────────────────────────────┘
```

## Scoring Formula

The score is calculated as:
```
score = (price × 0.4) + (distance_km × 0.4) - (rating × 0.2)
```

**Weights:**
- **Price (40%):** Lower price is better
- **Distance (40%):** Closer to stadium is better
- **Rating (20%):** Higher rating is better

**Score Interpretation:**
- **Score < 40:** Excellent match (Best Match badge 🏆)
- **Score 40-70:** Great choice (Great Choice badge ✓)
- **Score > 70:** Good option (Good Option badge !)

## Example Scoring Breakdown

Hotel: "Ibis Casa Voyageurs"
- Price: $80 × 0.4 = $32
- Distance: 1.5 km × 0.4 = 0.6
- Rating: 3.6 × 0.2 = 0.72
- **Score: 32 + 0.6 - 0.72 = 31.88** ✅

## API Endpoints

### 1. Get Best Hotels

**URL:**
```
GET /best-hotels
```

**Parameters:**
```
country    (string, required)   - Country name (e.g., "Nigeria")
max_price  (float, optional)    - Maximum price per night
limit      (integer, optional)  - Number of results (1-20, default: 5)
```

**Examples:**
```
/best-hotels?country=Nigeria
/best-hotels?country=Morocco&max_price=150
/best-hotels?country=Egypt&limit=10
/best-hotels?country=Senegal&max_price=120&limit=5
```

### 2. Health Check

**URL:**
```
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "mode": "LIVE",
  "database": "Neo4j connected"
}
```

### 3. Root Endpoint

**URL:**
```
GET /
```

**Response:**
```json
{
  "message": "Hotel Recommendation API for Africa Cup of Nations (CAN)",
  "mode": "LIVE",
  "docs": "/docs",
  "endpoints": {
    "best_hotels": "/best-hotels?country=Egypt&max_price=150&limit=5"
  },
  "available_countries": [
    "Egypt", "Morocco", "Algeria", "Senegal",
    "Cameroon", "Nigeria", "Tunisia", "Ivory Coast"
  ]
}
```

## Error Responses

### 404 - Country Not Found

**Request:**
```
GET /best-hotels?country=InvalidCountry
```

**Response:**
```json
{
  "detail": "No hotels found for country 'InvalidCountry'. Available countries: Egypt, Morocco, Algeria, Senegal, Cameroon, Nigeria, Tunisia, Ivory Coast"
}
```

### 400 - Bad Parameters

**Request:**
```
GET /best-hotels?country=Nigeria&limit=100
```

**Response:**
```json
{
  "detail": "ensure this value is less than or equal to 20"
}
```

## Testing the API

### Using curl

```bash
# Basic search
curl "http://127.0.0.1:8000/best-hotels?country=Nigeria"

# With formatting
curl -s "http://127.0.0.1:8000/best-hotels?country=Nigeria&limit=3" | python -m json.tool

# With price filter
curl "http://127.0.0.1:8000/best-hotels?country=Morocco&max_price=150&limit=5"
```

### Using Python

```python
import requests
import json

url = "http://127.0.0.1:8000/best-hotels"
params = {
    "country": "Nigeria",
    "max_price": 150,
    "limit": 5
}

response = requests.get(url, params=params)
hotels = response.json()

for hotel in hotels:
    print(f"{hotel['name']} - {hotel['stadium_name']} ({hotel['city']})")
    print(f"  Price: ${hotel['price']}, Rating: {hotel['rating']}, Distance: {hotel['distance_km']}km")
    print(f"  Score: {hotel['score']}")
    print()
```

### Using Browser

Simply visit:
```
http://127.0.0.1:8000/best-hotels?country=Nigeria&limit=5
```

You'll see the JSON response formatted in your browser!

## Interactive API Documentation

**Swagger UI (recommended):**
```
http://127.0.0.1:8000/docs
```

Features:
- Try out endpoints
- See request/response examples
- View parameter descriptions
- Test in real-time

**ReDoc:**
```
http://127.0.0.1:8000/redoc
```

Features:
- Beautiful documentation
- Detailed descriptions
- Examples
- Read-only interface

---

**The API now includes full stadium information in every response!** ✅
