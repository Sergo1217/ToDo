from sqlalchemy.orm import Session

from models.model import TaskDto
from services.UnitOfWork import SQLAlchemyUnitOfWork


def get_tasks(db: Session) -> TaskDto:
    with SQLAlchemyUnitOfWork(db) as uow:
        try:
            tasks = uow.task.get_all()
        except Exception as e:
            print(e)
        else:
            return tasks


def add_task(db: Session, task_data: TaskDto):
    with SQLAlchemyUnitOfWork(db) as uow:
        try:
            task_id = uow.task.add(task_data)
            for subtask_data in task_data.subtasks:
                subtask_data.task_id = task_id
                print(subtask_data)
                uow.subtask.add(subtask_data)
        except Exception as e:
            print(e)
        else:
            uow.commit()


def delete_task(db: Session, task_id: int):
    with SQLAlchemyUnitOfWork(db) as uow:
        try:
            uow.task.delete(task_id)
        except Exception as e:
            print(e)
        else:
            uow.commit()