import re, os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import get_object_or_404

from django.contrib import messages

from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.utils.text import slugify

from django.db.models import Q 

from .forms import MemberCreationForm, MemberChangeForm
from .models import Member

from apps.item.models import Item
from apps.forum.models import Post

from .forms import ItemForm, ItemImageForm


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
    posts_num = member.posts.all().count()

    postal_code_map = {
        '01': "Raffles Place, Cecil, Marina, People's Park", '02': "Raffles Place, Cecil, Marina, People's Park", '03': "Raffles Place, Cecil, Marina, People's Park", 
        '04': "Raffles Place, Cecil, Marina, People's Park", '05': "Raffles Place, Cecil, Marina, People's Park", '06': "Raffles Place, Cecil, Marina, People's Park",

        '07': "Anson, Tanjong Pagar", '08': "Anson, Tanjong Pagar", 
        
        '09': "Telok Blangah, Harbourfront", '10': "Telok Blangah, Harbourfront",

        '11': "Pasir Panjang, Hong Leong Garden, Clementi New Town", '12': "Pasir Panjang, Hong Leong Garden, Clementi New Town", 
        '13': "Pasir Panjang, Hong Leong Garden, Clementi New Town", 

        '14': "Queenstown, Tiong Bahru", '15': "Queenstown, Tiong Bahru", '16': "Queenstown, Tiong Bahru",

        '17': "High Street, Beach Road (part)", 
        
        '18': "Middle Road, Golden Mile", '19': "Middle Road, Golden Mile", 
        
        '20': "Little India", '21': "Little India",

        '22': "Orchard, Cairnhill, River Valley", '23': "Orchard, Cairnhill, River Valley", 
        
        '24': "Ardmore, Bukit Timah, Holland Road, Tanglin", '25': "Ardmore, Bukit Timah, Holland Road, Tanglin", '26': "Ardmore, Bukit Timah, Holland Road, Tanglin",
        '27': "Ardmore, Bukit Timah, Holland Road, Tanglin"

    }

    postal_sector = member.postal_code[:2]
    member.location = postal_code_map[postal_sector]
    member.save()

    return render(request, 'member/member_admin.html', {'member': member, 'items': items, 
                                                        'num_shares': range(member.share_badge), 
                                                        'num_donates': range(member.donate_badge),
                                                        'num_posts': posts_num
                                                        })

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

@login_required
def edit_item(request, pk):
    member = request.user.username
    item = get_object_or_404(Item, id = pk)

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance = item) #instance parameter should be given for populating the fields with existing data

        if form.is_valid():
            print('EDIT FORM')
            form.save()
            messages.success(request, 'Your Item was successfully updated!')

            return redirect('member/member_admin.html')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ItemForm(instance = item)

    return render(request, 'member/edit_item.html', {'form': form, 'item': item})

@login_required
def edit_user(request, pk):
    member = get_object_or_404(Member, id = pk)

    if request.method == 'POST':
        form = MemberChangeForm(request.POST, request.FILES, instance = member)

        if form.is_valid():
            form.save()
            messages.success(request, 'User Info was successfully updated!')

            return redirect('member/member_admin.html')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = MemberChangeForm(instance = member)
        
    return render(request, 'member/edit_user.html', {'form': form})

@login_required
def donation_view(request):
    user = request.user

    return render(request, 'member/donate.html', {'user': user})

@login_required
def donate_badges(request):
    user = request.user
    user.donate_badge += 1
    user.save()

    return redirect('member/donate.html')





