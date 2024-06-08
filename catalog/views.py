import django.core.exceptions
from django.shortcuts import render
from django.urls import reverse_lazy
from catalog.models import Product, Blog
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


"""def home(request):
    context = {"product_list": Product.objects.all()}
    return render(request, "product_list.html", context=context)"""


# Перевели имеющиеся контроллеры с FBV на CBV
class ProductListView(ListView):
    model = Product


"""def contacts(request):
    if request.method == "POST":
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        # а также передается информация, которую заполнил пользователь
        print(name, phone, message)
    return render(request, "contacts.html")
"""


# Перевели имеющиеся контроллеры с FBV на CBV
class ContactsPageView(TemplateView):
    template_name = "catalog/contacts.html"


# FBV
"""def product(request, pk):
    try:
        context = {"product": Product.objects.get(pk=pk)}
        return render(request, "product_detail.html", context=context)
    except django.core.exceptions.ObjectDoesNotExist:
        return render(request, "404.html")
"""


# Перевели имеющиеся контроллеры с FBV на CBV
class ProductDetailView(DetailView):
    model = Product


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog


class BlogCreateView(CreateView):
    model = Blog  # Модель
    fields = (
        "title",
        "content",
        "preview",
    )  # Поля для заполнения при создании
    success_url = reverse_lazy(
        "catalog:blog_list"
    )  # Адрес для перенаправления после успешного создания

class BlogUpdateView(UpdateView):
    model = Blog # Модель
    fields = (
        "title",
        "content",
        "preview",
    )  # Поля для редактирования
    success_url = reverse_lazy('catalog:blog_list') # Адрес для перенаправления после успешного редактирования


class BlogDeleteView(DeleteView):
    model = Blog # Модель
    success_url = reverse_lazy('catalog:blog_list') # Адрес для перенаправления после успешного удаления