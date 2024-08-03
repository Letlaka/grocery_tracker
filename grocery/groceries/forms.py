from django import forms # type: ignore
from .models import GroceryItem, Category

class GroceryItem(forms.ModelForm):
    class Meta:
        model = GroceryItem
        fields = ['name', 'quantity', 'category']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']