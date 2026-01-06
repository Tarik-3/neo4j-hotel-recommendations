# Hotel Recommendation System for CAN (Africa Cup of Nations)

A FastAPI-based hotel recommendation system with a beautiful web frontend that helps visitors find the best hotels near stadiums where their national team will play during the Africa Cup of Nations (CAN).

## 🌟 Features

### Backend API
- **Smart Hotel Recommendations**: Finds hotels based on:
  - Where the visitor's country team will play
  - Hotel price (with optional maximum price filter)
  - Distance from the stadium
  - Hotel rating

- **Scoring Algorithm**: Hotels are ranked using a weighted score:
  - Price: 40% weight
  - Distance: 40% weight
  - Rating: 20% weight (inverted - higher rating = better)

- **Dual Mode Operation**:
  - LIVE mode with Neo4j database
  - MOCK mode with sample data (automatic fallback)

### Frontend Interface
- 🎨 **Beautiful UI**: Modern, responsive design with gradient themes
- 🔍 **Easy Search**: Dropdown country selection with optional filters
- 📊 **Rich Display**: Shows price, rating, distance, and match score
- ⚡ **Real-time**: Live API status indicator
- 📱 **Responsive**: Works perfectly on desktop, tablet, and mobile

## 🚀 Quick Start (Easiest Way)

### One-Click Launch

1. Make sure Neo4j is running (see setup instructions below)
2. Double-click `launch.bat`
3. The API server and frontend will open automatically!

That's it! The frontend will open in your browser and connect to the API.

### Manual Launch

If you prefer to start things manually:

1. **Start the API Server**:
   ```bash
   start_server.bat
   # OR
   uvicorn app.main:app --port 8000
   ```

2. **Open the Frontend**:
   - Double-click `frontend/index.html`
   - OR open it in your browser: `start frontend\index.html`

## Prerequisites

- Python 3.8+
- Neo4j Database (4.x or 5.x)
- Neo4j Desktop OR Neo4j Community Edition installed and running

## Setup Instructions

### 1. Neo4j Database Setup

#### Option A: Using Neo4j Desktop
1. Open Neo4j Desktop
2. Create a new project or use an existing one
3. Create a new database or start an existing one
4. Note the connection details:
   - Bolt URL (e.g., `neo4j://localhost:7687` or `bolt://localhost:7687`)
   - Username (default: `neo4j`)
   - Password (the one you set)

#### Option B: Using Neo4j Community Edition
1. Install Neo4j from https://neo4j.com/download/
2. Start Neo4j service:
   ```bash
   neo4j start
   ```
3. First-time setup:
   - Go to http://localhost:7474
   - Default username: `neo4j`
   - Default password: `neo4j`
   - You'll be prompted to change the password

### 2. Configure Environment Variables

Update the `.env` file with your Neo4j credentials:

```env
NEO4J_URI=neo4j://127.0.0.1:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=your_password_here
```

**Important**: Replace `your_password_here` with your actual Neo4j password.

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

Or if using a virtual environment:

