from django.contrib import admin #type: ignore
from .models import Category, GroceryItem

admin.site.register(Category)
admin.site.register(GroceryItem)
