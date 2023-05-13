from django.shortcuts import render

# Create your views here.


def home(request):
    context = {}
    blog_posts = [
        {
        'number':'#0', 
        'title': "my frist blog post", 
        'content': "integrations are where the money is at. "
        },
        {
        'number':'#1', 
        'title': "defining a central path", 
        'content': "it's goot to have guding documents even if just in the context of this blog. this is mine.",
    
        },
        #{'title': "#1   ", 'content': "this is my second blog post"},
    ]

    context['blog_posts'] = blog_posts


    return render(request, 'blog/home.html', context=context)