from django.urls import path

from .views import AllPostsView, PostView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', AllPostsView.as_view(), name='all_posts'),
    path('<int:pk>/', PostView.as_view(), name='single_post'),
    path('new/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
