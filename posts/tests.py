# flake8: noqa
# from django.test import TestCase
# from django.urls import reverse
# from django.contrib.auth import get_user_model
# from django.contrib.messages import get_messages
# from .models import Post, Comment

# User = get_user_model()


# class PostTests(TestCase):
#     def setUp(self):
#         # Users
#         self.user1 = User.objects.create_user(
#             username="alice", email="a@x.com", password="pass1234"
#         )
#         self.user2 = User.objects.create_user(
#             username="bob", email="b@x.com", password="pass1234"
#         )
#         # Public and private posts
#         self.public_post = Post.objects.create(
#             user=self.user1, title="Public Post", content="pub", is_public=True
#         )
#         self.private_post = Post.objects.create(
#             user=self.user1, title="Private Post", content="priv", is_public=False
#         )

#     # --- Visibility tests ---
#     def test_public_feed_shows_only_public(self):
#         resp = self.client.get(reverse("post_list"))
#         self.assertContains(resp, "Public Post")
#         self.assertNotContains(resp, "Private Post")

#     def test_private_post_not_visible_to_others(self):
#         self.client.login(username="bob", password="pass1234")
#         resp = self.client.get(
#             reverse("post_detail", kwargs={"post_id": self.private_post.id})
#         )
#         self.assertEqual(resp.status_code, 302)

#     def test_owner_can_view_private(self):
#         self.client.login(username="alice", password="pass1234")
#         resp = self.client.get(
#             reverse("post_detail", kwargs={"post_id": self.private_post.id})
#         )
#         self.assertEqual(resp.status_code, 200)
#         self.assertContains(resp, "Private Post")

#     # --- Login  ---
#     def test_my_posts_requires_login(self):
#         resp = self.client.get(reverse("my_posts"))
#         self.assertEqual(resp.status_code, 302)
#         self.assertIn("/login", resp.url)

#     # --- CRUD  ---
#     def test_create_post(self):
#         self.client.login(username="alice", password="pass1234")
#         resp = self.client.post(
#             reverse("create_post"),
#             {"title": "New Post", "content": "Content", "is_public": True},
#             follow=True,
#         )
#         self.assertEqual(resp.status_code, 200)
#         self.assertTrue(Post.objects.filter(title="New Post").exists())

#     def test_edit_post(self):
#         self.client.login(username="alice", password="pass1234")
#         resp = self.client.post(
#             reverse("edit_post", kwargs={"post_id": self.public_post.id}),
#             {"title": "Updated Post", "content": "Updated", "is_public": True},
#             follow=True,
#         )
#         self.assertEqual(resp.status_code, 200)
#         self.public_post.refresh_from_db()
#         self.assertEqual(self.public_post.title, "Updated Post")

#     def test_delete_post(self):
#         self.client.login(username="alice", password="pass1234")
#         resp = self.client.post(
#             reverse("delete_post", kwargs={"post_id": self.public_post.id}),
#             follow=True,
#         )
#         self.assertEqual(resp.status_code, 200)
#         self.assertFalse(Post.objects.filter(id=self.public_post.id).exists())

#     # --- Comment tests---
#     def test_delete_comment_message(self):
#         self.client.login(username="alice", password="pass1234")
#         comment = Comment.objects.create(
#             post=self.public_post, user=self.user1, content="Nice post!"
#         )
#         resp = self.client.post(
#             reverse("post_detail", kwargs={"post_id": self.public_post.id}),
#             {"delete_comment_id": comment.id},
#             follow=True,
#         )
#         messages = list(get_messages(resp.wsgi_request))
#         texts = [m.message for m in messages]
#         self.assertIn("Comment deleted successfully.", texts)
