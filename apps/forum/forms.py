from dataclasses import field
from turtle import width
from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    content = forms.CharField(label = '', 
                                widget = forms.Textarea(attrs = {'placeholder': 'Add your comments here...', 
                                                                    'rows': 4, 'cols': 3}))
    class Meta:
        model = Comment
        fields = ['content']