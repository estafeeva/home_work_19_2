# myapp/management/commands/fill.py
from django.core.management import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        Category.objects.create(name="Овощи", description="Сезонные овощи")
        Category.objects.create(name="Фрукты", description="Сезонные фрукты")
        Category.objects.create(name="Ягоды", description="Сезонные ягоды")

        Product.objects.create(
            name="Яблоко",
            category_id=Category.objects.get(name="Фрукты").id,
            description="Яблоки антоновка",
            price=120,
        )
        Product.objects.create(
            name="Картошка",
            category_id=Category.objects.get(name="Овощи").id,
            description="Просто картошка",
            price=40,
        )
        Product.objects.create(
            name="Малина",
            category_id=Category.objects.get(name="Ягоды").id,
            description="Малина желтая",
            price=300,
        )
