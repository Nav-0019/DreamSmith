"""
Authentication Routes for Money Seed

This module handles user registration and login endpoints.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from database import get_db
from models import User
from schemas import UserCreate, UserLogin, UserResponse, Token
from auth.hashing import hash_password, verify_password
from auth.jwt_handler import create_access_token, verify_token

# Create router for authentication endpoints
router = APIRouter(
    prefix="/auth",
    tags=["authentication"]  # Groups endpoints in API docs
)

# OAuth2 password flow for token-based authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> User:
    """
    Dependency function to get current authenticated user from JWT token.
    Used to protect routes that require authentication.
    
    Args:
        token: JWT token from request Authorization header
        db: Database session
        
    Returns:
        User: Current authenticated user
        
    Raises:
        HTTPException: If token is invalid or user not found
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    # Verify token and get email
    token_data = verify_token(token, credentials_exception)
    
    # Get user from database
    user = db.query(User).filter(User.email == token_data.email).first()
    if user is None:
        raise credentials_exception
    
    return user


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    """
    Register a new user account.
    
    Endpoint: POST /auth/register
    Body: { "username": "string", "email": "email@example.com", "password": "string" }
    
    Returns:
        UserResponse: Created user data (without password)
        
    Raises:
        HTTPException: If email or username already exists
    """
    # Check if email already exists
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Check if username already exists
    existing_username = db.query(User).filter(User.username == user_data.username).first()
    if existing_username:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already taken"
        )
    
    # Hash password before storing (never store plain passwords!)
    hashed_password = hash_password(user_data.password)
    
    # Create new user
    new_user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hashed_password
    )
    
    # Save to database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user


@router.post("/login", response_model=Token)
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    """
    Login user and return JWT access token.
    
    Endpoint: POST /auth/login
    Body: { "email": "email@example.com", "password": "string" }
    
    Returns:
        Token: JWT access token and token type
        
    Raises:
        HTTPException: If email/password is incorrect
    """
    # Find user by email
    user = db.query(User).filter(User.email == user_data.email).first()
    
    # Verify user exists and password is correct
    if not user or not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create access token with user email in "sub" (subject) field
    access_token = create_access_token(data={"sub": user.email})
    
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=UserResponse)
def get_current_user_info(current_user: User = Depends(get_current_user)):
    """
    Get current authenticated user's information.
    
    Endpoint: GET /auth/me
    Headers: Authorization: Bearer <token>
    
    Returns:
        UserResponse: Current user data
    """
    return current_user
