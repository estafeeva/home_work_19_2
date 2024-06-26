from django.forms import ModelForm
from catalog.models import Product

class ProductForm(ModelForm):
    """Пользователи могут создавать новые продукты"""
    class Meta:
        model = Product
        fields = "__all__"
