from django.shortcuts import render, redirect
from .models import Products


def shopIndex(request):
    products = Products.objects.all()
    return render(request, 'shop/catalog.html', {'products': products})