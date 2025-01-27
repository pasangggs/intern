from django.urls import path
from .views import index
# from . import views

urlpatterns = [
    path('', index, name='home'),
    path('api/send/mail',),
    # path('product', views.product_list, name='product_list')
]
