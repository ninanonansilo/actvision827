import json

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from settings.update_json import *
from django.contrib import messages
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from PIL import ImageColor

#from django.utils import simplejson
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

import cgitb; cgitb.enable()

@csrf_exempt
def check(request): #이전 설정값 확인
    print("========= 설정값 체크 시작 ===========")
    if request != "":
        recently_file_name = list_blobs(user_id)
        DOWNLOAD("ynu-mcl-act", user_id + "/JSON/READALL/" + recently_file_name, user_id + "/temp")  # 버켓 속 최신파일 -> user_id/temp 임시파일로 불러옴
        setting = read_json()  # 임시파일에서 불러온 json
        print(setting)
        sudonglight = setting['Brightness_Control']['Brightness']
        print(sudonglight)
        now_kst = time_now()  # 현재시간 받아옴

        setting["Time"] = {}
        setting["Time"]["year"] = now_kst.strftime("%Y")
        setting["Time"]["month"] = now_kst.strftime("%m")
        setting["Time"]["day"] = now_kst.strftime("%d")

        setting["Time"]["hour"] = now_kst.strftime("%H")
        setting["Time"]["minute"] = now_kst.strftime("%M")
        setting["Time"]["second"] = now_kst.strftime("%S")


        #######################################################
        print("========= 설정값 체크 종료 ===========")
        print(sudonglight)
        a = json.dumps(sudonglight)

        return render(request, 'settings.html', {a})
    else:
        # return HttpResponse("ERROR: POST방식으로 전송됨")
        return redirect('settings.html')

# Create your views here.
def settings(request):
    return render(request,'settings.html')

@csrf_exempt
def check_pattern(request):
    print("========= 시작 ===========")
    if request != "":
        change = value_of_request_body(request.body)
        print(str(change))
        recently_file_name = list_blobs(user_id)
        createDirectory(user_id)
        DOWNLOAD("ynu-mcl-act", user_id + "/JSON/READALL/" + recently_file_name, user_id + "/temp")
        setting = read_json()  # 임시파일에서 불러온 json
        setting['Pattern'] = str(change)
        now_kst = time_now()  # 현재시간 받아옴
        setting["Time"] = {}
        setting["Time"]["year"] = now_kst.strftime("%Y")
        setting["Time"]["month"] = now_kst.strftime("%m")
        setting["Time"]["day"] = now_kst.strftime("%d")

        setting["Time"]["hour"] = now_kst.strftime("%H")
        setting["Time"]["minute"] = now_kst.strftime("%M")
        setting["Time"]["second"] = now_kst.strftime("%S")
        save_file(setting)
        UPLOAD("ynu-mcl-act", user_id + "/send", user_id + "/JSON/READALL" + now_kst.strftime("/%Y%m%d%H%M%S"))
        print("========= 종료 ===========")
        return redirect('settings.html')
    else:
# return HttpResponse("ERROR: POST방식으로 전송됨")
        return redirect('settings.html')

@csrf_exempt
def check_Brightness_mode(request):
    print("========= 시작 ===========")
    if request != "":
        change = value_of_request_body(request.body)
        print(request.body)
        print(str(change))
        recently_file_name = list_blobs(user_id)
        createDirectory(user_id)
        DOWNLOAD("ynu-mcl-act", user_id + "/JSON/READALL/" + recently_file_name, user_id + "/temp")
        setting = read_json()  # 임시파일에서 불러온 json
        setting['Brightness_Control']['Mode'] = str(change)
        now_kst = time_now()  # 현재시간 받아옴
        setting["Time"] = {}
        setting["Time"]["year"] = now_kst.strftime("%Y")
        setting["Time"]["month"] = now_kst.strftime("%m")
        setting["Time"]["day"] = now_kst.strftime("%d")

        setting["Time"]["hour"] = now_kst.strftime("%H")
        setting["Time"]["minute"] = now_kst.strftime("%M")
        setting["Time"]["second"] = now_kst.strftime("%S")
        save_file(setting)
        UPLOAD("ynu-mcl-act", user_id + "/send", user_id + "/JSON/READALL" + now_kst.strftime("/%Y%m%d%H%M%S"))
        print("========= 종료 ===========")
        return redirect('settings.html')
    else:
# return HttpResponse("ERROR: POST방식으로 전송됨")
        return redirect('settings.html')

