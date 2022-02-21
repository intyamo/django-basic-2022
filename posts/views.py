from django.views.generic import ListView

from .models import Post


class AllPostsView(ListView):
    model = Post
    template_name = 'posts/all.html'
    context_object_name = 'all_posts_list'
