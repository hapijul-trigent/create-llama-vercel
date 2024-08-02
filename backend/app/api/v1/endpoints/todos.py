from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.todo import crud_todo
from app.schemas.todo import Todo, TodoCreate, TodoUpdate
from app.db.session import get_session

router = APIRouter()

@router.post("/", response_model=Todo)
async def create_todo(
    *, db: AsyncSession = Depends(get_session), todo_in: TodoCreate
):
    todo = await crud_todo.create(db=db, obj_in=todo_in)
    return todo

@router.get("/{id}", response_model=Todo)
async def read_todo(
    *, db: AsyncSession = Depends(get_session), id: int
):
    todo = await crud_todo.get(db=db, id=id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.put("/{id}", response_model=Todo)
async def update_todo(
    *, db: AsyncSession = Depends(get_session), id: int, todo_in: TodoUpdate
):
    todo = await crud_todo.get(db=db, id=id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo = await crud_todo.update(db=db, db_obj=todo, obj_in=todo_in)
    return todo

@router.delete("/{id}", response_model=Todo)
async def delete_todo(
    *, db: AsyncSession = Depends(get_session), id: int
):
    todo = await crud_todo.get(db=db, id=id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo = await crud_todo.remove(db=db, id=id)
    return todo
