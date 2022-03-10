from django.shortcuts import render

posts = [
    {
        'author': 'John2',
        'title': 'Title2',
        'content': 'Content2',
        'date_posted': 'Feb 22, 2022',
    },
    {
        'author': 'John',
        'title': 'Title',
        'content': 'Content',
        'date_posted': 'Feb 22, 2022',
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
