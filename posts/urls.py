from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("my_posts/", views.my_posts, name="my_posts"),
    path("create/", views.create_post, name="create_post"),
    path("edit/<int:post_id>/", views.edit_post, name="edit_post"),
    path("delete/<int:post_id>/", views.delete_post, name="delete_post"),
    path("post/<int:post_id>/", views.post_detail, name="post_detail"),
]
