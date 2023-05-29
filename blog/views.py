from django.shortcuts import render

# Create your views here.


def home(request):
    context = {}
    blog_posts = [
        
        {
        'number':'#3', 
        'date':'2023 may 26', 
        'title': "AS IS - TO BE diagram", 
        'content': "",
        },{
        'number':'#2', 
        'date':'2023 may 26', 
        'title': "opc ua", 
        'content': "",
        },{
        'number':'#1', 
        'date':'2023 apr 10', 
        'title': "the central path", 
        'content': """in conventional contexts (e.g school, work) I sign a syllabys or contract with predefined rights and duties.
        what is my guding principle for the work i love to do? \n
        <i>automated data processing and information technology</i> \n
        the farther i stray from this phrase the more work feels like drudgery. 
        fair to say the word <b>automated</b> is carrying a lot of the weight.
        data processing is what humans do exeptionally well and information technology is becoming all-prevasive.
        """,
        'embed':"gewerbe.png"
        },
        {
        'number':'#0', 
        'date':'2023 feb 4', 
        'title': "my frist blog post", 
        'content': "hello, I'm abel and I'm trying to work in the IOT agriculture industry.",
        'embed':"blog_0.png"
        },
        
        #{'title': "#1   ", 'content': "this is my second blog post"},
    ]

    context['blog_posts'] = [blog_posts[-1]]


    return render(request, 'blog/home.html', context=context)