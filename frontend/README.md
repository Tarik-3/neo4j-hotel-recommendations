# Hotel Recommendation Frontend

A beautiful, responsive web interface for finding the best hotels near stadiums during the Africa Cup of Nations.

## Features

✨ **User-Friendly Interface**
- Clean, modern design with gradient backgrounds
- Responsive layout that works on all devices
- Smooth animations and hover effects

🔍 **Smart Search**
- Country selection dropdown
- Optional price filtering
- Adjustable number of results (1-20 hotels)
- Real-time API status indicator

📊 **Hotel Information Display**
- **Hotel Name** - Clear identification
- **Price** - Cost per night in USD
- **Rating** - Star rating (1-5 stars)
- **Distance** - How far from the stadium (in km)
- **Match Score** - Overall recommendation score (lower is better)
- **Ranking Badge** - "Best Match", "Great Choice", or "Good Option"

## Quick Start

### 1. Start the API Server

Open a terminal in the project root directory and run:

```bash
# Option 1: Using the batch file (Windows)
start_server.bat

# Option 2: Manual start
uvicorn app.main:app --port 8000
```

The API will start at http://127.0.0.1:8000

### 2. Open the Frontend

Simply open the `frontend/index.html` file in your web browser:

```bash
# Option 1: Double-click the file in File Explorer

# Option 2: From terminal
start frontend\index.html

# Option 3: From VS Code - right-click and "Open with Live Server" or "Open in Browser"
```

### 3. Use the Application

1. **Select a country** from the dropdown menu
2. **Set max price** (optional) - leave empty for no limit
3. **Choose number of results** - default is 5
4. **Click "Search Hotels"** button
5. **View results** - hotels are displayed sorted by best match

## How It Works

### Scoring System

Hotels are ranked based on a weighted scoring formula:
- **40%** - Price (lower is better)
- **40%** - Distance from stadium (closer is better)
- **20%** - Rating (higher is better)

The hotel with the **lowest score** is the best recommendation!

### API Connection

The frontend connects to your FastAPI backend at `http://127.0.0.1:8000`. The API can run in two modes:

- **LIVE Mode**: Uses real data from Neo4j database
- **MOCK Mode**: Uses sample data (if Neo4j is unavailable)

The current mode is displayed in the API status bar at the top.

## Available Countries

- 🇪🇬 Egypt
- 🇲🇦 Morocco
- 🇩🇿 Algeria
- 🇸🇳 Senegal
- 🇨🇲 Cameroon
- 🇳🇬 Nigeria
- 🇹🇳 Tunisia
- 🇨🇮 Ivory Coast

*Note: Mock mode only includes Egypt, Morocco, Algeria, and Senegal*

## Troubleshooting

### Problem: "API is not running" message

**Solution:**
1. Make sure the API server is running: `uvicorn app.main:app --port 8000`
2. Check that port 8000 is not being used by another application
3. Verify the API is accessible at http://127.0.0.1:8000/health

### Problem: CORS errors in browser console

**Solution:**
The API has been configured with CORS middleware to allow frontend access. If you still see CORS errors:
1. Make sure you're using the updated `app/main.py` with CORS middleware
2. Restart the API server
3. Clear your browser cache

### Problem: "No hotels found" result

**Solution:**
1. Try a different country
2. Remove or increase the max price filter
3. If using LIVE mode, verify your database has data: `python populate_db.py`
4. Try running in MOCK mode: `set USE_MOCK=true` before starting the server

### Problem: Frontend doesn't update after changing API

**Solution:**
1. Hard refresh the browser (Ctrl + F5)
2. Clear browser cache
3. Check browser console (F12) for JavaScript errors

## Customization

### Change API URL

If your API is running on a different port or host, edit `index.html`:

```javascript
const API_BASE_URL = 'http://127.0.0.1:8000';  // Change this line
```

### Modify Styling

All styles are in the `<style>` section of `index.html`. Key customization options:

- **Colors**: Search for gradient definitions and color codes
- **Card Layout**: Modify `.hotels-grid` grid-template-columns
- **Font**: Change the `font-family` in the `body` selector

### Add More Countries

1. Update the API to support the new country in the database
2. Add a new `<option>` in the country dropdown in `index.html`

## File Structure

```
frontend/
└── index.html          # Single-page application (HTML + CSS + JavaScript)
```

## Technologies Used

- **HTML5** - Structure
- **CSS3** - Styling with gradients, flexbox, and grid
- **JavaScript (Vanilla)** - API communication and dynamic content
- **Fetch API** - HTTP requests to backend

## Browser Compatibility

✅ Chrome (recommended)
✅ Firefox
✅ Edge
✅ Safari
✅ Opera

## Next Steps

### Enhancements You Could Add

1. **Map Integration** - Show hotel locations on a map
2. **Image Gallery** - Add hotel photos
3. **Booking Links** - Link to booking platforms
4. **Comparison Mode** - Compare multiple hotels side-by-side
5. **User Reviews** - Display guest reviews
6. **Filters** - Add amenity filters (WiFi, pool, parking, etc.)
7. **Sorting Options** - Sort by price, distance, or rating
8. **Favorites** - Save favorite hotels to local storage
9. **Dark Mode** - Toggle between light and dark themes
10. **Multi-language** - Add language selection

## Support

For issues or questions:
1. Check the main project README.md
2. Review NEO4J_SETUP_GUIDE.md for database issues
3. Test the API directly at http://127.0.0.1:8000/docs

## License

This is part of the Hotel Recommendation API - CAN Edition project.
