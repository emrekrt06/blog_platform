from django.urls import path
from .views import (
    PostListView,
    MyPostsView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostDetailView,
)

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("my_posts/", MyPostsView.as_view(), name="my_posts"),
    path("create/", PostCreateView.as_view(), name="create_post"),
    path("edit/<int:pk>/", PostUpdateView.as_view(), name="edit_post"),
    path("delete/<int:pk>/", PostDeleteView.as_view(), name="delete_post"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
]
