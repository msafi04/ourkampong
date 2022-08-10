from django.contrib.auth.forms import (
                                        UserCreationForm, 
                                        UserChangeForm, 
                                        PasswordResetForm,
                                        SetPasswordForm
                                )
from django.forms import ModelForm
from django import forms

from .models import Member
from apps.item.models import Item, ItemImage

class MemberCreationForm(UserCreationForm):
    class Meta:
        model = Member
        fields =  ('username', 'email', 'radius', 'postal_code')

class MemberChangeForm(UserChangeForm):
    class Meta:
        model = Member
        fields = ('username', 'email', 'radius', 'postal_code', 'profile_pic')

class ResetPasswordForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)

    email = forms.CharField(widget = forms.TextInput(attrs = {'class': 'input',
                                                                'type': 'email',
                                                                'placeholder': 'Enter Email-id'
                                                            }))

class NewPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(NewPasswordForm, self).__init__(*args, **kwargs)
    
    new_password1 = forms.CharField(widget = forms.PasswordInput(attrs = {'class': 'input',
                                                                            'type': 'password',
                                                                            'autocomplete': 'new-password'
                                                                        }))
    new_password2 = forms.CharField(strip = False, 
                                    widget = forms.PasswordInput(attrs = {'class': 'input',
                                                                            'type': 'password',
                                                                            'autocomplete': 'new-password'
                                                                        }))


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'label', 'title', 'description', 'price', 'image', 'status']

class ItemImageForm(ModelForm):
    class Meta:
        model = ItemImage
        fields = ['image']