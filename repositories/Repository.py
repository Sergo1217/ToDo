from models.model import TaskDto
from models.orm import SubTask, Task


class TaskRepository:
    def __init__(self, session, model=Task):
        self.session = session
        self.model = model

    def get_all(self):
        tasks = self.session.query(self.model).all()
        return (task for task in tasks)

    def add(self, task_data: TaskDto):
        task = Task(title=task_data.title, description=task_data.description)
        self.session.add(task)
        self.session.flush()
        return task.id

    def delete(self, task_id: int):
        task = self.session.query(self.model).filter(self.model.id==task_id).first()
        self.session.delete(task)


class SubTaskRepository:
    def __init__(self, session, model=Task):
        self.session = session
        self.model = model

    def add(self, subtask_data: TaskDto):
        subtask = SubTask(name=subtask_data.name, description=subtask_data.description, task_id=subtask_data.task_id)
        self.session.add(subtask)

    def delete(self, subtask_id: int):
        task = self.session.query(self.model).filter(self.model.id==subtask_id).first()
        self.session.delete(task)