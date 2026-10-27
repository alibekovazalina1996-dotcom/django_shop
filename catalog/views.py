from .models import Product

def home(request):
    """Главная страница интернет-магазина."""
    latest_products = Product.objects.order_by('-created_at')[:5]
    print("Последние 5 продуктов:")
    for product in latest_products:
        print(f"{product.name} - {product.price} руб.")
        
    return render(request, 'catalog/home.html')
 
