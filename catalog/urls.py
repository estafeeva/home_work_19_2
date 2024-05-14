from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home

catalog_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
]
