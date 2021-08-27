from django.core import paginator
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']  # 로그인 시에는 유저이름과 비밀번호만 입력 받는다.


# Create your views here.
def login(request):
    return render(request, 'login.html')


def login_success(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home.html')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')
