from django.urls import path
from . import views  # from current folder import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),  # creating a name for simplicity purposes
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug>", views.post_detail, name="posts-detail-page")  # this is dynamic. /posts/my-first-post is
    # referred to as a slug
]
