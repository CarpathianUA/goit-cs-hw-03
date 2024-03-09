from sqlalchemy import Column, Integer, String, Text, ForeignKey
from models.base import Base
from constants.database import TASKS_TABLE, STATUS_TABLE, USERS_TABLE


class Task(Base):
    __tablename__ = TASKS_TABLE

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100))
    description = Column(Text())
    status_id = Column(Integer, ForeignKey(f"{STATUS_TABLE}.id"))
    user_id = Column(Integer, ForeignKey(f"{USERS_TABLE}.id", ondelete="CASCADE"))

    def __repr__(self):
        return f"<Task(id='{self.id}', title='{self.name}', \
    description='{self.description}', status_id='{self.status_id}', \
    user_id='{self.user_id}')>"
