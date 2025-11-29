"""
Password Hashing Utilities for Money Seed

This module handles password hashing and verification using bcrypt.
Never store plain text passwords - always hash them!
"""

from passlib.context import CryptContext

# Create password context using bcrypt algorithm
# bcrypt is a secure, slow hashing algorithm perfect for passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    """
    Hash a plain text password using bcrypt.
    
    Args:
        password: Plain text password to hash
        
    Returns:
        str: Hashed password string
    """
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    """
    Verify a plain text password against a hashed password.
    
    Args:
        plain_password: Plain text password to verify
        hashed_password: Hashed password from database
        
    Returns:
        bool: True if passwords match, False otherwise
    """
    return pwd_context.verify(plain_password, hashed_password)
