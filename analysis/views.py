from django.shortcuts import render, redirect
from .models import Post
import pandas as pd
# Create your views here.

def display(request):
    posts = Post.objects.all()
    sarcasm_model=pd.read_pickle(r'C:\Users\HP\MinorProject\minor\models\SarcasmDetection\model.pkl')
    stance_model=pd.read_pickle(r'C:\Users\HP\MinorProject\minor\models\StanceDetection\stance.pkl')
    vectorizer=pd.read_pickle(r'C:\Users\HP\MinorProject\minor\models\SarcasmDetection\tfidf.pkl')
    for post in posts:
        s=[]
        s.append(post.content)
        data=vectorizer.transform(s).toarray()
        result1=sarcasm_model.predict(data)
        if result1:
            post.sarcasm="Yes"
        else:
            post.sarcasm="No"
        result2=stance_model.predict(s)
        post.stance=result2[0]
        post.save()

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
        return redirect('/analysis')
    else:
        return render(request, "addpost.html")