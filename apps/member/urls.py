from django.urls import path
from django.contrib.auth import views as auth_views

from .views import member_admin, register_member, add_item, delete_item

urlpatterns = [
    path('register-user/', register_member, name = 'member/register_member.html'),
    path('member-admin/', member_admin, name = 'member/member_admin.html'),
    path('add-item/', add_item, name = 'member/add_item.html'),
    path('<int:pk>/delete-item/', delete_item, name = 'member/delete_item.html'),
    
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('login/', auth_views.LoginView.as_view(template_name = 'member/login.html'), name = 'login'),

]
