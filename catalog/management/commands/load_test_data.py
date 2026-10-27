from django.core.management.base import BaseCommand 
from django.core.management import call_command 
from catalog.models import Product, Category 
 
class Command(BaseCommand): 
    help = 'Загружает тестовые данные из фикстур' 
 
    def handle(self, *args, **options): 
        self.stdout.write('Удаляем старые данные...') 
        Product.objects.all().delete() 
        Category.objects.all().delete() 
 
        self.stdout.write('Загружаем фикстуры...') 
        call_command('loaddata', 'categories.json') 
        call_command('loaddata', 'products.json') 
 
        self.stdout.write(self.style.SUCCESS('Данные успешно загружены!')) 
