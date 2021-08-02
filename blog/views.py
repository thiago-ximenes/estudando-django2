from django.shortcuts import render

posts = [
    {
        'author': 'ThiagoXL',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'July 30, 2021'
    },
    {
        'author': 'MiguelLX',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'July 29, 2021'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
