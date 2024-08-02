from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoUpdate

class CRUDTodo:
    async def create(self, db: AsyncSession, *, obj_in: TodoCreate) -> Todo:
        db_obj = Todo(
            title=obj_in.title,
            description=obj_in.description,
            completed=obj_in.completed,
        )
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def get(self, db: AsyncSession, id: int) -> Todo:
        result = await db.execute(select(Todo).filter(Todo.id == id))
        return result.scalars().first()

    async def update(
        self, db: AsyncSession, *, db_obj: Todo, obj_in: TodoUpdate
    ) -> Todo:
        obj_data = obj_in.model_dump(exclude_unset=True)
        for field in obj_data:
            setattr(db_obj, field, obj_data[field])
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def remove(self, db: AsyncSession, *, id: int) -> Todo:
        result = await db.execute(select(Todo).filter(Todo.id == id))
        obj = result.scalars().first()
        await db.delete(obj)
        await db.commit()
        return obj

crud_todo = CRUDTodo()
