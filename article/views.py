from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ArticleForm,SongForm,MedsosForm
from .models import Article,Comment,Song,Medsos
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles":articles})
    articles = Article.objects.all()

    return render(request,"articles.html",{"articles":articles})
def index(request):
    facebooks = get_object_or_404(Medsos,nomer = 1)
    twitters =  get_object_or_404(Medsos,nomer = 2)
    youtubes =  get_object_or_404(Medsos,nomer = 3)
    instagrams =  get_object_or_404(Medsos,nomer = 4)
    apks =  get_object_or_404(Medsos,nomer = 5)

    pops = Song.objects.filter(tipe = 'pop')
    dangduts = Song.objects.filter(tipe = 'dangdut')
    mancas = Song.objects.filter(tipe = 'manca')
    # untuk tirticle di indexex.html
    articles = Article.objects.all()[:4]
    
    context = {
     "pops":pops,"dangduts":dangduts,"mancas":mancas,"articles":articles,"facebook":facebooks.link,"twitter":twitters.link
     ,"youtube":youtubes.link,"instagram":instagrams.link,"apk":apks.link
    }
    return render(request,"index.html",context)
    
def about(request):
    return render(request,"about.html")
@login_required(login_url = "user:login")



def dashboard(request):
    medsoss = Medsos.objects.all()
    articles = Article.objects.filter(author = request.user)
    pops = Song.objects.filter(tipe = 'pop')
    dangduts = Song.objects.filter(tipe = 'dangdut')
    mancas = Song.objects.filter(tipe = 'manca')
    print('hasil request :',request)
    context = {
        "articles":articles,"pops":pops,"dangduts":dangduts,"mancas":mancas,"medsoss":medsoss
    }
    return render(request,"dashboard.html",context)
@login_required(login_url = "user:login")


def dashboard_new(request,input):
    medsoss = Medsos.objects.all()    
    articles = Article.objects.filter(author = request.user)
    pops = Song.objects.filter(tipe = 'pop')
    dangduts = Song.objects.filter(tipe = 'dangdut')
    mancas = Song.objects.filter(tipe = 'manca')
    
    print('hasil request :',input)
    context = {
        "articles":articles,"pops":pops,"dangduts":dangduts,"mancas":mancas,"medsoss":medsoss,"tipe":input
    }
    return render(request,"dashboard.html",context)
@login_required(login_url = "user:login")







def addArticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        
        article.author = request.user
        article.save()

        messages.success(request,"Artikel berhasil dibuat")
        return redirect(reverse("article:dashboard_new",kwargs={"input":'article'}))
    return render(request,"addarticle.html",{"form":form})


def addSongPop(request):
    form = SongForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        song = form.save(commit=False)
        
        song.tipe = "pop"
        song.save()

        messages.success(request,"Tangga Lagu berhasil dibuat")
        return redirect(reverse("article:dashboard_new",kwargs={"input":'pop'}))
    return render(request,"addsong.html",{"form":form})

    


def addSongDangdut(request):
    form = SongForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        song = form.save(commit=False)
        
        song.tipe = "dangdut"
        song.save()

        messages.success(request,"Tangga Lagu berhasil dibuat")
        return redirect(reverse("article:dashboard_new",kwargs={"input":'dangdut'}))
    return render(request,"addsong.html",{"form":form})

 
def addSongManca(request):
    form = SongForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        song = form.save(commit=False)
        
        song.tipe = "manca"
        song.save()

        messages.success(request,"Tangga Lagu berhasil dibuat")
        return redirect(reverse("article:dashboard_new",kwargs={"input":'manca'}))
    return render(request,"addsong.html",{"form":form})       


    
def detail(request,id):
    #article = Article.objects.filter(id = id).first()   
    article = get_object_or_404(Article,id = id)

    comments = article.comments.all()
    return render(request,"detail.html",{"article":article,"comments":comments})
@login_required(login_url = "user:login")




def updateArticle(request,id):

    article = get_object_or_404(Article,id = id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance = article)
    if form.is_valid():
        article = form.save(commit=False)
        
        article.author = request.user
        article.save()

        messages.success(request,"Artikel berhasil diperbarui")
        return redirect(reverse("article:dashboard_new",kwargs={"input":'article'}))


    return render(request,"update.html",{"form":form})
@login_required(login_url = "user:login")

def updateSong(request,id):
    print('hasil id:',id)
    song = get_object_or_404(Song,id = id)   
    print('hasil tipe:',song.tipe)    

    form = SongForm(request.POST or None,request.FILES or None,instance = song)
    if form.is_valid():
        song = form.save(commit=False)
        
     #   song.author = request.user
        song.save()
  #      print('hasil post:',request.POST['tipe'])

        messages.success(request,"update tangga lagu berhasil diperbarui")
        return redirect(reverse("article:dashboard_new",kwargs={"input":song.tipe}))
    #  return redirect("http://localhost:8000/articles/dashboard/#dangdut")
    
    

    return render(request,"songupdate.html",{"form":form})
@login_required(login_url = "user:login")



def updateMedsos(request,id):
    print('hasil id:',id)
    medsos = get_object_or_404(Medsos,id = id)   
    
    form = MedsosForm(request.POST or None,request.FILES or None,instance = medsos)
    if form.is_valid():
        medsos = form.save(commit=False)
        
     #   song.author = request.user
        medsos.save()
  #      print('hasil post:',request.POST['tipe'])

       # messages.success(request,"update tangga lagu berhasil diperbarui")
        return redirect(reverse("article:dashboard_new",kwargs={"input":'setting'}))
    #  return redirect("http://localhost:8000/articles/dashboard/#dangdut")
    
    

    return render(request,"medsosupdate.html",{"form":form})
@login_required(login_url = "user:login")






def deleteArticle(request,id):
    article = get_object_or_404(Article,id = id)

    article.delete()

    messages.success(request,"Artikel Berhasil Dihapus")

    return redirect(reverse("article:dashboard_new",kwargs={"input":'article'}))

def deleteSong(request,id):
    song = get_object_or_404(Song,id = id)

    print(song)

    song.delete()

    messages.success(request,"Tangga Lagu Berhasil Dihapus")

    return redirect(reverse("article:dashboard_new",kwargs={"input":song.tipe}))

def addComment(request,id):
    article = get_object_or_404(Article,id = id)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author  = comment_author, comment_content = comment_content)

        newComment.article = article

        newComment.save()
    return redirect(reverse("article:detail",kwargs={"id":id}))
    
