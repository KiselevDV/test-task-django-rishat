import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.contrib.auth import get_user_model
from django.core.management import call_command

User = get_user_model()


def initialize_database():
    print("Применение миграций...")
    call_command("migrate")

    if not User.objects.filter(is_superuser=True).exists():
        print("Загрузка фикстур...")
        fixtures = [
            "payments/fixtures/items.json",
            "payments/fixtures/discounts.json",
            "payments/fixtures/taxes.json",
            "payments/fixtures/orders.json"
        ]
        for fixture in fixtures:
            call_command("loaddata", fixture)

        print("Создание суперпользователя...")
        User.objects.create_superuser("admin", "admin@example.com", "admin123")
        print("Суперпользователь 'admin' создан успешно.")
    else:
        print("Суперпользователь уже существует")


if __name__ == "__main__":
    initialize_database()
