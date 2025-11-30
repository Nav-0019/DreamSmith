"""
Database Configuration and Session Management

This module sets up the SQLAlchemy database connection and session management.
Uses SQLite for simplicity (can be easily switched to PostgreSQL/MySQL later).
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

import os

# Database URL: Read from env variable or default to SQLite
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./students.db")

# Handle Render's Postgres URL format (starts with postgres:// but SQLAlchemy needs postgresql://)
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Create database engine
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        DATABASE_URL, connect_args={"check_same_thread": False}
    )
else:
    engine = create_engine(DATABASE_URL)

# Create SessionLocal class for database sessions
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base class for database models
Base = declarative_base()


def get_db():
    """
    Dependency function to get database session.
    Used with FastAPI's Depends() to manage database connections.
    
    Yields:
        Session: Database session object
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

