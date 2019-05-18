from django.shortcuts import render, get_list_or_404
from .models import Product, ProductCategory
from basketapp.models import BasketSlot

def main(request):
    return render(request, 'mainapp/index.html')


def products(request, pk=None):
    basket = []
    if request.user.is_authenticated:
        basket = BasketSlot.objects.filter(user=request.user)
    total_quantity = sum(list(map(lambda basket_slot: basket_slot.quantity, basket)))

    if pk:
        get_list_or_404(ProductCategory, pk=pk)
        product_object = Product.objects.filter(category=pk)
    else:
        product_object = Product.objects.all()
    context = {
        'categoriets' : ProductCategory.objects.all(),
        'products' : product_object,
        'basket_qantity': total_quantity,
    }
    return render(request, 'mainapp/products.html', context)


def contacts(request):
    return render(request, 'mainapp/contacts.html')
