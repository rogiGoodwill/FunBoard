from django.urls import path
from .views import IndexListView, CreateAdCreateView

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('create-ad/', CreateAdCreateView.as_view(), name='create-ad'),
]