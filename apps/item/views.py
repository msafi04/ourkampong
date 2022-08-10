import random

from django.db.models import Q
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required

from .models import Item

def item_view(request, category_slug, item_slug):
    item_detail = get_list_or_404(Item, cat_slug = category_slug, slug = item_slug)

    likes_item = get_object_or_404(Item, cat_slug = category_slug, slug = item_slug)
    total_likes = likes_item.total_likes()
    
    return render(request, 'item/item_detail.html', {'item_detail': item_detail, 'total_likes': total_likes})

def category_view(request, category_slug):
    category_detail = get_list_or_404(Item.category, slug = category_slug)

    return render(request, 'items/category.html', {'category_detail': category_detail})

def search_view(request):
    query = request.GET.get('query', '')
    items = Item.objects.filter(Q(title__icontains = query) | Q(description__icontains = query))

    return render(request, 'item/search.html', {'items': items, 'query': query})

@login_required
def likes_view(request, category_slug, item_slug):
    item = get_object_or_404(Item, id = request.POST.get('item_id'))
    item.likes.add(request.user)

    print(item, category_slug, item_slug)
    return HttpResponseRedirect(reverse('item/item_detail.html', args = [category_slug, item_slug]))