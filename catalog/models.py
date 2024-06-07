from django.db import models

# Create your models here.


class Category(models.Model):
    """Category
    Наименование
    Описание"""

    name = models.CharField(
        max_length=100,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        blank=True,
        null=True,
        max_length=300,
        verbose_name="Описание категории",
        help_text="Введите описание категории",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Product(models.Model):
    """Product:
    Наименование
    Описание
    Изображение (превью)
    Категория
    Цена за покупку
    Дата создания (записи в БД)
    Дата последнего изменения (записи в БД)"""

    name = models.CharField(
        max_length=100,
        verbose_name="Наименование продукта",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        blank=True,
        null=True,
        max_length=300,
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
    )
    photo = models.ImageField(
        upload_to="media/photo",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        max_length=100,
        verbose_name="Категория продукта",
        help_text="Введите категорию продукта",
        null=True,
        blank=True,
        related_name="products",
    )
    price = models.PositiveIntegerField(
        verbose_name="Стоимость продукта",
        help_text="Введите стоимость продукта",
    )
    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата создания (записи в БД)",
        help_text="Введите Дату создания",
    )
    updated_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата последнего изменения (записи в БД)",
        help_text="Введите Дату последнего изменения",
    )
    """   manufactured_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата производства",
        help_text="Введите Дату производства",
    )
"""

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price"]


"""Свяжите продукт и категорию, используя связь между таблицами «Один ко многим».
У одной категории может быть много продуктов, но у одного продукта может быть только одна категория.
Воспользуйтесь специальным полем модели — ForeignKey()."""


class Blog(models.Model):
    """заголовок;
    slug (реализовать через CharField);
    содержимое;
    превью (изображение);
    дата создания;
    признак публикации;
    количество просмотров."""

    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок статьи",
        help_text="Введите заголовок статьи",
    )
    slug = models.CharField(
        max_length=200,
        verbose_name="slug",
        blank=True,
        null=True,
    )
    content = models.TextField(
        blank=True,
        null=True,
        verbose_name="Содержимое статьи",
        help_text="Введите текст статьи",
    )
    preview = models.ImageField(
        upload_to="media/photo",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите изображение",
    )
    created_at = models.DateField(
        auto_created=True,
        blank=True,
        null=True,
        verbose_name="Дата создания (записи в БД)",
        help_text="Введите Дату создания",
    )
    is_publication = models.BooleanField(
        default=True,
    )
    views_count = models.PositiveIntegerField(
        default=0,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["title"]