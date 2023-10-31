from models.model import TaskDto
from services.UnitOfWork import LiteUnitOfWork


def get_tasks() -> TaskDto:
    with LiteUnitOfWork() as uow:
        return uow.get_all()


def add_task(task_data: TaskDto):
    with LiteUnitOfWork() as uow:
        uow.reg_task_to_add(task_data)
        for subtaks in task_data.subtasks:
            uow.reg_subtask_to_add(subtaks)
        uow.commit()


def delete_task(task_id: int):
    with LiteUnitOfWork() as uow:
        uow.reg_task_to_del(task_id)
        uow.reg_subtask_to_del(task_id)
        uow.commit()
