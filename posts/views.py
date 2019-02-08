"""Posts views module"""

#Djnago modules
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
#Utilities
from datetime import datetime
from posts.forms import PostForm
from posts.models import Post

class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all publishe posts"""

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 30
    context_object_name = 'data'

class PostDetailView(LoginRequiredMixin, DetailView):
    """Detail of a post"""
    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'

class CreatePostView(LoginRequiredMixin, CreateView):
    """Create new posts"""
    template_name = 'posts/new.html'
    form_class = PostForm
    seccess_url = reverse_lazy('feed')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile

        return context