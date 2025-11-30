"""
JWT Token Handler for Money Seed

This module handles JWT (JSON Web Token) creation and verification.
JWT tokens are used for user authentication.
"""

from datetime import datetime, timedelta
from jose import jwt, JWTError
from schemas import TokenData

# Secret key for signing JWT tokens
# TODO: Change this to use environment variable in production
SECRET_KEY = "SUPER_SECRET_KEY_CHANGE_THIS"
ALGORITHM = "HS256"  # HMAC SHA-256 algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # Token expires after 60 minutes


def create_access_token(data: dict):
    """
    Create a JWT access token with expiration.
    
    Args:
        data: Dictionary containing user data (usually email in "sub" field)
        
    Returns:
        str: Encoded JWT token
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(token: str, credentials_exception):
    """
    Verify and decode a JWT token.
    
    Args:
        token: JWT token string to verify
        credentials_exception: Exception to raise if token is invalid
        
    Returns:
        TokenData: Decoded token data containing user email
        
    Raises:
        credentials_exception: If token is invalid or expired
    """
    try:
        # Decode the token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")  # "sub" (subject) contains user email
        
        if email is None:
            raise credentials_exception
        
        # Return token data
        token_data = TokenData(email=email)
        return token_data
        
    except JWTError:
        raise credentials_exception
