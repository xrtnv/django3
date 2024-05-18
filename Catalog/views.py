from django.shortcuts import render, get_object_or_404

from Catalog.models import Category, Product


def catalog(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'catalog.html', context)


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'product_details.html', context)
