from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Post


class AllPostsView(ListView):
    model = Post
    template_name = 'posts/all.html'
    context_object_name = 'all_posts_list'


class PostView(DetailView):
    model = Post
    template_name = 'posts/single_post.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/post_create.html'
    fields = ('title', 'text', 'author')


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/post_update.html'
    fields = ('title', 'text')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('all_posts')
