#!/bin/sh

until [
  echo "..."
  sleep 15
  python manage.py shell
  sleep 5
  echo "from django.contrib.auth import get_user_model"
  sleep 5
  echo "User = get_user_model()"
  sleep 5
  echo "User.objects.create_superuser('admin', 'admin@myproject.com', '123')"
  sleep 5

]; do python manage.py migrate

done


python manage.py collectstatic --noinput

gunicorn --bind 0.0.0.0:8000 cicada.wsgi