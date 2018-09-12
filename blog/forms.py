from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    """class creating a form"""
    class Meta:
        model = Post
        fields = ('title', 'text')