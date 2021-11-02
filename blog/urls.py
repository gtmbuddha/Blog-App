from django.urls import path
from .views import HomeView, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('/post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('/post/create', PostCreateView.as_view(), name = 'post_create'),
    path('/post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('/post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
]