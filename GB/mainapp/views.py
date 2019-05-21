from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory
from basketapp.models import BasketSlot

def main(request):
    return render(request, 'mainapp/index.html')


def products(request, pk=None):
    if pk or pk == 0:
        product_object = Product.objects.all()
        if pk:
            get_object_or_404(ProductCategory, pk=pk)
            product_object = Product.objects.filter(category=pk)
        context = {
            'categoriets' : ProductCategory.objects.all(),
            'products' : product_object,
        }
        return render(request, 'mainapp/products.html', context)

    else:
        hot_product = Product.objects.filter(is_hop=True).first()
        context = {
            'categoriets': ProductCategory.objects.all(),
            'hot_product': hot_product,
        }
        return render(request, 'mainapp/hot_product.html', context)


def product(request, pk):
    title = 'продукты'

    content = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
    }

    return render(request, 'mainapp/product.html', content)


def contacts(request):
    return render(request, 'mainapp/contacts.html')
