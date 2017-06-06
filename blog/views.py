# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from blog.models import Post, Comment


def home(request):
    template_name = 'blog/home.html'
    posts = Post.objects.all()
    for i in posts:
        i.content = i.content[0:100] + "..."
    context = {'object_list': posts}
    return render(request, template_name, context)


def post_detail(request, id):
    template_name = "blog/post.html"
    post = Post.objects.get(id=int(id))
    comments = Comment.objects.filter(post=post)
    context = {'post': post, 'comments': comments}
    return render(request, template_name, context)