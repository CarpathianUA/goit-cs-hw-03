def find_all_records(collection):
    """
    Find all records in the given collection.
    """
    if collection.estimated_document_count() == 0:
        print("Collection is empty!")
        return None
    for record in collection.find():
        print(record)


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
    try:
        collection.insert_one(
            {
                "name": name,
                "author": author,
                "price": price,
                "isbn": isbn,
                "tags": tags,
            }
        )
        print(f"Added {name} to collection {collection.name}")
    except Exception as e:
        print(e)


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
    try:
        if collection.count_documents({"name": name}) > 0:
            collection.update_one({"name": name}, {"$set": {"price": new_price}})
            print(f"Updated price of {name} to {new_price}")
        else:
            print(f"Record {name} not found")
        return find_record_by_name(collection, name)
    except Exception as e:
        print(e)


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
    try:
        if collection.count_documents({"name": name}) > 0:
            collection.update_one({"name": name}, {"$addToSet": {"tags": tag}})
            print(f"Added {tag} to {name}")
            return find_record_by_name(collection, name)
        else:
            print(f"Record {name} not found")
            return None
    except Exception as e:
        print(e)


def delete_record_by_name(collection, name):
    """
    Deletes a record from the collection by name.

    Args:
        collection: The collection from which to delete the record.
        name: The name of the record to be deleted.
    """
    try:
        if collection.count_documents({"name": name}) > 0:
            collection.delete_one({"name": name})
            print(f"Deleted {name} from collection {collection.name}")
        else:
            print(f"Record {name} not found")
    except Exception as e:
        print(e)


def delete_all_records(collection):
    """
    Deletes all records from the given collection.
    """
    try:
        collection.delete_many({})
        print("Deleted all records from collection...Done!")
    except Exception as e:
        print(e)
