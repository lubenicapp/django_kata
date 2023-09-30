#!/bin/sh

python manage.py migrate --fake api
python manage.py migrate

echo "migrated"

python manage.py runserver 0.0.0.0:8000
