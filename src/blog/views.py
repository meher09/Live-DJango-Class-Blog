from django.shortcuts import render, get_object_or_404
from .models import Post, Category

from rest_framework import viewsets
from .serializers import PostSerializer

# Create your views here.
def home(request):
    posts = Post.objects.filter(status ='publish')
    template_name = 'blog/home.html'
    context = {'posts':posts}
    return render(request,template_name, context )


def category_details(request, category_slug):
    category_url = get_object_or_404(Category, slug = category_slug )
    posts = Post.objects.filter(category = category_url, status = 'publish' )
    template_name = 'blog/category-details.html'
    context = {'posts':posts}
    return render(request, template_name, context)


def post_details(request, post_slug):
    post = get_object_or_404(Post, slug = post_slug, status = 'publish')
    return render(request, 'blog/blog-details.html', {'post':post})


def handler404(request, exception):
    return render(request, '404.html', status=404)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
