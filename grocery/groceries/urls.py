from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_item', views.add_item, name='add_item'),
    path('item_list', views.item_list, name='item_list'),
    path('category/<int:pk>', views.category_detail, name='category_detail'),
    path('category/edit/<int:pk>', views.category_edit, name='category_edit'),
]
