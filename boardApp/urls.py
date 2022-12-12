from django.urls import path
from .views import (AdListView, AdDetailView, CreateAdCreateView, AdUpdateView, AdDeleteView, CommentAdCreateView,
                    MyCommentsListView, CommentDeleteView)

urlpatterns = [
    path('', AdListView.as_view(), name='index'),
    path('ad/<int:pk>', AdDetailView.as_view(), name='ad-detail'),
    path('ad/<int:pk>/comment/', CommentAdCreateView.as_view(), name='ad-comment'),
    path('create-ad/', CreateAdCreateView.as_view(), name='create-ad'),
    path('ad/<int:pk>/edit/', AdUpdateView.as_view(), name='edit-ad'),
    path('ad/<int:pk>/delete/', AdDeleteView.as_view(), name='delete-ad'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete-comment'),
    path('comments/', MyCommentsListView.as_view(), name='my-comments'),
]