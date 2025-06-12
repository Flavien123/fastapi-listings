# FastAPI Listing Service

This project is a simple web service built with FastAPI for managing property listings. It provides a RESTful API to perform standard CRUD (Create, Read, Update, Delete) operations on listing data, backed by a SQLite database using SQLAlchemy.

## Features

- **Retrieve Listings:** Fetch a list of all listings or a specific listing by its ID.
- **Create Listing:** Add a new listing to the database.
- **Update Listing:** Modify an existing listing using either partial (PATCH) or full (PUT) updates.
- **Delete Listing:** Remove a listing from the database.
- Data validation using Pydantic models.

## Technology Stack

- **Framework:** FastAPI
- **ORM:** SQLAlchemy
- **Database:** SQLite (default configuration)
- **ASGI Server:** Uvicorn
- **Package Management:** `uv`
- **Configuration:** Pydantic Settings
- **Linting/Formatting:** Ruff

## Installation

To set up and run this project locally, follow these steps:

1.  **Prerequisites:** Ensure you have Python 3.13 and the `uv` package manager installed. You can install `uv` by following the instructions on its official website.

2.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Flavien123/fastapi-listings
    cd test-project
    ```

3.  **Create and Activate a Virtual Environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

4.  **Install Dependencies:**
    Install the project dependencies using the `uv.lock` file:
    ```bash
    uv sync
    ```

5.  **Run the Application:**
    Start the FastAPI application using Uvicorn:
    ```bash
    uv run app/main.py
    ```
    The application will run at `http://127.0.0.1:8000` by default.

## API Endpoints

The API is available under the `/api/v1` prefix. Here are the main endpoints for managing listings:

-   `GET /api/v1/listings/`: Get a list of all listings. Supports `skip` and `limit` query parameters for pagination.
-   `GET /api/v1/listings/{listing_id}`: Get a specific listing by its unique ID.
-   `POST /api/v1/listings/`: Create a new listing. Expects a JSON request body conforming to the `ListingCreate` schema.
-   `PATCH /api/v1/listings/{listing_id}`: Partially update an existing listing by ID. Expects a JSON request body with fields to update.
-   `PUT /api/v1/listings/{listing_id}`: Fully update an existing listing by ID. Expects a JSON request body conforming to the `ListingCreate` schema.
-   `DELETE /api/v1/listings/{listing_id}`: Delete a listing by ID.

You can access the automatically generated interactive API documentation (Swagger UI) at `http://127.0.0.1:8000/docs`.

## Project Structure

The main application code resides in the `app/` directory:

```/dev/null/path
test-project/
├── .env
├── .excalidraw.json
├── .gitignore
├── .python-version
├── Dockerfile
├── README.md
├── alembic.ini
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── listings.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── core/
│   │   ├── config.py
│   │   └── __init__.py
│   ├── crud/
│   │   ├── crud.py
│   │   └── __init__.py
│   ├── database/
│   │   ├── base.py
│   │   ├── session.py
│   │   └── __init__.py
│   ├── models/
│   │   ├── listings.py
│   │   └── __init__.py
│   ├── schemas/
│   │   ├── listings.py
│   │   └── __init__.py
│   └── main.py
├── docs/
│   └── README.md
├── pyproject.toml
├── test.py
└── uv.lock
