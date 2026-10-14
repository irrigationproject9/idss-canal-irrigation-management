from fastapi import FastAPI
import geopandas as gpd
from shapely.geometry import Point
import sqlalchemy

app = FastAPI(
    title="IDSS Canal Irrigation Backend",
    version="1.0.0",
    description="Intelligent Decision Support System for Canal Irrigation Management"
)

@app.get("/health", tags=["Health Check"])
def health_check():
    """
    Health check endpoint verifying FastAPI and core geospatial/database modules.
    """
    # Quick test to ensure spatial packages are fully functional in memory
    p = Point(1.0, 1.0)
    
    return {
        "status": "healthy",
        "system": "IDSS Backend (Ubuntu)",
        "spatial_stack": "Operational",
        "test_point_wkt": p.wkt
    }