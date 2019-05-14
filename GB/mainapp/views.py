from django.shortcuts import render
from .models import Product, ProductCategory


def main(request):

    return render(request, 'mainapp/index.html')


def products(request, pk=None):
    print(pk)
    context = {'products' : Product.objects.all()}
    return render(request, 'mainapp/products.html', context)


def contacts(request):
    return render(request, 'mainapp/contacts.html')
