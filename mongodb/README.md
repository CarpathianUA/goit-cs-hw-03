### Demo application to seed a MongoDB database using PyMongo

Instead of cats collection I decided to use collection for sci fi books.
Collection record schema can be looked up in `mongo_collections/seed.py`

## Start MongoDB

```shell
docker-compose up -d
````

## Stop MongoDB

```shell
docker-compose down
```

## Usage

1. Start MongoDB with `docker-compose up -d`
2. Install requirements with `pip install -r requirements.txt`
3. Seed a collection with `python main.py --seed`
4. Run `main.py` to emulate a MongoDB CLI:

```shell
python main.py --help
```

Some examples:

```shell
python main.py -c find_all
python main.py -c update_record_price -n "<NAME>" -p 55.00
```
