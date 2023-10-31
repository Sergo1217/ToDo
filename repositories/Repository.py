import sqlite3

from models.model import SubTaskDto, TaskDto


class TaskRepository:
    def __init__(self, conn: sqlite3.Connection):
        self.session = conn
        self.cursor = self.session.cursor()

    def get_all(self):
        tasks = []
        for row in self.session.execute("SELECT id, title, description FROM tasks").fetchall():
            task = TaskDto(id=row[0], title=row[1], description=row[2], subtasks=[])
            tasks.append(task)
        return tasks

    def add(self, task_data: TaskDto):
        return self.session.execute("INSERT INTO tasks (title, description) VALUES (?, ?)", (task_data.title, task_data.description)).lastrowid

    def delete(self, task_id: int):
        self.session.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.session.commit()


class SubTaskRepository:
    def __init__(self, conn: sqlite3.Connection):
        self.session = conn
        self.cursor = self.session.cursor()

    def get_all(self, task_id: int):
        subtasks = []
        for row in self.session.execute("SELECT id, name, description, task_id FROM subtasks WHERE task_id = ?", (task_id,)).fetchall():
            subtask = SubTaskDto(id=row[0], name=row[1], description=row[2], task_id=row[3])
            subtasks.append(subtask)
        return subtasks

    def add(self, subtask_data: SubTaskDto):
        self.session.execute("INSERT INTO subtasks (name, description, task_id) VALUES (?, ?, ?)", (subtask_data.name, subtask_data.description, subtask_data.task_id))
        self.session.commit()

    def delete(self, task_id: int):
        self.session.execute("DELETE FROM subtasks WHERE task_id = ?", (task_id,))
        self.session.commit()