@csrf_exempt
def check_Brightness_mode_auto_time(request):
    print("========= 시작 ===========")
    if request != "":
        change = value_of_request_body(request.body)
        print(request.body)
        print(str(change))
        recently_file_name = list_blobs(user_id)
        createDirectory(user_id)
        DOWNLOAD("ynu-mcl-act", user_id + "/JSON/READALL/" + recently_file_name, user_id + "/temp")
        setting = read_json()  # 임시파일에서 불러온 json
        setting['Brightness_Control']['Mode'] = str(change)
        now_kst = time_now()  # 현재시간 받아옴
        setting["Time"] = {}
        setting["Time"]["year"] = now_kst.strftime("%Y")
        setting["Time"]["month"] = now_kst.strftime("%m")
        setting["Time"]["day"] = now_kst.strftime("%d")

        setting["Time"]["hour"] = now_kst.strftime("%H")
        setting["Time"]["minute"] = now_kst.strftime("%M")
        setting["Time"]["second"] = now_kst.strftime("%S")
        save_file(setting)
        UPLOAD("ynu-mcl-act", user_id + "/send", user_id + "/JSON/READALL" + now_kst.strftime("/%Y%m%d%H%M%S"))
        print("========= 종료 ===========")
        return redirect('settings.html')
    else:
# return HttpResponse("ERROR: POST방식으로 전송됨")
        return redirect('settings.html')


@csrf_exempt
def check_Brightness_mode_auto_CDS(request):
    print("========= 시작 ===========")
    if request != "":
        change = value_of_request_body(request.body)
        print(request.body)
        print(str(change))
        recently_file_name = list_blobs(user_id)
        createDirectory(user_id)
        DOWNLOAD("ynu-mcl-act", user_id + "/JSON/READALL/" + recently_file_name, user_id + "/temp")
        setting = read_json()  # 임시파일에서 불러온 json
        setting['Brightness_Control']['Mode'] = str(change)
        now_kst = time_now()  # 현재시간 받아옴

        setting["Time"] = {}
        setting["Time"]["year"] = now_kst.strftime("%Y")
        setting["Time"]["month"] = now_kst.strftime("%m")
        setting["Time"]["day"] = now_kst.strftime("%d")

        setting["Time"]["hour"] = now_kst.strftime("%H")
        setting["Time"]["minute"] = now_kst.strftime("%M")
        setting["Time"]["second"] = now_kst.strftime("%S")

        save_file(setting)
        UPLOAD("ynu-mcl-act", user_id + "/send", user_id + "/JSON/READALL" + now_kst.strftime("/%Y%m%d%H%M%S"))
        print("========= 종료 ===========")
        return redirect('settings.html')
    else:
# return HttpResponse("ERROR: POST방식으로 전송됨")
        return redirect('settings.html')

@csrf_exempt
def update_Brightness(request): # 밝기 업데이트2
    print("========= 시작 ===========")
    if request != "":
        print("요청 방식 = " + request.method)
        print("input = " + value_of_request_body(request.body))
########################################################
        change = value_of_request_body(request.body) # input값 받아옴
        recently_file_name = list_blobs(user_id) # 버켓안에 최신파일 이름 받아옴
        print("버켓 최신 파일 이름 ->")
        print(recently_file_name)
        createDirectory(user_id) # user_id (시리얼포트)로 디렉토리로 만들고 temp 파일 생성, 이미 생성시 패스
        DOWNLOAD("ynu-mcl-act" , user_id + "/JSON/READALL/" + recently_file_name, user_id +"/temp") # 버켓 속 최신파일 -> user_id/temp 임시파일로 불러옴
        setting = read_json() # 임시파일에서 불러온 json
        setting['Brightness_Control']['Brightness'] = str(change)
        now_kst = time_now()  # 현재시간 받아옴
        setting["Time"] = {}
        setting["Time"]["year"] = now_kst.strftime("%Y")
        setting["Time"]["month"] = now_kst.strftime("%m")
        setting["Time"]["day"] = now_kst.strftime("%d")

        setting["Time"]["hour"] = now_kst.strftime("%H")
        setting["Time"]["minute"] = now_kst.strftime("%M")
        setting["Time"]["second"] = now_kst.strftime("%S")
        save_file(setting)
        UPLOAD("ynu-mcl-act", user_id+"/send" , user_id + "/JSON/READALL" + now_kst.strftime("/%Y%m%d%H%M%S"))
