from django.urls import path
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
    BlogDeleteView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path("contacts/", ContactsPageView.as_view(), name="contacts"),
    path("product/<int:pk>", ProductDetailView.as_view(), name="product"),
    path("blog_list/", BlogListView.as_view(), name="blog_list"),
    path("blog_list/blog/<int:pk>", BlogDetailView.as_view(), name="blog"),
    path("blog_list/blog/create", BlogCreateView.as_view(), name="create"),
    path("blog_list/blog/update/<int:pk>", BlogUpdateView.as_view(), name="update"),
    path("blog_list/blog/delete/<int:pk>", BlogDeleteView.as_view(), name="delete"),
    path("product/create", ProductCreateView.as_view(), name="create_product"),
    path("product/update/<int:pk>", ProductUpdateView.as_view(), name="update_product"),
    path("product/delete/<int:pk>", ProductDeleteView.as_view(), name="delete_product"),
]
