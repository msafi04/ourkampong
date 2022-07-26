from django.urls import path

from .views import item_view, search_view

urlpatterns = [
    path('<slug:category_slug>/<slug:item_slug>/', item_view, name = 'item/item_detail.html'),
    path('search/', search_view, name = 'item/search.html'),
    #path('<slug:category_slug>/', category_view, name = 'item/category.html'),
]