from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.todo import Todo, TodoCreate, TodoUpdate
from app.services.todo import create_todo, get_todos, get_todo, update_todo, delete_todo
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=Todo)
def create_todo_item(todo: TodoCreate, db: Session = Depends(get_db)):
    return create_todo(db=db, todo=todo)

@router.get("/", response_model=List[Todo])
def read_todos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_todos(db, skip=skip, limit=limit)

@router.get("/{todo_id}", response_model=Todo)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = get_todo(db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

@router.put("/{todo_id}", response_model=Todo)
def update_todo_item(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    return update_todo(db=db, todo_id=todo_id, todo=todo)

@router.delete("/{todo_id}", response_model=Todo)
def delete_todo_item(todo_id: int, db: Session = Depends(get_db)):
    return delete_todo(db=db, todo_id=todo_id)
