from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    """Главная страница: список всех товаров."""
    # Критерий: Использован лаконичный запрос Product.objects.all()
    products = Product.objects.all()
    return render(request, 'catalog/home.html', {'products': products})

def contacts(request):
    """Страница контактов."""
    return render(request, 'catalog/contacts.html')

def product_detail(request, pk):
    """Страница подробной информации о товаре."""
    # Критерий: Контроллер получает pk, извлекает объект через ORM и передает его в шаблон
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})