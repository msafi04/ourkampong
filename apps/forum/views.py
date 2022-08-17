from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect

from django.contrib import messages
from django.core.paginator import Paginator

from .models import Post
from.forms import PostForm, CommentForm

@login_required
def post_create_view(request):
    my_posts = Post.objects.filter(member = request.user)

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            instance = form.save(commit = False)
            instance.member = request.user
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()

    return render(request, 'forum/post_new.html', {'form': form, 'my_posts': my_posts})

@login_required
def post_delete_view(request, pk):
    if request.user == Post.objects.filter(id = pk)[0].member:
        Post.objects.filter(id = pk).delete()
        messages.success(request, 'Post Removed Successfully!!')
    else:
        messages.warning(request, 'You are not authorized to delete this Post!!')

    return redirect('post_list')

def posts_list_view(request):
    all_posts = Post.objects.all()
    page_posts = Paginator(all_posts, 3)
    page_list = request.GET.get('page')
    page_posts = page_posts.get_page(page_list)

    if request.user.is_authenticated:
        my_posts = Post.objects.filter(member = request.user)
        return render(request, 'forum/post_list.html', {'page_posts': page_posts, 'my_posts': my_posts})
    else:
        return render(request, 'forum/post_list.html', {'page_posts': page_posts})

def post_detail_view(request, pk):
    post = get_object_or_404(Post, id = pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            instance = form.save(commit = False)
            instance.user = request.user
            instance.post = post
            instance.save()

            return redirect('post_detail', pk = post.pk)
    else:
        form = CommentForm()

    return render(request, 'forum/post_detail.html', {'post': post, 'form': form})

def post_likes_view(request, pk):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))
    if request.user.is_authenticated:
        if request.user in post.post_likes.all():
            post.post_likes.remove(request.user)
        else:
            post.post_likes.add(request.user)
    else:
        messages.info(request, 'Please login to Like the Post!!')

    return HttpResponseRedirect(reverse('post_detail', args = [str(pk)]))