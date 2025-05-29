from django.core.management.base import BaseCommand
import json
from api.models import Ingredient


class Command(BaseCommand):
    help = 'Load ingredients from JSON file'

    def handle(self, *args, **options):
        with open('data/ingredients.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                Ingredient.objects.create(
                    name=item['name'],
                    measurement_unit=item['measurement_unit']
                )
        self.stdout.write(self.style.SUCCESS('Ингредиенты успешно загружены!'))