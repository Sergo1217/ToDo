from __future__ import annotations

import sqlite3

from models.model import SubTaskDto, TaskDto
from repositories.Repository import SubTaskRepository, TaskRepository


class LiteUnitOfWork:
    def __init__(self):
        self.conn = sqlite3.connect("database/db.sqlite")

    def __enter__(self):
        self.task = TaskRepository(self.conn)
        self.subtask = SubTaskRepository(self.conn)
        self._tasks_to_add = []
        self._tasks_to_del = []
        self._subtasks_to_add = []
        self._subtasks_to_del = []
        return self

    def get_all(self):
        try:
            tasks = self.task.get_all()
            for task in tasks:
                subtasks = self.subtask.get_all(task.id)
                task.subtasks = subtasks
        except Exception as e:
            print(e)
            return []
        else:
            return tasks

    def reg_task_to_add(self, task_data: TaskDto):
        self._tasks_to_add.append(task_data)

    def reg_task_to_del(self, task_id: int):
        self._tasks_to_del.append(task_id)

    def reg_subtask_to_add(self, subtask_data: SubTaskDto):
        pass

    def reg_subtask_to_del(self, task_id: int):
        self._subtasks_to_del.append(task_id)

    def __exit__(self, *args):
        self.rollback()

    def _add_tasks(self):
        for task in self._tasks_to_add:
            task_id = self.task.add(task)
            for subtask_data in task.subtasks:
                subtask_data.task_id = task_id
                self._subtasks_to_add.append(subtask_data)

    def _del_tasks(self):
        for task_id in self._tasks_to_del:
            self.task.delete(task_id)


    def _add_subtasks(self):
        for subtask in self._subtasks_to_add:
            self.subtask.add(subtask)



    def _del_subtasks(self):
        for task_id in self._subtasks_to_del:
            self.subtask.delete(task_id)


    def commit(self):
        try:
            self._add_tasks()
            self._del_tasks()
            self._add_subtasks()
            self._del_subtasks()
        except Exception as e:
            print(e)
            self.rollback()
        else:
            self.conn.commit()

    def rollback(self):
        self.conn.rollback()
