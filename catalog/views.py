import django.core.exceptions
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from catalog.models import Product, Blog
from django.views.generic.base import TemplateView
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from pytils.translit import slugify

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

    """get_queryset выводит в список статей только те, которые имеют положительный признак публикации"""

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_publication=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    """При открытии отдельной статьи get_object увеличивает счетчик просмотров"""

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


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

    """form_valid при создании динамически формирует slug name для заголовка"""

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog  # Модель
    fields = (
        "title",
        "content",
        "preview",
    )  # Поля для редактирования
    #    success_url = reverse_lazy('catalog:blog_list') # Адрес для перенаправления после успешного редактирования

    """form_valid при создании динамически формирует slug name для заголовка"""

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

    """После успешного редактирования записи get_success_url перенаправляет пользователя на просмотр этой статьи"""

    def get_success_url(self):
        return reverse("catalog:blog", args=[self.kwargs.get("pk")])


class BlogDeleteView(DeleteView):
    model = Blog  # Модель
    success_url = reverse_lazy(
        "catalog:blog_list"
    )  # Адрес для перенаправления после успешного удаления
