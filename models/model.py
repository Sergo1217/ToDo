from dataclasses import dataclass

from pydantic import BaseModel


@dataclass
class SubTaskDto(BaseModel):
    id: int = 0
    name: str
    description: str
    task_id: int = 0

    def __init__(self, name: str, description: str, task_id: int = 0, id: int = 0) -> BaseModel:
         super().__init__(id=id, name=name, description=description, task_id=task_id)

@dataclass
class TaskDto(BaseModel):
    id: int = 0
    title: str
    description: str
    subtasks: list[SubTaskDto]

    def __init__(self, title: str, description: str, subtasks: list[SubTaskDto], id: int = 0) -> BaseModel:
         super().__init__(id=id, title=title, description=description, subtasks=subtasks)
