from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import *

# Create your views here.

def homeView(request):
    return render(request, "base/main.html")

def logoutView(request):
    logout(request)

    return redirect('login')

def inventoryView(request):
    products = Product.objects.all()

    return render(request, "base/inventory.html", { "products" : products })

def addProductView(request):
    error = ''

    if request.method == 'POST':
        name = request.POST['name']

        if Product.objects.filter(name = name).exists():
            error = "Product already exists"
            return render(request, 'base/add-product.html', { "error" : error})
        else:
            product = Product(name = name)
            product.save()

            return redirect('inventory')

    return render(request, 'base/add-product.html')

def deleteView(request, pk):
    product = Product.objects.get(pk = pk)

    product.delete()

    return redirect('inventory')

def updateView(request, pk):
    product = Product.objects.get(pk = pk)

    if request.method == 'POST':
        name = request.POST['name']

        print(product)

        product.name = name

        product.save()

        return redirect('inventory')

    return render(request, 'base/update-product.html', { "product" : product })