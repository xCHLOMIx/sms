from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import *

# Create your views here.
@login_required(login_url = 'login')
def homeView(request):
    return render(request, "base/main.html")

@login_required(login_url = 'login')
def logoutView(request):
    logout(request)

    return redirect('login')

@login_required(login_url = 'login')
def inventoryView(request):
    products = Product.objects.all()

    return render(request, "base/inventory.html", { "products" : products })

@login_required(login_url = 'login')
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

@login_required(login_url = 'login')
def deleteView(request, pk):
    product = Product.objects.get(pk = pk)

    product.delete()

    return redirect('inventory')

@login_required(login_url = 'login')
def updateView(request, pk):
    product = Product.objects.get(pk = pk)

    if request.method == 'POST':
        name = request.POST['name']

        print(product)

        product.name = name

        product.save()

        return redirect('inventory')

    return render(request, 'base/update-product.html', { "product" : product })

@login_required(login_url = 'login')
def productInView(request):
    products =  Product.objects.all()

    if request.method == 'POST':
        code = Product.objects.get(code = request.POST['code'])
        quantity = request.POST['quantity']
        unitPrice = request.POST['unitPrice']
        totalPrice = unitPrice * quantity

        prodcutIn = ProductIn(code = code, quantity = quantity, unitPrice = unitPrice, totalPrice = totalPrice)
        prodcutIn.save()

        redirect('inventory')
    return render(request, 'base/product-in.html', { "products" : products})

@login_required(login_url = 'login')
def productOutView(request):
    products =  Product.objects.all()

    if request.method == 'POST':
        code = Product.objects.get(code = request.POST['code'])
        quantity = int(request.POST['quantity'])
        unitPrice = int(request.POST['unitPrice'])
        totalPrice = unitPrice * quantity

        prodcutOut = ProductOut(code = code, quantity = quantity, unitPrice = unitPrice, totalPrice = totalPrice)
        prodcutOut.save()

        redirect('inventory')

    return render(request, 'base/product-out.html', { "products" : products })


@login_required(login_url = 'login')
def stockInReportView(request):
    transactions = ProductIn.objects.all()

    return render(request, 'base/stock-in-report.html', { "transactions" : transactions})

@login_required(login_url = 'login')
def stockOutReportView(request):
    transactions = ProductOut.objects.all()

    return render(request, 'base/stock-out-report.html', { "transactions" : transactions})