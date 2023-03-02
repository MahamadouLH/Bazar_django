from django.contrib import admin
from .models import Category, Sub_category, Main_Category
# Register your models here.


    

class MainCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
    list_display = ('name', 'slug')
    sortable_by = ('name')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
    list_display = ( 'name','__str__', 'slug')


class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
    list_display = ('name', '__str__', 'slug')



admin.site.register(Main_Category, MainCategoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Sub_category, SubCategoryAdmin)