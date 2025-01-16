from django.urls import path
from .views import dashboard, admin_login, product_create, product_update, product_delete

urlpatterns = [
    path('', dashboard, name='dashboard'),  # Dashboard URL
    path('login/', admin_login, name='login'),  # Login URL
    path('product/create/', product_create, name='product_create'),  # Create product URL
    path('product/update/<int:pk>/', product_update, name='product_update'),  # Update product URL
    path('product/delete/<int:pk>/', product_delete, name='product_delete'),  # Delete product URL
]