#######################################################
        print("========= 종료 ===========")
        return redirect('settings.html')
    else:
        #return HttpResponse("ERROR: POST방식으로 전송됨")
        return redirect('settings.html')


@csrf_exempt
def update_CDS_Value(request): # 밝기 업데이트2
    print("========= 시작 ===========")
    if request != "":

        print("요청 방식 = " + request.method)
        print("input = " + value_of_request_body(request.body))
########################################################
        change = value_of_request_body(request.body) # input값 받아옴
        print(" 조도값 : {}".format(change))

################################################################
        recently_file_name = list_blobs(user_id) # 버켓안에 최신파일 이름 받아옴
        print("버켓 최신 파일 이름 ->")
        print(recently_file_name)
        createDirectory(user_id) # user_id (시리얼포트)로 디렉토리로 만들고 temp 파일 생성, 이미 생성시 패스
        DOWNLOAD("ynu-mcl-act" , user_id + "/JSON/READALL/" + recently_file_name, user_id +"/temp") # 버켓 속 최신파일 -> user_id/temp 임시파일로 불러옴
        setting = read_json() # 임시파일에서 불러온 json
        setting['Brightness_Control']['CDS_Value'] = str(change)
        now_kst = time_now()  # 현재시간 받아옴
        setting["Time"] = {}
        setting["Time"]["year"] = now_kst.strftime("%Y")
        setting["Time"]["month"] = now_kst.strftime("%m")
        setting["Time"]["day"] = now_kst.strftime("%d")

        setting["Time"]["hour"] = now_kst.strftime("%H")
        setting["Time"]["minute"] = now_kst.strftime("%M")
        setting["Time"]["second"] = now_kst.strftime("%S")
        save_file(setting)
        UPLOAD("ynu-mcl-act", user_id+"/send" , user_id + "/JSON/READALL" + now_kst.strftime("/%Y%m%d%H%M%S"))
#######################################################
        print("========= 종료 ===========")
        return redirect('settings.html')
    else:
        #return HttpResponse("ERROR: POST방식으로 전송됨")
        return redirect('settings.html')


@csrf_exempt
def update_min_max(request):
    change = value_of_request_body_list(request.body) # 4개의 input 값
########################################################
    recently_file_name = list_blobs(user_id)  # 버켓안에 최신파일 이름 받아옴
    print("버켓 최신 파일 이름 ->")
    print(recently_file_name)
    createDirectory(user_id)  # user_id (시리얼포트)로 디렉토리로 만들고 temp 파일 생성, 이미 생성시 패스
    DOWNLOAD("ynu-mcl-act" , user_id + "/JSON/READALL/" + recently_file_name, user_id +"/temp") # 버켓 속 최신파일 -> user_id/temp 임시파일로 불러옴
    setting = read_json()  # 임시파일에서 불러온 json

    setting['Brightness_Control']['Auto_Brightness'] = {}
    setting['Brightness_Control']['Auto_Brightness']['min'] = str(change[0])
    setting['Brightness_Control']['Auto_Brightness']["max"] = str(change[1])

    setting['Brightness_Control']['Auto_CDS'] = {}
    setting['Brightness_Control']['Auto_CDS']["min"] = str(change[2])
    setting['Brightness_Control']['Auto_CDS']["max"] = str(change[3])


    now_kst = time_now()  # 현재시간 받아옴
    setting["Time"] = {}
    setting["Time"]["year"] = now_kst.strftime("%Y")
    setting["Time"]["month"] = now_kst.strftime("%m")
    setting["Time"]["day"] = now_kst.strftime("%d")

    setting["Time"]["hour"] = now_kst.strftime("%H")
    setting["Time"]["minute"] = now_kst.strftime("%M")
    setting["Time"]["second"] = now_kst.strftime("%S")
    save_file(setting)
    UPLOAD("ynu-mcl-act", user_id+"/send" , user_id + "/JSON/READALL" + now_kst.strftime("/%Y%m%d%H%M%S"))
#######################################################

    return redirect('settings.html')