```bash
# Create virtual environment
python -m venv env

# Activate it
# On Windows:
.\env\Scripts\activate
# On Linux/Mac:
source env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 4. Test Database Connection

Before populating data, test your connection:

```bash
python test_connection.py
```

If successful, you should see:
```
✓ Connection successful!
✓ Found X nodes in database
```

If you see an authentication error:
- Verify your password in `.env` is correct
- Make sure Neo4j is running
- Check that the URI and port are correct

### 5. Populate Database with Sample Data

Once the connection test passes:

```bash
python populate_db.py
```

This will create:
- 8 countries (Egypt, Morocco, Algeria, Senegal, etc.)
- 4 stadiums (Cairo International Stadium, Stade Mohammed V, etc.)
- 13 hotels near various stadiums
- Relationships showing which countries play at which stadiums
- Distance relationships between stadiums and hotels

### 6. Start the API Server

```bash
uvicorn app.main:app --reload
```

Or:

```bash
python -m uvicorn app.main:app --reload
```

The API will be available at: http://127.0.0.1:8000

## API Usage

### Get Best Hotels for a Country

**Endpoint**: `GET /best-hotels`

**Parameters**:
- `country` (required): Name of the country (e.g., "Egypt", "Morocco")
- `max_price` (optional): Maximum price per night
- `limit` (optional): Number of hotels to return (default: 5)

**Examples**:

1. Find best hotels for Egypt:
   ```
   http://127.0.0.1:8000/best-hotels?country=Egypt
   ```

2. Find hotels for Morocco under $150:
   ```
   http://127.0.0.1:8000/best-hotels?country=Morocco&max_price=150
   ```

3. Find top 3 hotels for Senegal:
   ```
   http://127.0.0.1:8000/best-hotels?country=Senegal&limit=3
   ```

**Response Format**:
```json
[
  {
    "name": "Le Meridien Cairo",
    "price": 180.0,
    "rating": 4.7,
    "distance_km": 3.5,
    "score": 73.46
  },
  {
    "name": "Cairo Marriott Hotel",
    "price": 150.0,
    "rating": 4.5,
    "distance_km": 5.2,
    "score": 61.18
  }
]
```

### Interactive API Documentation

Once the server is running, visit:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## 🎨 Using the Frontend

The web interface provides an easy way to search for hotels without using API endpoints directly.

### Features:
1. **Country Selection** - Choose from 8 African countries
2. **Price Filter** - Set maximum price (optional)
3. **Results Limit** - Control how many hotels to display (1-20)
4. **Live Results** - Beautiful cards showing all hotel details
5. **Smart Badges** - "Best Match", "Great Choice", "Good Option"
6. **API Status** - See if you're in LIVE or MOCK mode

### How to Use:
1. Select a country from the dropdown
2. Optionally set a maximum price
3. Click "Search Hotels"
4. View the ranked results with all details

For more details, see [frontend/README.md](frontend/README.md)

## Project Structure

```
Neo4j/
├── app/
│   ├── __init__.py       # Package initializer
│   ├── main.py           # FastAPI application with CORS
│   ├── main_flexible.py  # Alternative flexible mode
│   ├── database.py       # Neo4j connection
│   ├── schemas.py        # Pydantic models
│   ├── services.py       # Business logic (Neo4j queries)
│   └── services_mock.py  # Mock data service
├── frontend/
│   ├── index.html        # Web interface (single-page app)
│   └── README.md         # Frontend documentation
├── .env                  # Environment variables
├── populate_db.py        # Database population script
├── test_connection.py    # Connection test script
├── test_api.py           # API testing script
├── launch.bat            # One-click launcher
├── start_server.bat      # Server startup script
├── requirements.txt      # Python dependencies
├── README.md             # This file
├── NEO4J_SETUP_GUIDE.md  # Detailed setup guide
└── QUICK_START.md        # Quick start guide
```

## Troubleshooting

### Authentication Error
**Problem**: `Neo.ClientError.Security.Unauthorized`

**Solutions**:
1. Verify password in `.env` file (no quotes needed)
2. Reset Neo4j password:
   - In Neo4j Browser: `:server change-password`
   - Or reinstall Neo4j Desktop database
3. Check if you're using the correct database instance

### Connection Refused
**Problem**: Cannot connect to Neo4j

**Solutions**:
1. Make sure Neo4j is running:
   - Neo4j Desktop: Check if database is started
   - Community Edition: `neo4j status`
2. Verify the port (7687 for Bolt protocol)
3. Check firewall settings

### Module Not Found
**Problem**: `ModuleNotFoundError: No module named 'X'`

**Solutions**:
1. Install dependencies: `pip install -r requirements.txt`
2. Make sure you're in the correct virtual environment
3. Try installing the specific package: `pip install X`

### Empty Results
**Problem**: API returns empty list

**Solutions**:
1. Check if database is populated: `python test_connection.py`
2. Re-run population script: `python populate_db.py`
3. Verify country name spelling (case-sensitive)

## Sample Data

The database includes:

**Countries**: Egypt, Morocco, Algeria, Senegal, Cameroon, Nigeria, Tunisia, Ivory Coast

**Stadiums**:
- Cairo International Stadium (Cairo)
- Stade Mohammed V (Casablanca)
- Stade du 5 Juillet (Algiers)
- Stade Abdoulaye Wade (Diamniadio)

**Hotels**: Range from budget ($50-70/night) to luxury ($200-250/night)

## Extending the Project

### Add More Data
Edit `populate_db.py` to add:
- More countries and teams
- Additional stadiums
- More hotels
- Different match schedules

### Modify Scoring Algorithm
Edit the query in `app/services.py` to adjust weights:
```python
score = (h.price * weight1 + r.distance_km * weight2 - h.rating * weight3)
```

### Add New Features
- Filter by hotel amenities
- Consider match dates and schedules
- Add hotel availability
- Include public transportation info
- Add user reviews and ratings

## License

This project is for educational purposes.

## Support

For issues:
1. Check the Troubleshooting section
2. Verify Neo4j is running: `python test_connection.py`
3. Check API logs for error messages
