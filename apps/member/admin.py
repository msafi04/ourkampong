from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import MemberCreationForm, MemberChangeForm
from .models import Member

class MemberAdmin(UserAdmin):
    add_form = MemberCreationForm
    form = MemberChangeForm
    model = Member
    list_display = ['email', 'username', 'radius', 'postal_code', 'is_staff',]


admin.site.register(Member, MemberAdmin)