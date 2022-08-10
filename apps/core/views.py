from django.shortcuts import render

from django.db.models import Q

from apps.item.models import Item

def homepage_view(request):
    if request.user.is_authenticated:
        user_location = request.user.location
        user_postal_code = request.user.postal_code
        
        latest_items = Item.objects.filter(Q(member__postal_code__startswith = user_postal_code[:2]))

        return render(request, 'core/home.html', {'latest_items': latest_items, 'user_location': user_location})
    else:
        latest_items = Item.objects.all()

        return render(request, 'core/home.html', {'latest_items': latest_items})       

def contact_view(request):
    return render(request, 'core/contact.html')

def about_view(request):
    return render(request, 'core/about.html')

def guidelines_view(request):
    return render(request, 'core/guidelines.html')
