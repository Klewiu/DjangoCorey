from django.shortcuts import render
from .models import Post
posts = [
    {
        'author':'CoreyMS',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'August 27, 2021'
    },
    {
        'author':'Jane Doe',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted':'August 28, 2021'
    }

]

def home(request): #definiujemy funkcje home która będzie domyslnie otwierana na stronie
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request): #definiujemy funkcje about
    return render(request, 'blog/about.html', {'title': 'About'}) # przekazujemy tytył strony jako dictionary

