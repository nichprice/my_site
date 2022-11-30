from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("all-posts/", views.posts, name="all-posts"),
    path("posts/<slug:slug>/", views.blog_post, name="blog-post") # blog post is a slug
]