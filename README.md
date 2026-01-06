# Neo4j Hotel Recommendations System

A FastAPI-based hotel recommendation engine for the Africa Cup of Nations (CAN) 2025 tournament in Morocco, with a beautiful web frontend and Neo4j graph database backend.

## 🏗️ Project Structure

```
Neo4j/
├── app/                      # FastAPI application
│   ├── main.py              # FastAPI server & endpoints
│   ├── database.py          # Neo4j connection management
│   ├── schemas.py           # Pydantic data models
│   ├── services.py          # Business logic & queries
│   └── __init__.py
│
├── frontend/                 # Web user interface
│   ├── index.html           # Single-page application
│   └── README.md            # Frontend documentation
│
├── scripts/                  # Setup & utility scripts
│   ├── populate_morocco_can.py    # Database initialization
│   ├── populate_db.py             # Alternative DB setup
│   ├── test_api.py                # API endpoint testing
│   ├── test_connection.py         # Neo4j connection test
│   ├── test_direct.py             # Direct query testing
│   ├── start_server.bat           # Windows batch startup
│   ├── start_server.ps1           # PowerShell startup
│   └── launch.bat                 # Quick launch script
│
├── queries/                  # Cypher query reference
│   └── queries_morocco_can.cypher
│
├── docs/                     # Documentation
│   ├── README.md                     # Documentation index
│   ├── QUICK_START.md                # Quick start guide
│   ├── QUICK_REFERENCE.md            # Command reference
│   ├── COMPLETE_SETUP_GUIDE.md       # Detailed setup
│   ├── NEO4J_SETUP_GUIDE.md          # Neo4j configuration
│   ├── MOROCCO_CAN_SETUP.md          # Tournament data setup
│   ├── FRONTEND_SUMMARY.md           # UI/UX documentation
│   ├── STADIUM_UPDATE.md             # Stadium data addition
│   ├── API_RESPONSE_EXAMPLES.md      # API response formats
│   ├── IMPROVEMENTS_SUMMARY.md       # Recent changes
│   ├── FINAL_SUMMARY.md              # Project overview
│   ├── BEFORE_AFTER_COMPARISON.md    # Comparison of versions
│   └── IMPLEMENTATION_CHECKLIST.md   # Verification checklist
│
├── env/                      # Python virtual environment
├── .env                      # Environment variables (credentials)
├── requirements.txt          # Python dependencies
├── organize_files.ps1        # File organization script
└── README.md                 # This file
```

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.13+
- Neo4j Server (local or remote)
- Windows (for .bat scripts) or PowerShell

### 2. Setup

```bash
# Install Python dependencies
pip install -r requirements.txt

# Configure environment
# Edit .env with your Neo4j credentials:
# NEO4J_URI=bolt://localhost:7687
# NEO4J_USER=neo4j
# NEO4J_PASSWORD=your_password
```

### 3. Initialize Database

```bash
# From scripts/ directory
python populate_morocco_can.py
```

### 4. Start API Server

```bash
# Option A: Windows Batch
scripts/start_server.bat

# Option B: PowerShell
scripts/start_server.ps1

# Option C: Direct Python
python -m uvicorn app.main:app --port 8000
```

### Server Modes

- **Live-only (default):** [app/main.py](app/main.py) always uses Neo4j data. If Neo4j is unreachable, the server exits with guidance to fix the connection.
- **Flexible (optional):** [app/main_flexible.py](app/main_flexible.py) supports falling back to mock data. Use this only for local demos when Neo4j isn’t available.

Start flexible mode manually:

```bash
python -m uvicorn app.main_flexible:app --port 8001
```

### 5. Access the Application

- **Frontend:** http://127.0.0.1:8000/
- **API Docs:** http://127.0.0.1:8000/docs
- **Health Check:** http://127.0.0.1:8000/health

## 📋 Features

### Database
- **8 Countries:** Nigeria, Morocco, Egypt, Senegal, Cameroon, Algeria, Tunisia, Ivory Coast
- **5 Moroccan Stadiums:** Fes, Casablanca, Marrakech, Rabat, Tangier
- **28 Hotels** across 5 cities with realistic pricing ($70-$300/night) and ratings (3.5-4.9★)
- **Relationships:** PLAYS_AT (country→stadium), HAS_NEARBY_HOTEL (stadium→hotel)

### API Endpoints

#### GET `/best-hotels`
Returns best hotel recommendations for a country.

**Parameters:**
- `country` (required): Country name (e.g., "Morocco")
- `max_price` (optional): Maximum price per night (default: 10000)
- `limit` (optional): Number of results (default: 5)

**Response:**
```json
[
  {
    "name": "Hotel Atlas",
    "stadium_name": "Stade de Fes",
    "city": "Fes",
    "price": 120.0,
    "rating": 4.5,
    "distance_km": 2.5,
    "score": 98.5
  }
]
```

**Scoring:** `(price × 0.4) + (distance × 0.4) - (rating × 0.2)`

### Frontend
- **Country Selection:** Dropdown with all 8 tournament countries
- **Price Filtering:** Set maximum price per night
- **Result Limiting:** Control number of results displayed
- **Beautiful UI:** Gradient background, responsive grid layout
- **Stadium Info:** Blue highlight showing stadium name and city

## 🛠️ Available Scripts

| Script | Purpose |
|--------|---------|
| `populate_morocco_can.py` | Create tournament data in Neo4j |
| `populate_db.py` | Alternative database setup |
| `test_api.py` | Test API endpoints |
| `test_connection.py` | Verify Neo4j connection |
| `test_direct.py` | Run Cypher queries directly |
| `start_server.bat` | Launch API on Windows |
| `start_server.ps1` | Launch API with PowerShell |
| `launch.bat` | Quick launch shortcut |

## 📚 Documentation

See [docs/README.md](docs/README.md) for:
- Detailed setup instructions
- API response examples
- Database schema documentation
- Frontend implementation details
- Troubleshooting guide

**Quick References:**
- [QUICK_START.md](docs/QUICK_START.md) - Get running in 5 minutes
- [QUICK_REFERENCE.md](docs/QUICK_REFERENCE.md) - Common commands
- [API_RESPONSE_EXAMPLES.md](docs/API_RESPONSE_EXAMPLES.md) - Response formats

## 🔧 Technical Stack

- **Backend:** FastAPI 0.109.2 (Python web framework)
- **Database:** Neo4j 5.x (Graph database)
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **ORM/Query:** Neo4j Python Driver
- **Data Validation:** Pydantic
- **API Documentation:** Swagger UI (FastAPI built-in)

## ✅ Verification

Run the verification checklist in [docs/IMPLEMENTATION_CHECKLIST.md](docs/IMPLEMENTATION_CHECKLIST.md) to ensure everything is working correctly.

## 📝 Recent Updates

See [docs/FINAL_SUMMARY.md](docs/FINAL_SUMMARY.md) for comprehensive project overview and [docs/IMPROVEMENTS_SUMMARY.md](docs/IMPROVEMENTS_SUMMARY.md) for recent enhancements.

## 🤝 Contributing

- Keep API logic in `app/services.py`
- Add new hotels to `scripts/populate_morocco_can.py`
- Update documentation in `docs/` folder
- Store queries in `queries/queries_morocco_can.cypher`

## 📞 Support

For issues:
1. Check [docs/](docs/) for relevant documentation
2. Review [docs/QUICK_REFERENCE.md](docs/QUICK_REFERENCE.md) for commands
3. Verify database connection in `test_connection.py`
4. Check API health: `curl http://127.0.0.1:8000/health`

---

**Last Updated:** 2025
**Status:** Production Ready ✅
