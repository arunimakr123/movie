from django.http import HttpResponse, request
from django.shortcuts import render, redirect

from. models import Movie
from. forms import MovieForm

# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={
        'movielist':movie
    }
    return render(request,'index.html',context)
def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':movie})

def add_movie(reduest):
    if request.method=="POST":
        name=reduest.POST.get('name')
        desc = reduest.POST.get('desc')
        year = reduest.POST.get('year')
        img = reduest.FILES['img']
        movie=Movie(name=name,desc=desc,year=year,img=img)
        movie.save()
    return render(reduest,'add.html')

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method=="POST":
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')