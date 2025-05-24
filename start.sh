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

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', '123')" | python manage.py shell

echo "from services.models import Service; Service.objects.create(title='3D Моделирование', slug='3d-modelirovanie', content='123')" | python manage.py shell

echo "from services.models import Service; Service.objects.create(title='3D Визуализация', slug='3d-vizualizaciya', content='123')" | python manage.py shell



python manage.py collectstatic --noinput

gunicorn --bind 0.0.0.0:8000 cicada.wsgi