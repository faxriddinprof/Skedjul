from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Post
from django import forms
# Create your views here.


class Homepageview(ListView):
    model = Post
    template_name = "home.html"


class BlogCreateview(CreateView):
    model = Post
    template_name='post_create.html'
    fields=['title','author','text','holati']


class BlogDetailview(DetailView):
    model=Post
    template_name='post_detail.html'

class BlogUpdateview(UpdateView):
    model=Post
    template_name='post_update.html'
    fields=['title','text','holati']
    success_url=reverse_lazy('home')

class BlogDeleteview(DeleteView):
    model=Post
    template_name='post_delete.html'
    success_url=reverse_lazy('home')

    