from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.todos import router as todos_router
from database import create_db_and_tables
description = """
Todo API is a simple API for managing a list of tasks.

Endpoints:
- POST /todos: Create a new Task.
- GET /todos: Retrieve all Taaks.
- GET /todo/{id}: Retrieve a specific Task.
- PUT /todos/{id}: Update a specific Task.
- DELETE /todos/{id}: Delete a specific Task.
"""

app = FastAPI(title="Todo API", description=description, version="1.0.0")
app.include_router(todos_router)

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    create_db_and_tables()
