from django.views.generic import ListView, DetailView

from .models import Post


class AllPostsView(ListView):
    model = Post
    template_name = 'posts/all.html'
    context_object_name = 'all_posts_list'


class PostView(DetailView):
    model = Post
    template_name = 'posts/single_post.html'
