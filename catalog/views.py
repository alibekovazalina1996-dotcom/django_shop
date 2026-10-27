from django.views.generic import TemplateView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm

class HomeView(TemplateView):
    template_name = 'catalog/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context

class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

class AddProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/add_product.html'
    success_url = reverse_lazy('home')