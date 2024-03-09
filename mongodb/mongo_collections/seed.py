from pymongo import MongoClient
from pymongo.server_api import ServerApi
from faker import Faker
from dotenv import dotenv_values

config = dotenv_values(".env")
client = MongoClient(config["MONGODB_URI"], server_api=ServerApi("1"))
db = client[config["DB_NAME"]]


def seed_collection():
    fake = Faker()
    collection = config["COLLECTION_NAME"]
    print(f"Seeding collection: {collection} with {config['COLLECTION_SIZE']} records")
    for _ in range(int(config["COLLECTION_SIZE"])):
        db[collection].insert_one(
            {
                "name": fake.sentence(nb_words=3).strip("."),
                "author": fake.name(),
                "price": fake.random_int(min=1, max=100),
                "isbn": fake.isbn13(),
                "tags": fake.words(nb=3),
            }
        )

    print(f"Finished seeding collection: {collection}")
