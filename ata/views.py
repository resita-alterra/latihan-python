from django.shortcuts import render,redirect
from .forms import MentorForm, MenteeForm, BlogForm
from .models import Mentor, Mentee, Blog

# Create your views here.
def home(request):
    return render(request,'home.html')

def author(request):
    return render(request, 'author.html')

def mentor(request):
    mentor = Mentor.objects.all()
    return render(request, 'mentor.html', {'mentor' : mentor})

def inputmentor(request):
    if request.method == 'POST':
        form = MentorForm(request.POST)
        if form.is_valid():
            post =form.save(commit=False)
            post.save()
            redirect('mentor/')
    else:
        form = MentorForm()
    return render(request, 'inputmentor.html',{'form':form})

def mentee(request):
    mentee = Mentee.objects.all()
    return render(request, 'mentee.html', {'mentee' : mentee})

def inputmentee(request):
    if request.method == 'POST':
        form = MenteeForm(request.POST)
        if form.is_valid():
            post =form.save(commit=False)
            post.save()
            redirect('mentee/')
    else:
        form = MenteeForm()
    return render(request, 'inputmentor.html',{'form':form})


def blog(request):
    blog = Blog.objects.all()
    return render(request, 'blog.html', {'blog' : blog})

def inputblog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            post =form.save(commit=False)
            post.save()
            redirect('blog/')
    else:
        form = BlogForm()
    return render(request, 'inputblog.html',{'form':form})
    
def masukblog(request, id_blog):
    hasil = "blog"+str(id_blog)+".html"
    return render(request, hasil)