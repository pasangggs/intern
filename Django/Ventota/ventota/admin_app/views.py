from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.
# def dashboard(request):
#     if not request.user.is_authenticated:
#         return redirect('login')
    # return render(request, 'admin_pages/dashboard.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')  # Replace with your admin dashboard URL
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'admin_pages/login.html')

# Product List
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    products = Product.objects.all()
    return render(request, 'admin_pages/dashboard.html', {'products': products})

def product_create(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')

        if not name or not image:
            messages.error(request, "Both name and image are required.")
            return render(request, 'admin_pages/dashboard.html')

        # Save the product
        Product.objects.create(name=name, image=image)
        messages.success(request, "Product created successfully!")
        return redirect('dashboard')  # Redirect to the 'dashboard' URL

    return render(request, 'admin_pages/dashboard.html')


# Update Product
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

# Update Product
def product_update(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    
    # Retrieve the product to be updated
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        # Update the product name
        product.name = request.POST.get('name', product.name)
        
        # Update the product image if provided
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        
        # Save the updated product
        product.save()
        messages.success(request, "Product updated successfully!")
        return redirect('dashboard')  # Redirect to the dashboard after update
    
    return render(request, 'admin_pages/dashboard.html', {'product': product})


# Delete Product
def product_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('dashboard')
