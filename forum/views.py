from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .models import Forum_post


class BlogListView(ListView):
    model = Forum_post
    template_name = 'forum.html'

class BlogDetailView(DetailView):
    model = Forum_post
    template_name = 'forum_detail.html'
    context_object_name = 'post_forum'

class BlogCreateView(CreateView):
    model = Forum_post
    #model.author = User.username
    template_name = 'post_new.html'
    fields = '__all__'
    #fields = ['title', 'text']