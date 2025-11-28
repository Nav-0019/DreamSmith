"""
Database Configuration and Session Management

This module sets up the SQLAlchemy database connection and session management.
Uses SQLite for simplicity (can be easily switched to PostgreSQL/MySQL later).
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Database URL: SQLite database file (creates students.db in project root)
DATABASE_URL = "sqlite:///./students.db"

# Create database engine
# connect_args needed for SQLite to allow multiple threads
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

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

