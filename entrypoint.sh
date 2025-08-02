#!/bin/sh
set -e

echo "Connecting to Database"

: "${DATABASE_PORT:=5432}"

while ! nc -z "$DATABASE_HOST" "$DATABASE_PORT"; do 
    echo "Waiting for database at $DATABASE_HOST:$DATABASE_PORT ..."
    sleep 1
done

echo "Database is ready"

python manage.py migrate

python manage.py runserver 0.0.0.0:8000