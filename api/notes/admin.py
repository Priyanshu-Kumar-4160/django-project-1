from django.contrib import admin
from .models import Note, Category, Product
# from .models import Category
# from .models import Product


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')  # Columns to show in list view
    search_fields = ('title',)                   # Add a search bar
    list_filter = ('created_at',)                # Add a sidebar filter
    ordering = ('-created_at',)        
    readonly_fields = ('created_at',)

    fieldsets = (
        ('Note Details', {
            'fields': ('title', 'content')
        }),
        ('Meta Information', {
            'fields': ('created_at',),
        }),
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'category']
    list_filter = ['category']
    search_fields = ['name']
# Register your models here.
# admin.site.register(Category)
# admin.site.register(Product)