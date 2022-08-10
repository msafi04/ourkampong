
from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.http import HttpResponseBadRequest

from django.utils.html import format_html

from apps.direct.models import Message
from apps.member.models import Member
from apps.item.models import Item

@login_required
def inbox_view(request):
    messages = Message.get_messages(user = request.user)
    active_user = None
    directs = None

    if messages:
        message = messages[0]
        active_user = message['user'].username
        directs = Message.objects.filter(user = request.user, receiver = message['user'])
        directs.update(is_read = True)

        for message in messages:
            if message['user'].username == active_user:
                message['unread'] = 0
        
    context = {
        'directs': directs,
        'messages': messages,
        'active_user': active_user,
    }

    return render(request, 'direct/direct.html', context)

@login_required
def directs_view(request, username):
    user = request.user
    messages = Message.get_messages(user = user)
    active_user = username
    directs = Message.objects.filter(user = user, receiver__username = username)
    directs.update(is_read = True)

    for message in messages:
        if message['user'].username == username:
                message['unread'] = 0
    print('selected active_user - receiver: ', active_user)
    print('sender: ', user)
    context = {
        'directs': directs,
        'messages': messages,
        'active_user': active_user,   
    }

    return render(request, 'direct/direct.html', context)

@login_required
def send_directs(request):
    from_user = request.user
    to_user_username = request.POST.get('to_user')
    body = request.POST.get('body')

    if request.method == 'POST':
        to_user = Member.objects.get(username = to_user_username)
        Message.send_message(from_user, to_user, body)
        print('....send_directs....')
        print('FROM:', from_user)
        print('TO:', to_user)

        return redirect('inbox')
    else:
        HttpResponseBadRequest()

@login_required
def new_message(request, username, category_slug, item_slug):
    if request.user != username:
        #print(request.META.get('HTTP_REFERER')) #Link to the previous page visited
        from_user = request.user
        to_user = Member.objects.get(username = username)
        current_item = get_list_or_404(Item, cat_slug =  category_slug, slug = item_slug)
        body = format_html(f"<a href='{request.META.get('HTTP_REFERER')}' target='_blank'>View Item - {item_slug}</a>")

        Message.send_message(from_user, to_user, body)

        return redirect('inbox')

def check_messages(request):
    directs_count = 0
    if request.user.is_authenticated:
        directs_count = Message.objects.filter(user = request.user, is_read = False).count()

    return {'directs_count': directs_count}


