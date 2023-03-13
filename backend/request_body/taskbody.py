from pydantic import BaseModel

class TaskBody(BaseModel):
    name: str
    description: str
    type: int = 1