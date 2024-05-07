import json
from pathlib import Path

from django.core.management.base import BaseCommand
from Catalog.models import Category, Product

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open(BASE_DIR / 'Catalog/fixtures/categories.json', 'r', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def json_read_products():
        with open(BASE_DIR / 'Catalog/fixtures/products.json', 'r', encoding='utf-8') as file:
            return json.load(file)

    def handle(self, *args, **options):
        Category.objects.all().delete()
        category_for_create = []
        for category_data in self.json_read_categories():
            category_for_create.append(
                Category(
                    name=category_data['fields']['name'],
                    description=category_data['fields']['description']
                )
            )
        Category.objects.bulk_create(category_for_create)

        Product.objects.all().delete()
        categories = Category.objects.all()
        product_for_create = []
        old_category_name = ""
        for product_data in self.json_read_products():
            category_pk = product_data['fields']['category']
            for el in self.json_read_categories():
                if el['pk'] == category_pk:
                    old_category_name = el['fields']['name']
            category = categories.get(name=old_category_name)
            if category:
                product_for_create.append(
                    Product(
                        name=product_data['fields']['name'],
                        description=product_data['fields']['description'],
                        category=category,
                        picture=product_data['fields']['picture'],
                        price=product_data['fields']['price']
                    )
                )

        # Сохранение продуктов в базу данных
        Product.objects.bulk_create(product_for_create)
