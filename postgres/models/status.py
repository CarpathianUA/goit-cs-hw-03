import enum
from sqlalchemy import Column, Integer
from sqlalchemy.types import Enum
from models.base import Base
from constants.database import STATUS_TABLE


class StatusName(enum.Enum):
    NEW = "new"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


class Status(Base):
    __tablename__ = STATUS_TABLE

    id = Column(Integer, primary_key=True, autoincrement=True)
    # custom ENUM-based type, allow only specified values from StatusName class
    name = Column(Enum(StatusName), unique=True)

    def __repr__(self):
        return f"<Status(id='{self.id}', name='{self.name}')>"
