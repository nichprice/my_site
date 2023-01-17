from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingAPageView.as_view(), name="starting-page"),
    path("all-posts/", views.AllPostsView.as_view(), name="all-posts"),
    path("posts/<slug:slug>/", views.SinglePostView.as_view(), name="blog-post") # blog post is a slug
]