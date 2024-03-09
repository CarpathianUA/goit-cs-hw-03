import mongo_collections.utils as utils
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from pymongo.server_api import ServerApi
from dotenv import dotenv_values
from argparse import ArgumentParser

from mongo_collections.seed import seed_collection
from constants.commands import COMMANDS

config = dotenv_values(".env")
client = MongoClient(
    config["MONGODB_URI"],
    server_api=ServerApi("1"),
    serverSelectionTimeoutMS=5000,  # 5 seconds
    socketTimeoutMS=5000,
)

parser = ArgumentParser(description="MongoDB CLI")
parser.add_argument(
    "--command",
    "-c",
    help="Available commands: " + ", ".join(COMMANDS),
)
parser.add_argument("--name", "-n", help="Name of the record to operate on")
parser.add_argument(
    "--price", "-p", help="Price of the record to operate on", type=float
)
parser.add_argument("--tag", "-t", help="Tag of the record to operate on")
parser.add_argument("--author", "-a", help="Author of the record to operate on")
parser.add_argument("--isbn", "-i", help="ISBN of the record to operate on")
parser.add_argument("--seed", "-s", action="store_true")


args = parser.parse_args()
command = args.command
name = args.name
price = args.price
tag = args.tag
author = args.author
isbn = args.isbn


if __name__ == "__main__":
    try:
        print("Connecting to MongoDB...")
        response = client.admin.command("ping")
        print("Connected:", response)
    except ServerSelectionTimeoutError as e:
        print("Failed to connect:", e)

    try:
        db = client[config["DB_NAME"]]
        collection = config["COLLECTION_NAME"]
        if collection not in db.list_collection_names():
            db.create_collection(collection, check_exists=True)

        if args.seed:
            seed_collection()

        if command == "find_all":
            utils.find_all_records(db[collection])
        elif command == "find_by_name":
            utils.find_record_by_name(db[collection], name)
        elif command == "delete_by_name":
            utils.delete_record_by_name(db[collection], name)
        elif command == "delete_all":
            utils.delete_all_records(db[collection])
        elif command == "add_record":
            utils.add_new_record(db[collection], name, author, price, isbn, tag)
        elif command == "update_record_price":
            utils.update_record_price(db[collection], name, price)
        elif command == "add_tag":
            utils.add_new_tag_to_record(db[collection], name, tag)
    except Exception as e:
        print(f"Error: {e}")

    client.close()
