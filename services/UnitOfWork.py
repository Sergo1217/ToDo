from __future__ import annotations

from sqlalchemy.orm import Session

from repositories.Repository import SubTaskRepository, TaskRepository


class SQLAlchemyUnitOfWork:
    def __init__(self, session: Session):
        self.session = session

    def __enter__(self):
        self.task = TaskRepository(self.session)
        self.subtask = SubTaskRepository(self.session)
        return self

    def __exit__(self, *args):
        self.rollback()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
