from django.shortcuts import render

# Create your views here.


def home(request):
    context = {}
    blog_posts = [
        {'title': "#0 my frist blog post", 'content': "this is my first blog post"},
        #{'title': "#1   ", 'content': "this is my second blog post"},
    ]

    context['blog_posts'] = blog_posts


    return render(request, 'blog/home.html', context=context)