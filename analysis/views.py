from django.shortcuts import render, redirect
from .models import Post
import pandas as pd
# Create your views here.

def display(request):
    posts = Post.objects.all()
    sentiment_model=pd.read_pickle(r'C:\Users\HP\MinorProject\minor\models\SentimentAnalysis\sentiment.pkl')
    sarcasm_model=pd.read_pickle(r'C:\Users\HP\MinorProject\minor\models\SarcasmDetection\model.pkl')
    vectorizer=pd.read_pickle(r'C:\Users\HP\MinorProject\minor\models\SarcasmDetection\tfidf.pkl')
    stance_model=pd.read_pickle(r'C:\Users\HP\MinorProject\minor\models\StanceDetection\stance.pkl')
   
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
        result3=sentiment_model.predict(s)
        post.stance=result2[0]
        if result3:
            post.sentiment="Positive"
        else:
            post.sentiment="Negative"
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

def report(request):
    posts = Post.objects.all()
    #favor,none,against
    targets = {'Atheism': [0, 0, 0], 'Climate Change is a real concern': [0, 0, 0],'Feminist Movement': [0, 0, 0],'Hillary Clinton': [0, 0, 0],'Legalization of Abortion': [0, 0, 0]}
    for post in posts:
        for t in targets.keys():
            if post.target==t:
                if post.stance=='FAVOR':
                    targets[t][0]=targets[t][0]+1
                elif post.stance=='NONE':
                    targets[t][1]=targets[t][1]+1
                else:
                    targets[t][2]=targets[t][2]+1
    #ans={'Atheism': 0, 'Climate Change is a real concern': 0,'Feminist Movement': 0,'Hillary Clinton': 0,'Legalization of Abortion': 0}
    for t in targets.keys():
        temp=targets[t][0]+targets[t][1]+targets[t][2]
        if temp==0:
            pass
        else:
            targets[t][0]=(targets[t][0]/temp)*100
            targets[t][1]=(targets[t][1]/temp)*100
            targets[t][2]=(targets[t][2]/temp)*100
    temp=['In Favor', 'Neither', 'Against']
    return render(request, "report.html",{'targets':targets,'temp':temp})