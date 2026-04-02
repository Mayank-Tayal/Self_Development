from django.shortcuts import render, get_object_or_404
from datetime import date
# Create your views here.


from .models import Tag, Author, Post

all_posts = Post.objects.order_by('-date')


def starting_page(requests):
    
    return render(requests,"blog/index.html",{
        "posts": all_posts[:3]
    })


def posts(requests):
    return render(requests,"blog/all-blogs.html",{
        "all_posts":all_posts
    })


def post_detail(requests, slug):
    id_post = get_object_or_404(Post,slug=slug)
    return render(requests, "blog/post-detail.html",{
        # "post":id_post
        'title': id_post.title,
        'excerpt': id_post.excerpt,
        'image': id_post.image_name,
        'slug': id_post.slug,
        'author': id_post.author,
        'tags': id_post.tags.all(),
        'content': id_post.content,
        'date': id_post.date
    })
