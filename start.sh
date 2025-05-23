#!/bin/sh

until  python manage.py migrate
do
  echo "..."
  sleep 15

done
python manage.py collectstatic --noinput

gunicorn --bind 0.0.0.0:8000 cicada.wsgi