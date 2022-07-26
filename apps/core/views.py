from django.shortcuts import render

from apps.item.models import Item

def homepage_view(request):
    latest_items = Item.objects.all()

    return render(request, 'core/home.html', {'latest_items': latest_items})

def contact_view(request):
    return render(request, 'core/contact.html')

def about_view(request):
    return render(request, 'core/about.html')
