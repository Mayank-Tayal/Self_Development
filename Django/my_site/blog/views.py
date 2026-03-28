from django.shortcuts import render

# Create your views here.


def starting_page(requests):
    return render(requests,"blog/index.html")


def posts(requests):
    return render(requests,"blog/all-blogs.html")


def post_detail(requests, slug):
    return render(requests, "blog/post-detail.html")
