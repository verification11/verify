#!/bin/bash
echo "building the project"
python3.9 -m pip install -r requirements.txt

echo "make migration.."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo "collect static..."
python3.9 manage.py collectstatic --noinput --clear