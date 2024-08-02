from sqlalchemy import Column, Integer, String, Boolean
from app.db.base import Base

# for SQLAlchemy Table
class Todo(Base):
    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    completed = Column(Boolean, default=False)
