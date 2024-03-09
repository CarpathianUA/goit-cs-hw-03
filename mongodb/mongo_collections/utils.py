def exception_handler(func):
    """
    A decorator that wraps the passed in function and catches exceptions.

    Args:
        func: The function to wrap.

    Returns:
        The wrapper function.
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred in {func.__name__}: {e}")
            return None

    return wrapper


@exception_handler
def find_all_records(collection):
    """
    Find all records in the given collection.
    """
    if collection.estimated_document_count() == 0:
        print("Collection is empty!")
        return None
    for record in collection.find():
        print(record)


@exception_handler
def find_record_by_name(collection, name):
    """
    Find a record in the collection by name.

    Args:
        collection: The collection to search in.
        name: The name of the record to search for.
    """
    if collection.count_documents({"name": name}) > 0:
        for record in collection.find({"name": name}):
            print(record)
    else:
        print(f"Record {name} not found")


@exception_handler
def add_new_record(collection, name, author, price, isbn, tags):
    """
    Function to add a new record to a collection.

    Parameters:
    - collection: the collection to which the record will be added
    - name: the name of the record
    - author: the author of the record
    - price: the price of the record
    - isbn: the ISBN of the record
    - tags: the tags associated with the record
    """
    result = collection.insert_one(
        {
            "name": name,
            "author": author,
            "price": price,
            "isbn": isbn,
            "tags": tags,
        }
    )
    print(f"Added {name} to collection {collection.name}")
    print("ID of the inserted document:", result.inserted_id)


@exception_handler
def update_record_price(collection, name, new_price):
    """
    Update the price of a record in the collection.

    Args:
        collection: The collection to update.
        name: The name of the record.
        new_price: The new price to set.

    Returns:
        The updated record.
    """
    if collection.count_documents({"name": name}) > 0:
        collection.update_many({"name": name}, {"$set": {"price": new_price}})
        print(f"Updated price of {name} to {new_price}")
    else:
        print(f"Record {name} not found")


@exception_handler
def add_new_tag_to_record(collection, name, tag):
    """
    Add a new tag to a record in the collection.

    Args:
        collection: The collection in which to update the record.
        name: The name of the record to update.
        tag: The new tag to add to the record.

    Returns:
        The updated record with the new tag added.
    """
    if collection.count_documents({"name": name}) > 0:
        collection.update_many({"name": name}, {"$addToSet": {"tags": tag}})
        print(f"Added {tag} to {name}")
        return find_record_by_name(collection, name)
    else:
        print(f"Record {name} not found")
        return None


@exception_handler
def delete_record_by_name(collection, name):
    """
    Deletes a record from the collection by name.

    Args:
        collection: The collection from which to delete the record.
        name: The name of the record to be deleted.
    """
    if collection.count_documents({"name": name}) > 0:
        collection.delete_many({"name": name})
        print(f"Deleted {name} from collection {collection.name}")
    else:
        print(f"Record {name} not found")


@exception_handler
def delete_all_records(collection):
    """
    Deletes all records from the given collection.
    """
    collection.delete_many({})
    print("Deleted all records from collection...Done!")
