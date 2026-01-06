from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import HotelResponse
from typing import List, Optional

# Always use live Neo4j-backed services
try:
    from app.services import get_best_hotels
    print("✓ Using Neo4j live data")
except Exception as e:
    # Fail hard rather than switching to mock mode
    raise RuntimeError(f"Failed to initialize Neo4j services: {e}")

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
        "mode": "LIVE",
        "docs": "/docs",
        "endpoints": {
            "best_hotels": "/best-hotels?country=Egypt&max_price=150&limit=5"
        },
        "available_countries": ["Egypt", "Morocco", "Algeria", "Senegal", "Cameroon", "Nigeria", "Tunisia", "Ivory Coast"]
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
        "mode": "LIVE",
        "database": "Neo4j connected"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
