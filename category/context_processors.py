from .models import Main_Category, Category, Sub_category

def menu_links(request):
    main_links = Main_Category.objects.all()
    cat_links = Category.objects.all()
    sub_cat_links = Sub_category.objects.all()
    return dict(main_links = main_links, cat_links = cat_links, sub_cat_links = sub_cat_links)

