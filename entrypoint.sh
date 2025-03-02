#!/bin/sh
set -e

echo "Ожидание базы данных..."
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 1
done
echo "База данных доступна!"

echo "Применение миграций..."
python manage.py migrate

echo "Загрузка фикстур..."
python manage.py loaddata payments/fixtures/items.json
python manage.py loaddata payments/fixtures/discounts.json
python manage.py loaddata payments/fixtures/taxes.json
python manage.py loaddata payments/fixtures/orders.json

echo "Создание суперпользователя..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(is_superuser=True).exists():
    User.objects.create_superuser("admin", "admin@example.com", "admin123")
    print("Суперпользователь создан.")
EOF

exec "$@"