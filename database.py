from sqlmodel import SQLModel, Field, create_engine, Session
from fastapi import Depends
from typing import Annotated
from datetime import datetime

# Database models
class Todo(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str = Field(index=True, max_length=100)
    description: str = Field(max_length=500)
    completed: bool = False
    created_at: datetime = Field(default_factory=datetime.now)

class CreateTodo(SQLModel):
    title: str = Field(index=True, max_length=100)
    description: str = Field(max_length=500)
    completed: bool = False

class UpdateTodo(SQLModel):
    title: str | None = Field(default=None, index=True, max_length=100)
    description: str | None = Field(default=None, max_length=500)
    completed: bool = Field(default=False)

class ReadTodo(SQLModel):
    id: int = Field(primary_key=True)
    title: str = Field(index=True, max_length=100)
    description: str = Field(max_length=500)
    completed: bool = False
    created_at: datetime = Field(default_factory=datetime.now)

# Database connection
sqlite_file_name = "todo.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

# Create the database
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Create a dependency for the database session
def get_session():
    with Session(engine) as session:
        yield session

SessionDependency = Annotated[Session, Depends(get_session)]
