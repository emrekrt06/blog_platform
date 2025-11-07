# flake8: noqa
from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """Form for creating and editing blog posts.
    Attributes:
        title (str): The title of the blog post.
        content (str): The main text content of the blog post.
        is_public (bool): A checkbox to set the post as public or private.
    Meta:
        model (Post): The Post model that this form is creating/editing.
        fields (list): The list of model fields included in the form: title, content, is_public.
    """

    class Meta:
        model = Post
        fields = ["title", "content", "is_public"]


class CommentForm(forms.ModelForm):
    """Form for adding comments to blog posts.
    Attributes:
        content (str): The text content of the comment.
    Meta:
        model (Comment): The Comment model that this form is creating/editing.
        fields (list): The list of model fields included in the form: content.
        widgets (dict): Custom widgets for form fields, including a textarea
        for the content field with specified rows and placeholder text.
    """

    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(
                attrs={"rows": 3, "placeholder": "Write a comment..."}
            ),
        }
