from django.urls import path

from .views import AllPostsView, PostView

urlpatterns = [
    path('', AllPostsView.as_view(), name='all_posts'),
    path('<int:pk>/', PostView.as_view(), name='single_post')
]
