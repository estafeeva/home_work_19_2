from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (
    ProductDetailView,
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ContactsPageView,
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView, CategoryListView, CategoryDetailView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path("categories/", CategoryListView.as_view(), name="categories"),
    path("categories/category/<int:pk>", cache_page(60)(CategoryDetailView.as_view()), name="category"),
    path("contacts/", ContactsPageView.as_view(), name="contacts"),
    path("product/<int:pk>", cache_page(60)(ProductDetailView.as_view()), name="product"),
    path("blog_list/", BlogListView.as_view(), name="blog_list"),
    path("blog_list/blog/<int:pk>", BlogDetailView.as_view(), name="blog"),
    path("blog_list/blog/create", BlogCreateView.as_view(), name="create"),
    path("blog_list/blog/update/<int:pk>", BlogUpdateView.as_view(), name="update"),
    path("blog_list/blog/delete/<int:pk>", BlogDeleteView.as_view(), name="delete"),
    path("product/create", ProductCreateView.as_view(), name="create_product"),
    path("product/update/<int:pk>", ProductUpdateView.as_view(), name="update_product"),
    path("product/delete/<int:pk>", ProductDeleteView.as_view(), name="delete_product"),
]
