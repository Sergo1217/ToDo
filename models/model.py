from dataclasses import dataclass

from pydantic import BaseModel


@dataclass
class SubTaskDto(BaseModel):
    name: str
    description: str
    task_id: int

@dataclass
class TaskDto(BaseModel):
    title: str
    description: str
    subtasks: list[SubTaskDto]
