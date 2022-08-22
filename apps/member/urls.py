from django.urls import path
from django.contrib.auth import views as auth_views

from .views import (donate_badges, member_admin, 
                    register_member, 
                    add_item, 
                    delete_item, 
                    edit_item, 
                    edit_user, 
                    donation_view,
                    donate_badges
                )
from .forms import ResetPasswordForm, NewPasswordForm

urlpatterns = [
    path('register-user/', register_member, name = 'member/register_member.html'),
    path('member-admin/', member_admin, name = 'member/member_admin.html'),
    path('add-item/', add_item, name = 'member/add_item.html'),
    path('<int:pk>/delete-item/', delete_item, name = 'delete_item'),
    path('edit-item/<int:pk>/', edit_item, name = 'member/edit_item.html'),
    path('edit-user/<int:pk>/', edit_user, name = 'member/edit_user.html'),
    path('donate/', donation_view, name = 'member/donate.html'),
    path('donate/badges', donate_badges, name = 'donate_badges'),

    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('login/', auth_views.LoginView.as_view(template_name = 'member/login.html'), name = 'login'),

    path('reset-password/', auth_views.PasswordResetView.as_view(template_name = 'member/password_reset.html', form_class = ResetPasswordForm), 
                                                                                name = 'reset_password'),
    path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(template_name = 'member/password_reset_done.html'), 
                                                                                name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'member/password_reset_confirm.html', form_class = NewPasswordForm), 
                                                                                name = 'password_reset_confirm'),
    path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'member/password_reset_complete.html'), name = 'password_reset_complete'),

]
