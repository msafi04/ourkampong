import random

from django.db.models import Q
from django.shortcuts import render, get_list_or_404

from .models import Item

def item_view(request, category_slug, item_slug):
    item_detail = get_list_or_404(Item, cat_slug = category_slug, slug = item_slug)
    
    return render(request, 'item/item_detail.html', {'item_detail': item_detail})

def category_view(request, category_slug):
    category_detail = get_list_or_404(Item.category, slug = category_slug)

    return render(request, 'items/category.html', {'category_detail': category_detail})

def search_view(request):
    query = request.GET.get('query', '')
    items = Item.objects.filter(Q(title__icontains = query) | Q(description__icontains = query))

    return render(request, 'item/search.html', {'items': items, 'query': query})