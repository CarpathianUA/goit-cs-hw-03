import random
from faker import Faker
from sqlalchemy.orm import sessionmaker
from models.users import User
from models.status import Status, StatusName
from models.tasks import Task

from constants.database import USERS_NUM


def seed_db(engine):
    fake = Faker()
    session_factory = sessionmaker(bind=engine)
    session = session_factory()

    with session as session:
        # statuses
        status_values = list(StatusName)
        for status_name in status_values:
            if not session.query(Status).filter(Status.name == status_name).first():
                session.add(Status(name=status_name))
        session.commit()

        # users and tasks
        for _ in range(USERS_NUM):
            user = User(fullname=fake.name(), email=fake.email())
            session.add(user)
        session.commit()

        users = session.query(User).all()
        statuses = session.query(Status.id).all()
        status_ids = [status.id for status in statuses]

        for user in users:
            task = Task(
                title=fake.word(),
                description=fake.sentence(),
                status_id=random.choice(status_ids),
                user_id=user.id,
            )
            session.add(task)
        session.commit()
