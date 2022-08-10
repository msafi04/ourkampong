from django.urls import path

from .views import inbox_view, directs_view, send_directs, new_message

urlpatterns = [
    path('inbox/', inbox_view, name = 'inbox'),
    path('inbox/<username>', directs_view, name = 'directs'),
    path('send/', send_directs, name = 'send_direct'),
    path('new/<username>/<slug:category_slug>/<slug:item_slug>', new_message, name = 'new_message'),
]