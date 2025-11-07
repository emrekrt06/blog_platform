# flake8: noqa
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib import messages


def post_list(request):
    """Renders the list of public blog posts.
    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: Renders the post list template that are public.
    """
    posts = Post.objects.filter(is_public=True).order_by("-created_at")
    return render(request, "posts/post_list.html", {"posts": posts})


@login_required
def my_posts(request):
    """Renders the list of blog posts created by the logged-in user.
    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: Renders the user's posts template.
    """
    posts = Post.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "posts/my_posts.html", {"posts": posts})


@login_required
def create_post(request):
    """Handles the creation of a new blog post by the logged-in user.
    Parameters:
        request (HttpRequest): The HTTP request object containing form data.
    Returns:
        HttpResponse: Renders the create post template or redirects to
        the user's posts page on successful creation.
    """
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("my_posts")
    else:
        form = PostForm()
    return render(request, "posts/create_post.html", {"form": form})


@login_required
def edit_post(request, post_id):
    """Handles editing an existing blog post by the logged-in user.
    Parameters:
        request (HttpRequest): The HTTP request object containing form data.
        post_id (int): The ID of the post to be edited.
    Returns:
        HttpResponse: Renders the edit post template or redirects to
        the user's posts page on successful update.
    """
    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("my_posts")
    else:
        form = PostForm(instance=post)
    return render(request, "posts/edit_post.html", {"form": form, "post": post})


@login_required
def delete_post(request, post_id):
    """Handles deletion of a blog post by the logged-in user.
    Parameters:
        request (HttpRequest): The HTTP request object.
        post_id (int): The ID of the post to be deleted.
    Returns:
        HttpResponse: Renders the delete confirmation template or
        redirects to the user's posts page on successful deletion.
    """
    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method == "POST":
        post.delete()
        return redirect("my_posts")
    return render(request, "posts/delete_post.html", {"post": post})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Restrict access to private posts
    if not post.is_public and post.user != request.user:
        return redirect("post_list")

    comments = post.comments.filter(is_deleted=False).order_by("-created_at")

    # Handle new comment submission
    if request.method == "POST" and "delete_comment_id" not in request.POST:
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.user = request.user
                comment.save()
                return redirect("post_detail", post_id=post.id)
        else:
            return redirect("login")

    # Handle comment deletion (mark as deleted instead of removing)
    elif request.method == "POST" and "delete_comment_id" in request.POST:
        comment_id = request.POST.get("delete_comment_id")
        comment = get_object_or_404(Comment, id=comment_id)
        if comment.user == request.user:
            comment.is_deleted = True
            comment.content = ""  # Optional: clear the content
            comment.save()
            messages.success(request, "Comment deleted successfully.")
        return redirect("post_detail", post_id=post.id)

    else:
        form = CommentForm()

    return render(
        request,
        "posts/post_detail.html",
        {"post": post, "comments": comments, "form": form},
    )
