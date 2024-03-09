from sqlalchemy import Column, Integer, String
from models.base import Base
from constants.database import USERS_TABLE


class User(Base):
    __tablename__ = USERS_TABLE

    id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(String(100))
    email = Column(String(100), unique=True)

    def __repr__(self):
        return (
            f"<User(id='{self.id}', fullname='{self.fullname}', email='{self.email}')>"
        )
