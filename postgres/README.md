### Demo application to create schema and seed PostgresSQL database using SQLAlchemy

## Start

```shell
docker-compose up --build -d
````

## Stop

```shell
docker-compose down
```

## Implementation

Queries are stored in the `sql/queries.sql` file.
After containers start, application will waite for database to be available
and create a schema based on the models in `models`, and seed the database
with mock data.

DML queries executions results can be checked in application stdout logs. 
