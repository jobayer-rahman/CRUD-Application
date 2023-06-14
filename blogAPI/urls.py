from django.urls import path
from .views import (
    AuthorCreateListAPIView,
    AuthorUDAPIView,
    CommentCreateListAPIView,
    CommentUDAPIView,
    PostCreateListAPIView,
    PostUDAPIView,
)

urlpatterns = [
    path('author/', AuthorCreateListAPIView.as_view(), name="author-view"),
    path('author/<int:pk>/', AuthorUDAPIView.as_view(), name="author-ud"),
    path('post/', PostCreateListAPIView.as_view(), name="post-view"),
    path('post/<int:pk>/', PostUDAPIView.as_view(), name="post-ud"),
    path('comment/', CommentCreateListAPIView.as_view(), name="comment-view"),
    path('comment/<int:pk>/', CommentUDAPIView.as_view(), name="comment-ud"),
]
