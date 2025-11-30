"""
Money Seed - FastAPI Backend

Main application file that sets up the FastAPI server and routes.
Student finance guidance app backend.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

# Add CORS middleware to allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (configure more restrictively in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Include authentication router
app.include_router(auth_router)


from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

# Mount frontend static files
# When running with rootDirectory=backend, we need to go up one level to find frontend
# Get the current file's directory (backend/)
current_dir = os.path.dirname(os.path.abspath(__file__))
# Go up one level to project root, then into frontend
frontend_path = os.path.join(os.path.dirname(current_dir), "frontend")

# If frontend doesn't exist at that path, try relative path (for local development)
if not os.path.exists(frontend_path):
    frontend_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")

print(f"Frontend path: {frontend_path}")  # Debug log

@app.get("/healthz")
async def health_check():
    return {"status": "ok"}


# Mount /css, /js, /assets if they exist
if os.path.exists(os.path.join(frontend_path, "css")):
    app.mount("/css", StaticFiles(directory=os.path.join(frontend_path, "css")), name="css")
if os.path.exists(os.path.join(frontend_path, "js")):
    app.mount("/js", StaticFiles(directory=os.path.join(frontend_path, "js")), name="js")
# app.mount("/assets", StaticFiles(directory=os.path.join(frontend_path, "assets")), name="assets") # Uncomment if you have assets

@app.get("/")
async def read_root():
    return FileResponse(os.path.join(frontend_path, "index.html"))

@app.get("/login.html")
async def read_login():
    return FileResponse(os.path.join(frontend_path, "login.html"))

@app.get("/signup.html")
async def read_signup():
    return FileResponse(os.path.join(frontend_path, "signup.html"))

@app.get("/dashboard.html")
async def read_dashboard():
    return FileResponse(os.path.join(frontend_path, "dashboard.html"))
