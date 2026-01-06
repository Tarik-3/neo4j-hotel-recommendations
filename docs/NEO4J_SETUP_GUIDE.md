# Neo4j Database Connection - Troubleshooting Guide

This guide will help you fix the Neo4j authentication issue and get your database connected.

## Problem

You're seeing this error:
```
Neo.ClientError.Security.Unauthorized: The client is unauthorized due to authentication failure.
```

## Solutions

### Option 1: Reset Neo4j Password (Recommended)

#### If using Neo4j Desktop:
1. Open Neo4j Desktop
2. Select your database/DBMS
3. Click on the three dots (•••) menu
4. Select "Reset DBMS password"
5. Set a new password
6. Update your `.env` file with the new password:
   ```
   NEO4J_PASSWORD=your_new_password
   ```
7. Start the database
8. Run `python test_connection.py` to verify

#### If using Neo4j Community Edition:
1. Stop Neo4j: `neo4j stop`
2. Reset password using neo4j-admin:
   ```bash
   neo4j-admin dbms set-initial-password your_new_password
   ```
3. Start Neo4j: `neo4j start`
4. Update your `.env` file
5. Test connection: `python test_connection.py`

### Option 2: Check Current Password

The current `.env` file has:
```
NEO4J_PASSWORD=Tarik2003
```

Try these common variations in `.env` (one at a time):
- `NEO4J_PASSWORD=neo4j` (default password)
- `NEO4J_PASSWORD=Tarik2003`
- `NEO4J_PASSWORD=tarik2003`

After each change, test with: `python test_connection.py`

### Option 3: Use Neo4j Browser to Reset

1. Make sure Neo4j is running
2. Go to http://localhost:7474 in your browser
3. Try logging in with username `neo4j` and various passwords
4. If you get in, change the password:
   ```cypher
   :server change-password
   ```
5. Follow the prompts to set a new password
6. Update `.env` with the new password

### Option 4: Fresh Database (Last Resort)

If nothing works, create a fresh database:

#### Neo4j Desktop:
1. Create a new DBMS (database)
2. Set a new password during creation
3. Start the database
4. Update `.env` with the new credentials and connection details
5. Run `python populate_db.py` to add data

## Testing the Solution

After fixing the password, follow these steps:

### 1. Test Connection
```bash
python test_connection.py
```

Expected output:
```
✓ Connection successful!
✓ Found X nodes in database
```

### 2. Populate Database
```bash
python populate_db.py
```

Expected output:
```
Database cleared
Created 8 countries
Created 4 stadiums
Created 8 PLAYS_AT relationships
Created 13 hotels with relationships

Node counts:
  Country: 8
  Stadium: 4
  Hotel: 13

Relationship counts:
  PLAYS_AT: 8
  HAS_NEARBY_HOTEL: 13

Database populated successfully!
```

### 3. Start API Server
```bash
# Using the Python interpreter found in your system
C:/Users/tarik/AppData/Local/Programs/Python/Python313/python.exe -m uvicorn app.main:app --port 8000
```

Expected output:
```
✓ Connected to Neo4j database
INFO: Uvicorn running on http://127.0.0.1:8000
```

### 4. Test API
Open your browser and visit:
- API Documentation: http://127.0.0.1:8000/docs
- Root endpoint: http://127.0.0.1:8000/
- Test query: http://127.0.0.1:8000/best-hotels?country=Egypt

## Alternative: Run in Mock Mode

If you can't get Neo4j working right now, you can still test the API with sample data:

### Windows PowerShell:
```powershell
$env:USE_MOCK="true"
C:/Users/tarik/AppData/Local/Programs/Python/Python313/python.exe -m uvicorn app.main:app --port 8000
```

### Windows CMD:
```cmd
set USE_MOCK=true
C:\Users\tarik\AppData\Local\Programs\Python\Python313\python.exe -m uvicorn app.main:app --port 8000
```

The API will work with sample data for Egypt, Morocco, Algeria, and Senegal.

## Common Issues

### Issue: "Module not found: uvicorn"
**Solution:**
```bash
C:/Users/tarik/AppData/Local/Programs/Python/Python313/python.exe -m pip install fastapi uvicorn neo4j pydantic python-dotenv
```

### Issue: "Port 8000 already in use"
**Solution:** Use a different port:
```bash
C:/Users/tarik/AppData/Local/Programs/Python/Python313/python.exe -m uvicorn app.main:app --port 8001
```

### Issue: Neo4j not running
**Check if running:**
- Neo4j Desktop: Check the database status in the UI
- Community Edition: Run `neo4j status`

**Start Neo4j:**
- Neo4j Desktop: Click the "Start" button
- Community Edition: Run `neo4j start`

### Issue: Wrong URI or Port
The `.env` file should have:
```
NEO4J_URI=neo4j://127.0.0.1:7687
```

Common alternatives:
- `bolt://127.0.0.1:7687` (alternative protocol name)
- `neo4j://localhost:7687`
- `bolt://localhost:7687`

If Neo4j is configured on a different port, check:
- Neo4j Desktop: Settings → Connection → Bolt port
- Community Edition: Check `conf/neo4j.conf` for `dbms.connector.bolt.listen_address`

## Quick Reference

### Commands
```bash
# Test connection
python test_connection.py

# Populate database
python populate_db.py

# Run tests
python test_direct.py

# Start API (normal mode)
C:/Users/tarik/AppData/Local/Programs/Python/Python313/python.exe -m uvicorn app.main:app --port 8000

# Start API (mock mode)
$env:USE_MOCK="true"; C:/Users/tarik/AppData/Local/Programs/Python/Python313/python.exe -m uvicorn app.main:app --port 8000
```

### Files to Check
- `.env` - Database credentials
- `test_connection.py` - Test database connection
- `populate_db.py` - Add sample data
- `app/main.py` - API server (with auto-fallback to mock mode)

## Need More Help?

1. Check Neo4j logs:
   - Desktop: Click on "Terminal" or "Logs" in Neo4j Desktop
   - Community Edition: Check `logs/` directory in Neo4j installation

2. Verify Neo4j is actually running:
   - Open http://localhost:7474 in browser
   - Should show Neo4j Browser interface

3. Test with Neo4j Browser first:
   - Log in at http://localhost:7474
   - Run a simple query: `RETURN 1`
   - If this works, the issue is in your Python connection settings
