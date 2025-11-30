# Money Seed Backend

This is the backend for the Money Seed application, built with Python and FastAPI.

## Prerequisites

- Python 3.8+
- pip (Python package installer)

## Setup

1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    - Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Server

To start the development server with hot-reloading:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.
API documentation is available at `http://localhost:8000/docs`.
