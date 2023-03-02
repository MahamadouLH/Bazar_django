from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import *
from django.utils.text import slugify

# Create your views here.

def store(request, main_category_slug = None, category_slug = None, sub_category_slug = None):
    categories = None
    products = None
    
    if main_category_slug != None and category_slug == None and sub_category_slug == None:
        main_categories = get_object_or_404(Main_Category, slug = main_category_slug)
        products = Product.objects.filter(main_category = main_categories, is_available = True)
        product_count = products.count()
    elif main_category_slug != None and category_slug != None and sub_category_slug == None:
        main_categories = get_object_or_404(Main_Category, slug = main_category_slug)
        main_categories_id = main_categories.id
        sub_categories = get_object_or_404(Category, slug = category_slug, parent = main_categories_id)
        products = Product.objects.filter(category = sub_categories, is_available = True, main_category = main_categories_id)
        product_count = products.count()
    elif main_category_slug != None and category_slug != None and sub_category_slug != None:
        main_categories = get_object_or_404(Main_Category, slug = main_category_slug)
        main_categories_id = main_categories.id
        categories = get_object_or_404(Category, slug = category_slug, parent = main_categories_id)
        category_id = categories.id
        sub_categories = get_object_or_404(Sub_category, slug = sub_category_slug, parent = category_id)
        products = Product.objects.filter(sub_category = sub_categories, is_available = True, category = category_id, main_category = main_categories_id)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()
    
    context = {
        'products' : products,
        'product_count' : product_count,
    }
    return render(request, 'store/store.html', context)


def product_detail(request, main_category_slug, category_slug, sub_category_slug, product_slug):
    try:
        single_product = Product.objects.get(main_category__slug = main_category_slug, category__slug = category_slug, sub_category__slug = sub_category_slug, slug = product_slug)
    except Exception as e:
        raise e
    
    context = {
        'single_product' : single_product,
    }
    
    return render(request, 'store/product_detail.html', context)