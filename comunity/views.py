from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone   
from .models import Post
from login.models import Account
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

def main_comu(request):
    post = Post.objects
    text = ""
    if request.user.is_authenticated:
        txt_prime =Account.objects.get(user=request.user)
        text = txt_prime.nickname + "님 안녕하세요!"
    else:
        text="로그인해주세요"
    return render(request, 'main_comunity.html', {"post":post, "txt": text})

def post(request):
    return render(request, 'post.html')

def create(request):
    post = Post()
    post.title = request.GET['title']
    post.writer = request.GET['writer']
    post.body = request.GET['body']
    post.date = timezone.datetime.now()
    post.img = request.GET['img']
    post.save()
    return redirect('http://127.0.0.1:8000/comunity')

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {"post":post_detail})

def delete(request):
    del_id = request.GET['blogNm']
    post = Post.objects.get(id=del_id)
    post.delete()
    return redirect('main')

def edit_page(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'edit_page.html', {"post":post_detail})
    

def edit(request, post_id):
    edit_id = request.GET['blogNm']
    post = Post.objects.get(id=edit_id)
    post.title = request.GET['title']
    post.writer = request.GET['writer']
    post.body = request.GET['body']
    post.date = timezone.datetime.now()
    post.img = request.GET['img']
    post.save()
    return redirect('comunity')
    
# Create your views here.
