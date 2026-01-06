# Frontend Usage Guide

## 🎯 What You'll See

Your hotel recommendation frontend is a single-page web application with these main sections:

### 1. Header
- **Title**: "🏨 Hotel Recommendations"
- **Subtitle**: "Africa Cup of Nations - Find the perfect hotel near the stadium"
- **API Status Bar**: Shows connection status and mode (LIVE/MOCK)

### 2. Search Panel (White Card)
Three input fields:
- **🌍 Select Country** - Dropdown with 8 countries
- **💰 Max Price ($)** - Optional price filter
- **📊 Results** - Number of hotels to show (1-20)
- **🔍 Search Hotels** - Purple button to execute search

### 3. Results Section
Grid of hotel cards with:
- **Rank Badge** - #1, #2, #3, etc.
- **Hotel Name** - Large, bold text
- **Price** - Green dollar amount
- **Rating** - Yellow stars (★★★★☆)
- **Distance** - Blue kilometers from stadium
- **Match Score** - Overall score with colored badge

## 📱 Step-by-Step Usage

### Basic Search

1. **Open the frontend**
   - Double-click `frontend/index.html`
   - OR use `launch.bat` for automatic setup

2. **Check API status**
   - Top bar should show: "API Status: healthy | Mode: LIVE | Database: Neo4j connected"
   - If red warning appears, start the API server

3. **Select a country**
   - Click the dropdown
   - Choose one: Egypt, Morocco, Algeria, Senegal, Cameroon, Nigeria, Tunisia, or Ivory Coast

4. **Click "Search Hotels"**
   - Loading spinner appears
   - Results load in ~1 second

