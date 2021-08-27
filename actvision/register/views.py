from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    return render(request,'register.html')


def users_list(request): # 조회 버튼을 누르면 사용자 정보들을 불러옴 (사용자 = GCP 버켓 이름)

    return redirect('register.html')