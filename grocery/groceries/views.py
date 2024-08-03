from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from .models import Category, GroceryItem
from .forms import GroceryItem, CategoryForm

def index(request):
    categories = Category.objects.all()
    context = {"title": "Home",'categories': categories}
    return render(request, 'groceries/index.html', context)

def add_item(request):
    if request.method == 'POST':
        form = GroceryItem(request.POST)
        if form.is_valid():
            form.save()
            return redirect("item_list")
    else:
        form = GroceryItem()
    context = {"form": form}
    return render(request, 'groceries/add_item.html', context)

def item_list(request):
    items = GroceryItem.objects.all()
    return render(request, 'grocery/item_list.html', {'items': items})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'grocery/category_detail.html', {'category': category})

def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_detail', pk=category.pk)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'grocery/category_edit.html', {'form': form, 'category': category})