from django.shortcuts import render
from catalog.models import Product


def home(request):
    context = {'product_list': Product.objects.all()}
    return render(request, "home.html", context=context)


def contacts(request):
    if request.method == "POST":
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        # а также передается информация, которую заполнил пользователь
        print(name, phone, message)
    return render(request, "contacts.html")


def product(request, pk):
    context = {'product': Product.objects.get(pk=pk)}
    return render(request, "product.html", context=context)