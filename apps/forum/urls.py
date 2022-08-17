from django.urls import path

from .views import posts_list_view, post_detail_view, post_create_view, post_delete_view, post_likes_view

urlpatterns = [

    path('forum/like/<int:pk>', post_likes_view, name = 'post_likes'),
    path('forum/delete/<int:pk>', post_delete_view, name = 'post_delete'), 
    path('forum/new/', post_create_view, name = 'post_new'),
    path('forum/', posts_list_view, name = 'post_list'),
    path('forum/<int:pk>', post_detail_view, name = 'post_detail'),

]