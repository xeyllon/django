from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView,DeleteView
from .models import Blog

class PostListView(ListView):
    queryset = Blog.objects.all()
    template_name = 'list.html'