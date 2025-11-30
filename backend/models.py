"""
Database Models for Money Seed

This module defines all database tables using SQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base


class User(Base):
    """
    User model: Stores student user accounts for Money Seed app
    
    Fields:
        id: Primary key
        username: Unique username
        email: Unique email address (used for login)
        hashed_password: Encrypted password (bcrypt)
        created_at: Account creation timestamp
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
