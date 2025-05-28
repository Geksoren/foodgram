import os
import django
import json
from api.models import Ingredient

# Настройка окружения Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodgram.settings')
django.setup()


def load_ingredients():
    with open('data/ingredients.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        for item in data:
            Ingredient.objects.create(
                name=item['name'],
                measurement_unit=item['measurement_unit']
            )
    print("Ингредиенты успешно загружены!")


if __name__ == '__main__':
    load_ingredients()