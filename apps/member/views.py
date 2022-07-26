import re
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

from django.contrib import messages

from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.utils.text import slugify

from .forms import MemberCreationForm
from .models import Member

from apps.item.models import Item
from .forms import ItemForm

def register_member(request):
    if request.method == 'POST':
        form = MemberCreationForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            
            messages.success(request, 'Registration Successful for ' + user)

            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below!')
        
    else:
        form = MemberCreationForm()
    
    return render(request, 'member/register_member.html', {'form': form})

@login_required
def member_admin(request):
    member = request.user
    items = member.items.all()
    return render(request, 'member/member_admin.html', {'member': member, 'items': items})

@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit = False)
            item.member = request.user
            item.slug = slugify(item.title)
            item.cat_slug = slugify(item.category)
            item.save()

            return redirect('member/member_admin.html')
    else:
        form = ItemForm()

    return render(request, 'member/add_item.html', {'form': form})

@login_required
def delete_item(request, pk):
    #print(Item.objects.filter(id = pk)[0].member)
    if request.user == Item.objects.filter(id = pk)[0].member:
        Item.objects.filter(id = pk).delete()
        messages.success(request, 'Item Removed Successfully!!')
    else:
        messages.info(request, 'You are not authorized to delete this Item!!')

    return redirect('member/member_admin.html')
