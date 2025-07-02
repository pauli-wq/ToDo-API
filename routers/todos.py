from fastapi import APIRouter, HTTPException, Query
from typing import Annotated, List
from sqlmodel import select
from database import CreateTodo, ReadTodo, UpdateTodo, Todo, SessionDependency

router = APIRouter()

# To create a Task
@router.post("/todos/", response_model=CreateTodo, tags=["Create Tasks"])
async def create_todo(todo: CreateTodo, session: SessionDependency):
    db_todo = Todo(**todo.model_dump())
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo

# To read all Tasks
@router.get("/todos/", response_model=List[ReadTodo], tags=["Read all Tasks"])
async def read_todos(
    session: SessionDependency,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100
):
    todos = session.exec(select(Todo).offset(offset).limit(limit)).all()
    return todos

# To read a Task
@router.get("/todo/{todo_id}", response_model=ReadTodo, tags=["Read a Task"])
async def read_todo(todo_id: int, session: SessionDependency):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Task not found")
    return todo

# To update a Task
@router.patch("/todo/{todo_id}", response_model=UpdateTodo, tags=["Update a Task"])
async def update_todo(todo_id: int, todo: UpdateTodo, session: SessionDependency):
    db_todo = session.get(Todo, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Task not found")
    todo_data = todo.model_dump(exclude_unset=True)
    db_todo.sqlmodel_update(todo_data)
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo

# To delete a Task
@router.delete("/todo/{todo_id}", response_model=ReadTodo, tags=["Delete a Task"])
async def delete_todo(todo_id: int, session: SessionDependency):
    db_todo = session.get(Todo, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Task not found")
    session.delete(db_todo)
    session.commit()
    return db_todo
