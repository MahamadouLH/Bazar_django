from django.db import models
from django.urls import reverse
# Create your models here.

class Main_Category(models.Model):
    name = models.CharField(max_length=128, unique=False)
    slug = models.SlugField(max_length=128, unique=False)
    description = models.TextField(max_length=255, blank=True)
    cat_img = models.ImageField(upload_to='photos/categories', blank=True)
    
    class Meta:
        verbose_name = 'Main_category'
        verbose_name_plural = 'Main_categories'
        ordering = ['name']
        
    def get_url(self):
        return reverse('product_by_main_category', args = [self.slug])
    
    def __str__(self):
        return self.name



class Category(models.Model):
    parent = models.ForeignKey(Main_Category, on_delete=models.CASCADE, related_name='category', parent_link=True)
    name = models.CharField(max_length=128, unique=False)
    slug = models.SlugField(max_length=128, unique=False)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['parent', 'name']
    
    def get_url(self):
        return reverse('product_by_category', args = [self.parent.slug, self.slug])
    
    
    def __str__(self):
        return self.parent.name + ' / ' + self.name



class Sub_category(models.Model):
    parent = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_category', parent_link=True)
    name = models.CharField(max_length=128, unique=False)
    slug = models.SlugField(max_length=128, unique=False)
    class Meta:
        verbose_name = 'Sub_category'
        verbose_name_plural = 'Sub_categories'
        ordering = ['parent', 'name']
    
    
    def get_url(self):
        return reverse('product_by_sub_category', args = [self.parent.parent.slug, self.parent.slug, self.slug])
    
    
    def __str__(self):
        return self.parent.parent.name + ' / ' + self.parent.name + ' / ' +self.name


