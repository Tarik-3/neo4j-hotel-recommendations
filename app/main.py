from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import HotelResponse
from typing import List, Optional
import os

# Try to import the real service, fall back to mock if Neo4j is not available
USE_MOCK = os.getenv("USE_MOCK", "false").lower() == "true"

if USE_MOCK:
    from app.services_mock import get_best_hotels_mock as get_best_hotels
    print("⚠️  Running in MOCK mode - using sample data instead of Neo4j")
else:
    try:
        from app.services import get_best_hotels
        print("✓ Connected to Neo4j database")
    except Exception as e:
        print(f"⚠️  Could not connect to Neo4j: {e}")
        print("⚠️  Falling back to MOCK mode - using sample data")
        from app.services_mock import get_best_hotels_mock as get_best_hotels
        USE_MOCK = True

app = FastAPI(
    title="Hotel Recommendation API - CAN Edition",
    description="Find the best hotels near stadiums where your national team will play during the Africa Cup of Nations",
    version="1.0.0"
)

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Root"])
def root():
    """Root endpoint with API information"""
    return {
        "message": "Hotel Recommendation API for Africa Cup of Nations (CAN)",
        "mode": "MOCK" if USE_MOCK else "LIVE",
        "docs": "/docs",
        "endpoints": {
            "best_hotels": "/best-hotels?country=Egypt&max_price=150&limit=5"
        },
        "available_countries": ["Egypt", "Morocco", "Algeria", "Senegal", "Cameroon", "Nigeria", "Tunisia", "Ivory Coast"] if not USE_MOCK else ["Egypt", "Morocco", "Algeria", "Senegal"]
    }

@app.get("/best-hotels", response_model=List[HotelResponse], tags=["Hotels"])
def best_hotels(
    country: str = Query(..., description="Name of the country (e.g., Egypt, Morocco)"),
    max_price: Optional[float] = Query(None, description="Maximum price per night (optional)"),
    limit: int = Query(5, ge=1, le=20, description="Number of hotels to return")
):
    """
    Get the best hotel recommendations for a specific country.
    
    The hotels are ranked based on:
    - **Price** (40% weight): Lower is better
    - **Distance** (40% weight): Closer to stadium is better
    - **Rating** (20% weight): Higher is better
    
    Returns hotels sorted by score (lower score = better match).
    """
    try:
        results = get_best_hotels(country, max_price, limit)
        
        if not results:
            raise HTTPException(
                status_code=404,
                detail=f"No hotels found for country '{country}'. Available countries: Egypt, Morocco, Algeria, Senegal, Cameroon, Nigeria, Tunisia, Ivory Coast"
            )
        
        return results
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error retrieving hotels: {str(e)}"
        )

@app.get("/health", tags=["System"])
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "mode": "MOCK" if USE_MOCK else "LIVE",
        "database": "Mock data" if USE_MOCK else "Neo4j connected"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
