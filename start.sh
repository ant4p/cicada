#!/bin/sh


until
    python manage.py makemigrations
    sleep 5
    python manage.py migrate

do
  echo "...prepare_database..."
  sleep 20

done

sleep 5

if
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.get(is_superuser=True) != []" | python manage.py shell

then
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', '123')" | python manage.py shell
fi

python manage.py collectstatic --noinput

gunicorn --bind 0.0.0.0:8000 cicada.wsgi