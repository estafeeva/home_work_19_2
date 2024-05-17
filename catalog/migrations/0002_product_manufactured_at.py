# Generated by Django 5.0.3 on 2024-05-17 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="manufactured_at",
            field=models.DateField(
                blank=True,
                help_text="Введите Дату производства",
                null=True,
                verbose_name="Дата производства",
            ),
        ),
    ]
