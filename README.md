# Money Seed - Backend API

FastAPI backend for Money Seed - Student Finance Guidance App.

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Run the Server

```bash
# Development mode (with auto-reload)
uvicorn main:app --reload

# Production mode
uvicorn main:app --host 0.0.0.0 --port 8000
```

The API will be available at:
- **API**: http://localhost:8000
- **Interactive Docs (Swagger)**: http://localhost:8000/docs
- **Alternative Docs (ReDoc)**: http://localhost:8000/redoc

## 📁 Project Structure

```
backend/
├── main.py              # FastAPI application entry point
├── database.py          # Database connection and session management
├── models.py            # SQLAlchemy database models
├── schemas.py           # Pydantic request/response schemas
├── requirements.txt     # Python dependencies
└── auth/
    ├── __init__.py
    ├── hashing.py       # Password hashing utilities (bcrypt)
    ├── jwt_handler.py   # JWT token creation/verification
    └── routers.py       # Authentication routes
```

## 🔐 Authentication Endpoints

### Register User

**POST** `/auth/register`

Register a new user account.

**Request Body:**
```json
{
  "username": "student123",
  "email": "student@example.com",
  "password": "securepassword"
}
```

**Response:** `201 Created`
```json
{
  "id": 1,
  "username": "student123",
  "email": "student@example.com",
  "created_at": "2025-11-28T10:00:00Z"
}
```

### Login

**POST** `/auth/login`

Login user and get JWT access token.

**Request Body:**
```json
{
  "email": "student@example.com",
  "password": "securepassword"
}
```

**Response:** `200 OK`
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "bearer"
}
```

### Get Current User

**GET** `/auth/me`

Get current authenticated user's information.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response:** `200 OK`
```json
{
  "id": 1,
  "username": "student123",
  "email": "student@example.com",
  "created_at": "2025-11-28T10:00:00Z"
}
```

## 🗄️ Database

- **Database**: SQLite
- **File**: `students.db` (created automatically)
- **ORM**: SQLAlchemy

### User Model

The `User` table contains:
- `id` (Integer, Primary Key)
- `username` (String, Unique)
- `email` (String, Unique)
- `hashed_password` (String, bcrypt hashed)
- `created_at` (DateTime, Auto-generated)

## 🔧 Configuration

### JWT Settings

Token expiration and secret key are configured in `auth/jwt_handler.py`:
- `SECRET_KEY`: Change this in production!
- `ACCESS_TOKEN_EXPIRE_MINUTES`: 60 minutes (default)

### Database

Database URL is configured in `database.py`:
- Default: `sqlite:///./students.db`
- Can be changed to PostgreSQL/MySQL for production

## 📝 API Documentation

FastAPI automatically generates interactive API documentation:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🛠️ Development

### Testing the API

1. **Start the server:**
   ```bash
   uvicorn main:app --reload
   ```

2. **Open Swagger UI:**
   - Navigate to http://localhost:8000/docs
   - Try the endpoints directly from the browser

3. **Test Registration:**
   ```bash
   curl -X POST "http://localhost:8000/auth/register" \
     -H "Content-Type: application/json" \
     -d '{"username":"testuser","email":"test@example.com","password":"test123"}'
   ```

4. **Test Login:**
   ```bash
   curl -X POST "http://localhost:8000/auth/login" \
     -H "Content-Type: application/json" \
     -d '{"email":"test@example.com","password":"test123"}'
   ```

## 🔒 Security Features

- ✅ Passwords are hashed with bcrypt (never stored in plain text)
- ✅ JWT tokens for stateless authentication
- ✅ Token expiration (60 minutes)
- ✅ Email validation with Pydantic
- ✅ Unique constraints on username and email

## 📚 Code Structure

- **Clean separation of concerns**: Models, schemas, routes, and utilities are separated
- **Well-commented**: All code includes helpful comments
- **Type hints**: Python type hints for better code clarity
- **Pydantic validation**: Automatic request/response validation

## 🚨 Important Notes

1. **Change SECRET_KEY**: Update `SECRET_KEY` in `auth/jwt_handler.py` before production
2. **Database migrations**: Use Alembic for production database migrations
3. **CORS**: Add CORS middleware if connecting to a frontend
4. **Environment variables**: Use `.env` file for sensitive configuration

## 📦 Dependencies

- `fastapi` - Web framework
- `uvicorn` - ASGI server
- `sqlalchemy` - Database ORM
- `pydantic` - Data validation
- `passlib[bcrypt]` - Password hashing
- `python-jose[cryptography]` - JWT tokens

## 🎯 Next Steps

1. Add more endpoints (budgets, savings goals, transactions)
2. Add database migrations with Alembic
3. Add unit tests
4. Add CORS middleware for frontend integration
5. Deploy to production server
