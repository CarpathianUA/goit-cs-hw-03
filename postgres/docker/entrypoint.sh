#!/bin/bash

set -e

host="$1"
shift
cmd="$@"

until PGPASSWORD="postgres" psql -h "$host" -U "postgres" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - start application"
exec $cmd
