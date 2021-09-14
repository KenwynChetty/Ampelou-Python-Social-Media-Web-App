from django.urls import path
from .views import (PostListView, PostDetailView,
                    PostUpdateView, PostDeleteView, UserPostListView,
                    FollowsListView, FollowersListView)
from blog import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('video/', views.video, name='video-pg'),
    path('business/', views.business, name='business-pg'),
    path('post/new/', views.create_post, name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(),
         name='post-update'),
    path('post/<int:pk>/del/', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>/follows',
         FollowsListView.as_view(),
         name='user-follows'),
    path('user/<str:username>/followers',
         FollowersListView.as_view(),
         name='user-followers'),
    path('post/<int:postid>/preference/<int:userpreference>',
         views.postpreference,
         name='postpreference'),
]