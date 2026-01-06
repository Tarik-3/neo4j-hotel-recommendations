# 🚀 Quick Reference Card

## Start Everything (Fastest)
```bash
launch.bat
```
Opens API server + frontend automatically!

## URLs to Remember
| What | URL |
|------|-----|
| 🎨 Frontend | Open `frontend/index.html` in browser |
| 📚 API Docs | http://127.0.0.1:8000/docs |
| 🏠 API Root | http://127.0.0.1:8000/ |
| ❤️ Health Check | http://127.0.0.1:8000/health |
| 🔍 Neo4j Browser | http://localhost:7474 |

## Common Commands

### Start API Server
```bash
# Easy way
start_server.bat

# Manual way
uvicorn app.main:app --port 8000

# With auto-reload (development)
uvicorn app.main:app --port 8000 --reload
```

### Test & Setup
```bash
# Test Neo4j connection
python test_connection.py

# Populate database with sample data
python populate_db.py

# Run API tests
python test_api.py
```

### Emergency: Use Mock Data
```powershell
$env:USE_MOCK="true"
python -m uvicorn app.main:app --port 8000
```

## Frontend Usage

### Search Hotels
1. Select country from dropdown
2. Set max price (optional)
3. Choose number of results (1-20)
4. Click "Search Hotels"

### Available Countries
Egypt • Morocco • Algeria • Senegal • Cameroon • Nigeria • Tunisia • Ivory Coast

### What You See
- **Price** - $ per night
- **Rating** - ⭐ 1-5 stars
- **Distance** - km from stadium
- **Score** - Lower = Better

## File Locations

| File | Purpose |
|------|---------|
| `frontend/index.html` | Web interface |
| `app/main.py` | API server |
| `.env` | Database credentials |
| `populate_db.py` | Add sample data |
| `test_connection.py` | Test Neo4j |

## Troubleshooting

### "API is not running"
→ Run: `start_server.bat` or `uvicorn app.main:app --port 8000`

### "No hotels found"
→ Run: `python populate_db.py`

### "Authentication failed"
→ Check `.env` file, verify NEO4J_PASSWORD

### Frontend not updating
→ Hard refresh: `Ctrl + F5`

### Port 8000 in use
→ Use different port: `uvicorn app.main:app --port 8001`

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `Enter` | Search (when in form field) |
| `F12` | Open browser dev tools |
| `Ctrl + F5` | Hard refresh page |
| `Ctrl + C` | Stop API server (in terminal) |

## Quick Examples

### Example 1: Find cheap hotels in Egypt
```
Country: Egypt
Max Price: 100
Results: 5
```

### Example 2: Top hotel in Morocco
```
Country: Morocco
Max Price: [empty]
Results: 1
```

### Example 3: Compare all Senegal options
```
Country: Senegal
Max Price: [empty]
Results: 10
```

## Support Files

- 📖 Full docs: `README.md`
- 🔧 Setup help: `NEO4J_SETUP_GUIDE.md`
- ⚡ Quick start: `QUICK_START.md`
- 🎨 Frontend docs: `frontend/README.md`
- 📋 Usage guide: `frontend/USAGE_GUIDE.md`

## Project Status
Check `PROJECT_STATUS.md` for current features and development status.

---

**Need help?** Check the documentation files listed above! 📚
