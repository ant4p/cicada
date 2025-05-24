#!/bin/sh

until python manage.py migrate

do
  echo "..."
  sleep 20

done


python manage.py shell

sleep 5
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', '123')"
sleep 5
echo "from services.models import Service; Service = get_model(); Service.objects.create(title='3D Моделирование', slug='3d-modelirovanie')"
sleep 5
echo "from services.models import Service; Service = get_model(); Service.objects.create(title='3D Визуализация', slug='3d-vizualizaciya')"
sleep 5

python manage.py collectstatic --noinput

gunicorn --bind 0.0.0.0:8000 cicada.wsgi