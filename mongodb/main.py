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

        db = client[config["DB_NAME"]]
        collection_name = config["COLLECTION_NAME"]
        if collection_name not in db.list_collection_names():
            db.create_collection(collection_name, check_exists=True)
        collection = db[collection_name]

        if args.seed:
            seed_collection()

        if command:
            if command not in COMMANDS:
                raise ValueError(f"Invalid command: {command}")

            if command == "find_all":
                utils.find_all_records(collection)
            elif command == "find_by_name":
                utils.find_record_by_name(collection, name)
            elif command == "delete_by_name":
                utils.delete_record_by_name(collection, name)
            elif command == "delete_all":
                utils.delete_all_records(collection)
            elif command == "add_record":
                utils.add_new_record(collection, name, author, price, isbn, tag)
            elif command == "update_record_price":
                utils.update_record_price(collection, name, price)
            elif command == "add_tag":
                utils.add_new_tag_to_record(collection, name, tag)
        elif not args.seed:
            # If no command is provided and --seed is not used, raise an error
            raise ValueError("No command provided and --seed flag not used.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"General error: {e}")
    finally:
        client.close()
