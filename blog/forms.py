from .models import Post, Comment
from django import forms
from django_summernote.widgets import SummernoteWidget


# Note: the code has been used from the CI tutorial
# I Think Therefore I Blog
# to help the setup and creation of this project.


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('likes',)
        widgets = {
            'content': SummernoteWidget(),
        }

    class Meta:
        model = Post
        fields = fields = (
            'title',
            'slug',
            'excerpt',
            'content',
            'status'
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)