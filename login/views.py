from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Account

def login(request):
    if request.method == 'POST':
        input_id = request.POST['input_id']
        password = request.POST['password']
        user = auth.authenticate(request, username=input_id, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            messages.info(request, "일치하는 정보가 없어요")
            return redirect('login')

    else:
        return render(request,'login.html')
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        user_id = request.POST.get('id')
        pw1 = request.POST.get('password1')
        pw2 = request.POST.get('password2')
        email = request.POST.get('email')
        nickname = request.POST.get('nickname')

        if user_id == "" or pw1 == "" or pw2 == "" or email == "" or nickname == "":
            messages.info(request, "빈칸을 채워주시오.")
            return redirect("signup")

        if pw1 != pw2 :
            messages.info(request, "비밀번호 달라요.")
            return redirect("signup")

        user = User.objects.create_user(username=user_id, password= pw1)
        user.save()
        account = Account(user=user, email=email, nickname=nickname)
        account.save()
        return redirect('signup')
    else:
        return render(request, 'signup.html')

    return render(request, 'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('main')
# Create your views here.
