from ast import Delete
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from posts.models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
class PostListView(ListView):
    template_name = 'posts/list.html'
    model = Post

class PostDetailView(DetailView):
    template_name = 'posts/detail.html'
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'posts/new.html'
    model = Post
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        

class PostUpdateView(LoginRequiredMixin, UpdateView, UserPassesTestMixin):
    template_name = 'posts/edit.html'
    model = Post
    fields = ['title', 'body']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class PostDeleteView(LoginRequiredMixin, DeleteView, UserPassesTestMixin):
    template_name = 'posts/delete.html'
    model = Post
    success_url = reverse_lazy('post_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user