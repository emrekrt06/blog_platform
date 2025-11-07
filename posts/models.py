# flake8: noqa
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# import User from django's built-in auth models

# Create your models here.


class Post(models.Model):
    """Represents a blog post created by a user.
    Attributes:
        user (User): The author of the post. When the user is deleted, their posts are also deleted.
        title (str): The title of the post, limited to 200 characters.
        content (str): The main text content of the post.
        visibility (str): Determines whether the post is public or private.
        created_at (datetime): The date and time when the post was created.
        updated_at (datetime): The date and time when the post was last modified.
    Meta:
        ordering (list): Orders posts by creation date in descending order, showing the newest posts first.
    Methods:
        __str__(): Returns the title of the post as its string representation.
    """

    VISIBILITY_CHOICES = [
        ("public", "Public"),
        ("private", "Private"),
    ]
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name=_("Author"),
    )  # Author of the post
    title = models.CharField(
        max_length=200, verbose_name=_("Title")
    )  # Title of the post
    content = models.TextField(verbose_name=_("Content"))  # Main content of the post
    visibility = models.CharField(
        max_length=10,
        choices=VISIBILITY_CHOICES,
        default="public",
        verbose_name=_("Visibility"),
    )  # Visibility status
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Created at")
    )  # Timestamp when created
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_("Updated at")
    )  # Timestamp when last updated
    is_public = models.BooleanField(
        default=True, verbose_name=_("Is public")
    )  # Public or private flag

    class Meta:
        ordering = ["-created_at"]  # Newest posts first
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title  # String representation of the post


class Comment(models.Model):
    """Represents a comment made by a user on a blog post.
    Attributes:
        post (Post): The blog post that the comment is associated with.
        user (User): The author of the comment.
        content (str): The text content of the comment.
        created_at (datetime): The date and time when the comment was created.
    Methods:
        __str__(): Returns a string representation of the comment,
        including the author's username and the post title.
    """

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments", verbose_name=_("Post")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
    content = models.TextField(verbose_name=_("Content"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    is_deleted = models.BooleanField(default=False, verbose_name=_("Deleted"))

    class Meta:
        ordering = ["created_at"]
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return f"{self.user.username} → {self.post.title}"
