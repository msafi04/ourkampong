from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from .models import Member
from apps.item.models import Item

class MemberCreationForm(UserCreationForm):
    class Meta:
        model = Member
        fields =  ('username', 'email', 'radius', 'postal_code')

class MemberChangeForm(UserChangeForm):
    class Meta:
        model = Member
        fields = UserChangeForm.Meta.fields

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'image', 'title', 'description', 'price']