5. **View results**
   - Hotels appear in ranked order (#1 = best match)
   - Scroll through the cards
   - Check prices, ratings, distances

### Advanced Filtering

**Limit by Price:**
```
Country: Morocco
Max Price: 120
Results: 5
```
→ Shows only hotels under $120/night in Morocco

**Get More Results:**
```
Country: Egypt
Max Price: [empty]
Results: 10
```
→ Shows top 10 hotels for Egypt (any price)

**Quick Scan:**
```
Country: Senegal
Max Price: [empty]
Results: 3
```
→ Shows just the top 3 best matches

## 🎨 Understanding the Display

### Score Badges

| Badge | Meaning | When |
|-------|---------|------|
| 🟢 **Best Match** | Top recommendation | Rank #1 |
| 🔵 **Great Choice** | Excellent option | Ranks #2-3 |
| 🟠 **Good Option** | Solid choice | Rank #4+ |

### Match Score Explained

The score is calculated as:
```
score = (price × 0.4) + (distance × 0.4) - (rating × 0.2)
```

**Lower score = Better hotel**

Examples:
- **Score 45**: Excellent (cheap, close, highly rated)
- **Score 75**: Good (moderate price/distance, good rating)
- **Score 120**: OK (expensive or far, but might have high rating)

### Hotel Card Layout

```
┌─────────────────────────────────────┐
│  #1                                 │  ← Rank indicator
│  Sheraton Cairo Hotel               │  ← Hotel name
│  ┌─────────────────────────────┐   │
│  │ 💰 Price: $120.00          │   │  ← Price per night
│  │ ⭐ Rating: ★★★★☆ 4.5       │   │  ← Star rating
│  │ 📍 Distance: 2.5 km        │   │  ← Distance from stadium
│  │ 🎯 Score: 52.30 Best Match │   │  ← Overall score + badge
│  └─────────────────────────────┘   │
└─────────────────────────────────────┘
```

## 🖱️ Interactions

### Keyboard Shortcuts
- **Enter** key in any field → Triggers search
- **Tab** → Move between fields
- **Arrow keys** → Navigate dropdown

### Mouse Actions
- **Hover over card** → Card lifts with shadow effect
- **Click dropdown** → Shows country list
- **Scroll** → View all results

### Loading States
- **Searching** → Spinner animation + "Finding the best hotels..."
- **Button disabled** → Prevents duplicate searches
- **Results clear** → Old results removed during new search

## 🔧 Troubleshooting Display Issues

### Problem: Blank page
**Check:**
- Open browser console (F12)
- Look for JavaScript errors
- Verify file path is correct

### Problem: No styling (plain HTML)
**Solution:**
- CSS is embedded in the HTML
- Reload page (Ctrl + F5)
- Try different browser

### Problem: Cards overlap or look weird
**Solution:**
- Zoom out/in (Ctrl + Mouse Wheel)
- Resize browser window
- Try responsive mode (F12 → Device toolbar)

### Problem: Can't click buttons
**Solution:**
- Wait for page to fully load
- Check if JavaScript is enabled
- Disable browser extensions temporarily

## 📊 Example Searches

### 1. Budget Traveler in Egypt
```
Country: Egypt
Max Price: 100
Results: 5
```
**Expected:** Affordable hotels near Cairo stadium

### 2. Premium Stay in Morocco
```
Country: Morocco
Max Price: 200
Results: 3
```
**Expected:** Top 3 luxury hotels in Casablanca

### 3. Exploring All Options in Algeria
```
Country: Algeria
Max Price: [empty]
Results: 10
```
**Expected:** Comprehensive list of all hotels in Algiers

### 4. Quick Decision for Senegal
```
Country: Senegal
Max Price: [empty]
Results: 1
```
**Expected:** Single best hotel recommendation in Dakar

## 🎯 Best Practices

### For Best Results:
1. ✅ Start with default settings (no price limit, 5 results)
2. ✅ Review all details on the top-ranked hotel
3. ✅ Compare top 3 options before deciding
4. ✅ Consider your priorities (price vs. distance vs. quality)

### Performance Tips:
1. ⚡ Keep results limit under 10 for faster loading
2. ⚡ Use price filter to narrow options
3. ⚡ Refresh page if it feels slow

### Mobile Usage:
1. 📱 Works perfectly on phones and tablets
2. 📱 Cards stack vertically on small screens
3. 📱 Touch-friendly buttons and dropdowns

## 🔄 Workflow Examples

### Scenario 1: Planning a Trip
1. Open frontend
2. Search Egypt (no filters)
3. Note top 3 hotels with prices
4. Search Morocco
5. Compare Egypt vs Morocco options
6. Make decision based on total cost

### Scenario 2: Budget Constrained
1. Search country of interest
2. Set max price to your budget
3. Review available options
4. If no results, increase price by $20
5. Repeat until you find options

### Scenario 3: Last-Minute Booking
1. Search with default settings
2. Look at #1 ranked hotel
3. Check if price/distance acceptable
4. Book immediately if it meets needs

## 🎨 Visual Design Elements

### Color Scheme:
- **Purple gradient** - Headers, buttons
- **Green** - Prices
- **Blue** - Distances
- **Yellow** - Star ratings
- **White cards** - Clean, modern look

### Typography:
- **Large, bold** hotel names
- **Clear numbers** for prices and ratings
- **Easy-to-read** body text

### Spacing:
- **Generous padding** around elements
- **Cards with gaps** for easy distinction
- **Responsive grid** adjusts to screen size

## 💡 Tips & Tricks

1. **Compare countries** - Open in multiple tabs to compare
2. **Share results** - Copy URL and share with friends (after implementing URL params)
3. **Print-friendly** - Use browser print function for reference
4. **Save favorites** - Screenshot your top picks
5. **Night mode** - Use browser dark mode extensions

## 🚀 What's Next?

Ideas for future enhancements:
- Add hotel images
- Show location on map
- Add booking links
- Save favorites to local storage
- Share results via social media
- Add currency converter
- Show amenities (WiFi, pool, etc.)
- Add user reviews
- Compare hotels side-by-side
- Dark mode toggle

---

**Enjoy finding the perfect hotel for your Africa Cup of Nations trip! ⚽🏨**
