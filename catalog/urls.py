from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    # Критерий: URL вида /products/int:pk/, нейминг product_detail
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
]