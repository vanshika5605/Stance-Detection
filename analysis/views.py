from django.shortcuts import render, redirect
from .models import Post
# Create your views here.

def display(request):
    posts = Post.objects.all()

    return render(request, "display.html", {'posts': posts})

def post(request):
    if request.method == 'POST':
        content=request.POST['content']
        target=request.POST['target']
        date=request.POST['date']
        img=request.POST['img']
        author=request.POST['author']

        post=Post(content=content, target=target, img=img, date_added=date, author=author)
        post.save()
        return redirect('/')
    else:
        return render(request, "addpost.html")