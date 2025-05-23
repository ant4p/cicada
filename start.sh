#!/bin/sh

until  python manage.py migrate
do
  echo "..."
  sleep 15
  python manage.py shell
  sleep 5
  echo from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', '123')
  sleep 5

done

python manage.py collectstatic --noinput

gunicorn --bind 0.0.0.0:8000 cicada.wsgi