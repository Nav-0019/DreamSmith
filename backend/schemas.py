"""
Pydantic Schemas for Money Seed

This module defines request/response schemas using Pydantic.
These schemas validate data and provide automatic API documentation.
"""

from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


# ============================================
# User Schemas
# ============================================

class UserCreate(BaseModel):
    """Schema for user registration - requires username, email, and password"""
    username: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    """Schema for user login - requires email and password"""
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    """Schema for user response - excludes password for security"""
    id: int
    username: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True  # Allows conversion from SQLAlchemy models (Pydantic V2)


# ============================================
# Authentication Schemas
# ============================================

class Token(BaseModel):
    """Schema for JWT token response"""
    access_token: str
    token_type: str


class TokenData(BaseModel):
    """Schema for token payload data"""
    email: Optional[str] = None