@csrf_exempt
def power_mode(request):
    print("========= 시작 ===========")
    if request != "":
        change = value_of_request_body(request.body)
        print(request.body)
        print(str(change))
        recently_file_name = list_blobs(user_id)
        createDirectory(user_id)
        DOWNLOAD("ynu-mcl-act", user_id + "/JSON/READALL/" + recently_file_name, user_id + "/temp")
        setting = read_json()  # 임시파일에서 불러온 json
        setting['Power_Control']['Mode'] = str(change)
        now_kst = time_now()  # 현재시간 받아옴
        setting["Time"] = {}
        setting["Time"]["year"] = now_kst.strftime("%Y")
        setting["Time"]["month"] = now_kst.strftime("%m")
        setting["Time"]["day"] = now_kst.strftime("%d")

        setting["Time"]["hour"] = now_kst.strftime("%H")
        setting["Time"]["minute"] = now_kst.strftime("%M")
        setting["Time"]["second"] = now_kst.strftime("%S")
        save_file(setting)
        UPLOAD("ynu-mcl-act", user_id + "/send", user_id + "/JSON/READALL" + now_kst.strftime("/%Y%m%d%H%M%S"))
        print("========= 종료 ===========")
        return redirect('settings.html')
    else:
        # return HttpResponse("ERROR: POST방식으로 전송됨")
        return redirect('settings.html')


@csrf_exempt
def manual_control(request):
    print("========= 시작 ===========")
    if request != "":
        change = value_of_request_body(request.body)
        print(request.body)
        print(str(change))
        recently_file_name = list_blobs(user_id)
        createDirectory(user_id)
        DOWNLOAD("ynu-mcl-act", user_id + "/JSON/READALL/" + recently_file_name, user_id + "/temp")
        setting = read_json()  # 임시파일에서 불러온 json
        setting['Power_Control']['Manual_ONOFF'] = str(change)
        now_kst = time_now()  # 현재시간 받아옴
        setting["Time"] = {}
        setting["Time"]["year"] = now_kst.strftime("%Y")
        setting["Time"]["month"] = now_kst.strftime("%m")
        setting["Time"]["day"] = now_kst.strftime("%d")

        setting["Time"]["hour"] = now_kst.strftime("%H")
        setting["Time"]["minute"] = now_kst.strftime("%M")
        setting["Time"]["second"] = now_kst.strftime("%S")
        save_file(setting)
        UPLOAD("ynu-mcl-act", user_id + "/send", user_id + "/JSON/READALL" + now_kst.strftime("/%Y%m%d%H%M%S"))
        print("========= 종료 ===========")
        return redirect('settings.html')
    else:
        # return HttpResponse("ERROR: POST방식으로 전송됨")
        return redirect('settings.html')

@csrf_exempt
def update_on_off(request):
    print("========= 시작 ===========")
    if request != "":
        change = value_of_request_body(request.body)
        print(request.body)
        print(str(change))
        recently_file_name = list_blobs(user_id)
        createDirectory(user_id)
        DOWNLOAD("ynu-mcl-act", user_id + "/JSON/READALL/" + recently_file_name, user_id + "/temp")
        setting = read_json()  # 임시파일에서 불러온 json

        setting['Power_Control']['Auto_ON'] = {}
        setting['Power_Control']['Auto_ON']['min'] = str(change[0])
        setting['Power_Control']['Auto_ON']['max'] = str(change[1])
        setting['Power_Control']['Auto_OFF'] = {}
        setting['Power_Control']['Auto_OFF']['min'] = str(change[2])
        setting['Power_Control']['Auto_OFF']['max'] = str(change[3])

        now_kst = time_now()  # 현재시간 받아옴
        setting["Time"] = {}
        setting["Time"]["year"] = now_kst.strftime("%Y")
        setting["Time"]["month"] = now_kst.strftime("%m")
        setting["Time"]["day"] = now_kst.strftime("%d")

        setting["Time"]["hour"] = now_kst.strftime("%H")
        setting["Time"]["minute"] = now_kst.strftime("%M")
        setting["Time"]["second"] = now_kst.strftime("%S")
        save_file(setting)
        UPLOAD("ynu-mcl-act", user_id + "/send", user_id + "/JSON/READALL" + now_kst.strftime("/%Y%m%d%H%M%S"))
        print("========= 종료 ===========")
        return redirect('settings.html')
    else:
        # return HttpResponse("ERROR: POST방식으로 전송됨")
        return redirect('settings.html')


