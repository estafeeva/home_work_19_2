# Generated by Django 4.2.2 on 2024-07-05 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0007_product_owner"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["name", "price"],
                "permissions": [
                    ("set_published", "Can publish posts"),
                    ("change_description", "Can change description"),
                    ("change_category", "Can change category"),
                ],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="is_published",
            field=models.BooleanField(default=False, verbose_name="Признак публикации"),
        ),
    ]
