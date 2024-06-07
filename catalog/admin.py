from django.contrib import admin
from catalog.models import Product, Category, Blog


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_filter = ("category",)
    search_fields = ("name", "description")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


@admin.register(Blog)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "content",
        "preview",
        "created_at",
        "is_publication",
        "views_count",
    )