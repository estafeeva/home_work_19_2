import django.core.exceptions
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from catalog.models import Product, Blog, Category
from catalog.models import Product, Blog, Version
from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from django.views.generic.base import TemplateView
from django.forms import inlineformset_factory
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from pytils.translit import slugify

from catalog.services import get_categories_from_cache, get_products_from_cache

"""def home(request):
    context = {"product_list": Product.objects.all()}
    return render(request, "product_list.html", context=context)"""


# Перевели имеющиеся контроллеры с FBV на CBV
class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    login_url = "/users/login/"

    def get_queryset(self):
        return get_products_from_cache()

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
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    login_url = "/users/login/"

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")
    login_url = "/users/login/"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # Формирование формсета
        ProductFormset = inlineformset_factory(
            Product, Version, form=VersionForm, extra=1
        )
        if self.request.method == "POST":
            context_data["formset"] = ProductFormset(
                self.request.POST, instance=self.object
            )
        else:
            context_data["formset"] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data["formset"]

        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            user = self.request.user
            self.object.owner = user
            self.object.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:

            return self.render_to_response(
                self.get_context_data(form=form, formset=formset)
            )

    """def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.save()

        return super().form_valid(form)"""


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")
    login_url = "/users/login/"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # Формирование формсета
        ProductFormset = inlineformset_factory(
            Product, Version, form=VersionForm, extra=1
        )
        if self.request.method == "POST":
            context_data["formset"] = ProductFormset(
                self.request.POST, instance=self.object
            )
        else:
            context_data["formset"] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data["formset"]

        if form.is_valid() and formset.is_valid():
            self.object = form.save()

            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:

            return self.render_to_response(
                self.get_context_data(form=form, formset=formset)
            )

    """def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.save()

        return super().form_valid(form)"""

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.set_published") and user.has_perm("catalog.change_description") and user.has_perm("catalog.change_category"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product  # Модель
    success_url = reverse_lazy(
        "catalog:home"
    )  # Адрес для перенаправления после успешного удаления
    login_url = "/users/login/"

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.set_published") and user.has_perm("catalog.change_description") and user.has_perm("catalog.change_category"):
            return ProductModeratorForm
        raise PermissionDenied

class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    login_url = "/users/login/"

    def get_queryset(self):
        return get_categories_from_cache()

class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category
    login_url = "/users/login/"

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
