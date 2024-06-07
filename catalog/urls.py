from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductDetailView, ProductListView, ContactsPageView, BlogListView

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path("contacts/", ContactsPageView.as_view(), name="contacts"),
    path("product/<int:pk>", ProductDetailView.as_view(), name="product"),
    path("blog_list/", BlogListView.as_view(), name="blog_list"),
]
