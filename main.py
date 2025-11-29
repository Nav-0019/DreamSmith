"""
Money Seed - FastAPI Backend

Main application file that sets up the FastAPI server and routes.
Student finance guidance app backend.
"""

from fastapi import FastAPI
from database import Base, engine
from auth.routers import router as auth_router

# Create database tables on startup
# In production, use Alembic for migrations instead
Base.metadata.create_all(bind=engine)

# Create FastAPI application instance
app = FastAPI(
    title="Money Seed API",
    description="Backend API for Money Seed - Student Finance Guidance App",
    version="1.0.0"
)

# Include authentication router
app.include_router(auth_router)


@app.get("/")
def root():
    """
    Root endpoint - API health check.
    
    Returns:
        dict: Welcome message
    """
    return {"message": "Money Seed API is running!"}
