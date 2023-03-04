from django.shortcuts import render, get_object_or_404
from .models import Product, Variation
from category.models import *
from django.utils.text import slugify
from carts.views import _cart_id
from carts.models import CartItem
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.

def store(request, main_category_slug = None, category_slug = None, sub_category_slug = None):
    categories = None
    products = None
    
    if main_category_slug != None and category_slug == None and sub_category_slug == None:
        main_categories = get_object_or_404(Main_Category, slug = main_category_slug)
        products = Product.objects.filter(main_category = main_categories, is_available = True)
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_product = paginator.get_page(page)
        product_count = products.count()
    elif main_category_slug != None and category_slug != None and sub_category_slug == None:
        main_categories = get_object_or_404(Main_Category, slug = main_category_slug)
        main_categories_id = main_categories.id
        sub_categories = get_object_or_404(Category, slug = category_slug, parent = main_categories_id)
        products = Product.objects.filter(category = sub_categories, is_available = True, main_category = main_categories_id)
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_product = paginator.get_page(page)
        product_count = products.count()
    elif main_category_slug != None and category_slug != None and sub_category_slug != None:
        main_categories = get_object_or_404(Main_Category, slug = main_category_slug)
        main_categories_id = main_categories.id
        categories = get_object_or_404(Category, slug = category_slug, parent = main_categories_id)
        category_id = categories.id
        sub_categories = get_object_or_404(Sub_category, slug = sub_category_slug, parent = category_id)
        products = Product.objects.filter(sub_category = sub_categories, is_available = True, category = category_id, main_category = main_categories_id)
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_product = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        paginator = Paginator(products, 2)
        page = request.GET.get('page')
        paged_product = paginator.get_page(page)
        product_count = products.count()
    
    context = {
        'products' : paged_product,
        'product_count' : product_count,
    }
    return render(request, 'store/store.html', context)


def product_detail(request, main_category_slug, category_slug, sub_category_slug, product_slug):
    try:
        single_product = Product.objects.get(main_category__slug = main_category_slug, category__slug = category_slug, sub_category__slug = sub_category_slug, slug = product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id = _cart_id(request), product = single_product).exists()
    except Exception as e:
        raise e
    
    context = {
        'single_product' : single_product,
        'in_cart' : in_cart,
    }
    
    return render(request, 'store/product_detail.html', context)


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains = keyword) | Q(product_name__icontains = keyword))
            product_count = products.count()
    context = {
        'products' : products,
        'product_count' : product_count,
        'keyword' : keyword,
    }
    return render(request, 'store/store.html', context)