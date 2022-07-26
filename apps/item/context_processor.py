from apps.item.models import Item

#Don't forget o register this in settings Templates
def menu_categories(request):
    categories = Item.category.objects.all()

    return {'menu_categories': categories}