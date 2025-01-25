from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from admin_app.models import Product
from .forms import ProductForm

def index(request):
    products = Product.objects.all()  # Make sure this gets all products
    return render(request, 'index.html', {'products': products})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product created successfully!')
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})