
from django.urls import path

from .views import homepage_view, contact_view, about_view

urlpatterns = [
    path('', homepage_view, name = 'core/homepage'),
    path('about/', about_view, name = 'core/about'),
    path('contact', contact_view, name = 'core/contact'),
]