from django.db import models
from django.urls import reverse
from category.models import Main_Category, Category, Sub_category

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(max_length=128, unique=True)
    description = models.TextField(max_length=512, blank=True, null=True)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    thumbnail = models.ImageField(upload_to="photos/products", blank=True, null=True)
    main_category = models.ForeignKey(Main_Category, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(Sub_category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    
    def get_url(self):
        return reverse('product_detail', args=[self.main_category.slug, self.category.slug, self.sub_category.slug, self.slug])
    
    
    def __str__(self):
        return self.product_name


variation_list = ['colors', 'sizes', 'brands', 'rom_memories', 'ram_memories']


class VariationManager(models.Manager):
    
    def colors(self):
        return super(VariationManager, self).filter(variation_category = 'color', is_active = True)
    
    def sizes(self):
        return super(VariationManager, self).filter(variation_category = 'size', is_active = True)
    
    def brands(self):
        return super(VariationManager, self).filter(variation_category = 'brand', is_active = True)
    
    def rom_memories(self):
        return super(VariationManager, self).filter(variation_category = 'rom_memory', is_active = True)
    
    def ram_memories(self):
        return super(VariationManager, self).filter(variation_category = 'ram_memory', is_active = True)
    



variation_category_choice = (
    ('color', 'color'),
    ('size', 'size'),
    ('brand', 'brand'),
    ('rom_memory', 'rom_memory'),
    ('ram_memory', 'ram_memory'),
)



class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=128, choices=variation_category_choice)
    variation_value = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now = True)
    
    objects = VariationManager()
    
    def __str__(self):
        return self.variation_value