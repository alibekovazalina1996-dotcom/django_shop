from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product
from .forms import ProductForm

def home(request):
    """Главная страница: список всех товаров."""
    products = Product.objects.all()
    return render(request, 'catalog/home.html', {'products': products})

def contacts(request):
    """Страница контактов."""
    return render(request, 'catalog/contacts.html')

def product_detail(request, pk):
    """Страница подробной информации о товаре."""
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})

def add_product(request):
    """Страница добавления нового товара."""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Товар успешно добавлен!')
            return redirect('home')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = ProductForm()
    
    return render(request, 'catalog/add_product.html', {'form': form})