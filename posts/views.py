# flake8: noqa
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib import messages
from .forms import CommentForm
from .models import Comment


class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"
    context_object_name = "posts"
    queryset = Post.objects.filter(is_public=True).order_by("-created_at")


class MyPostsView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "posts/my_posts.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user).order_by("-created_at")


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "posts/create_post.html"
    success_url = reverse_lazy("my_posts")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "posts/edit_post.html"
    success_url = reverse_lazy("my_posts")

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "posts/delete_post.html"
    success_url = reverse_lazy("my_posts")

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context["comments"] = post.comments.filter(is_deleted=False).order_by(
            "-created_at"
        )
        context["form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()

        if "delete_comment_id" in request.POST:
            comment_id = request.POST.get("delete_comment_id")
            comment = get_object_or_404(Comment, id=comment_id)
            if comment.user == request.user:
                comment.is_deleted = True
                comment.content = ""
                comment.save()
                messages.success(request, "Comment deleted successfully.")
            return redirect("post_detail", pk=post.pk)

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect("post_detail", pk=post.pk)

        context = self.get_context_data(form=form)
        return self.render_to_response(context)
