from django.urls import path
from . import views
from .views import (
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
    path("category/<int:pk>/", views.category_posts, name="category_posts"),

    path("post/new/", PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/edit/", PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
]

