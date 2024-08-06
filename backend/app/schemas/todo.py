from pydantic import BaseModel

class TodoLLMBase(BaseModel):
    title: str
    description: str
    completed: bool = False
    llmNote: str = 'CLick to generate from LLM'

class TodoCreate(TodoLLMBase):
    pass

class TodoUpdate(TodoLLMBase):
    pass

class TodoInDBBase(TodoLLMBase):
    id: int

    class Config:
        from_attributes = True

class Todo(TodoInDBBase):
    pass
