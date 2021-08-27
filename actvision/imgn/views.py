from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from settings.update_json import *
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from imgn.make_timetable import *
from PIL import ImageColor
from imgn.media_json import *
import unicodedata
import base64
from urllib import parse
import numpy as np
#from django.utils import simplejson
# Create your views here.

def imgn(request):  # 페이지 로딩시 리스트에 이미지, 문자 올림
    img_list = img_list_in_bucket(user_id)  # 버켓안에 최신파일 이름 받아옴
    print("현재 저장된 이미지 목록->")
    print(img_list) # 저장된 이미지 리스트
    img_time_list = []
    img_name_list = []
    for i in range(len(img_list)): # img_list에서 시간이랑 이미지 이름 분리
        len_t = int(img_list[i][14]) # (지속시간 길이)
        img_time_list.append(str(img_list[i][15: 14 + len_t+1])) # 파일 이름 앞에 지속시간 분리 (첫자리 제외)
        img_name_list.append(str(img_list[i][14 + len_t+1:])) # 나머지 파일이름 따로 저장


    text_list = text_list_in_bucket(user_id)


    print("현재 저장된 문자 목록->")
    print(text_list) # 저장된 문자 리스트
    text_list_trans = []
    for i in range(len(text_list)):
        text_list_trans.append(text_list[i][14:])


    list_dict = {
        'img_name' : img_name_list,
        'img_time' : img_time_list,
        'text' : text_list_trans,
    }
    context = json.dumps(list_dict)
    return render(request, 'image.html', {'context': context})

@csrf_exempt
def upload_img(request):
    print("호출 성공")
    if request.method == 'POST':
        if request.is_ajax():

            stay_time = request.POST['time']    # 지속시간
            img_name = request.POST['img_name']  # 이미지 이름
            print(stay_time)
            img = request.FILES.get('img')  # 이미지를 request에서 받아옴
            path = default_storage.save(user_id +"/img.jpg", ContentFile(img.read()))
            now_kst = time_now()
            UPLOAD("ynu-mcl-act", user_id + "/img.jpg", user_id + "/IMAGE/" + now_kst.strftime("%Y%m%d%H%M%S") + str(len(stay_time)) + str(stay_time) + img_name)
            os.remove(user_id+"/img.jpg") # 장고에서 중복된 이름의 파일에는 임의로 이름을 변경하기 때문에 임시파일은 제거
            return redirect('image.html')
        else:
            print("ajax 통신 실패!")
            return redirect('image.html')
    else:
        print("POST 호출 실패!")
        return redirect('image.html')

@csrf_exempt
def save_letter(request): # 문자 설정 -> 확인 버튼 눌렀을 시 // 버켓 안 TEXT_LIST 디렉토리에 업로드하여 저장 (TIMETABLE을)
    if request != "":
        print("========= 시작 ===========")


        print("요청 방식 = " + request.method)
        print(request.encoding)
        print(request.body)

        change = request_body_list_text(request.body)
        change[9] = parse.unquote(change[9])

        data = make_Timetable_text()
        now_kst = time_now_local()  # 현재시간 받아옴
        now_kst1 = time_now()
        now_kst += 15

        data[4]["detail_info"]["x"] = str(change[1])
        data[4]["detail_info"]["y"] = str(change[2])
        data[4]["detail_info"]["width"] = str(change[3])
        data[4]["detail_info"]["height"] = str(change[4])
        data[4]["detail_info"]["play_speed"] = str(change[5])
        data[4]["detail_info"]["play_count"] = str(change[6])
        data[4]["detail_info"]["font_size"] = "64"     # 폰트사이즈 - 인터페이스 수정 전까지 고정시킴
        data[4]["detail_info"]["scroll_fix"] = str(change[10])
        data[4]["detail_info"]["play_second"] = str(change[11])
        data[4]["title"] = str(change[0])
        hex = str("#" + change[8])
        rgb_value = ImageColor.getcolor(hex,"RGB")
        data[4]["detail_info"]["red_green_blue"] = str(rgb_value)

        data[4]["time"]["year"] = str(time.localtime(now_kst).tm_year)
        data[4]["time"]["month"] = str(time.localtime(now_kst).tm_mon)
        data[4]["time"]["day"] = str(time.localtime(now_kst).tm_mday)
        data[4]["time"]["hour"] = str(time.localtime(now_kst).tm_hour)
        data[4]["time"]["minute"] = str(time.localtime(now_kst).tm_min)
        data[4]["time"]["second"] = str(time.localtime(now_kst).tm_sec)

        if (str(change[10]) == '0'):
            title = str(change[0])
            len_text = len(title)
            all_text_pixel = int(0.9 * int(len_text) * int(data[4]["detail_info"]["font_size"])) - int(change[3])
            micro_second = (all_text_pixel * 100) / int(change[5]) # 100 is ms
            ans = np.rint((micro_second / 1000) * int(change[6]))
            now_kst = now_kst + 15 + ans
        elif (str(change[10]) == '1'):
            now_kst += 15 + int(change[11])
        else:
            print("스크롤-고정 선택 오류")
            return redirect('image.html')

        createDirectory(user_id)
        save_file(data)
        UPLOAD("ynu-mcl-act", user_id+"/send" , user_id + "/JSON/TEXT_LIST/" + now_kst1.strftime("%Y%m%d%H%M%S") + str(change[9]))

        return redirect('image.html')
    else:
        return redirect('image.html')


@csrf_exempt
def event_trans(request):    # 이벤트 전송 버튼 TEXT_LIST에서 선택된 TIMETABLE을 JSON/TIMETABLE로 전송
    check_list_text = value_of_request_body_list(request.body) # 선택된 파일 인덱스
    print(check_list_text)

    blobs = storage_client.list_blobs("ynu-mcl-act")
    list_blob = []
    i = 0
    except_str = str(user_id + "/JSON/TEXT_LIST/")  # 제외시킬 문자열
    for blob in blobs:
        if blob.name.startswith(except_str):
            i += 1
            blob.name = blob.name.replace(except_str, '')
            list_blob.append(blob.name)
    call_file = [] # 업로드할 파일
    j = 0
    for index in range(20):
        if check_list_text[index] != '': # 체크된 인덱스
            if len(list_blob) > index : # 이미 업로드된 범위 내의 체크
                call_file.append(list_blob[index])
                j += 1
        else:
            pass
    print(call_file) # 선택된 파일이름들

    for k in range(len(call_file)):
        now_kst = time_now()  # 현재시간 받아옴
        copy_blob("ynu-mcl-act", user_id + "/JSON/TEXT_LIST/" + call_file[k], user_id + "JSON/TIMETABLE"+ now_kst.strftime("/%Y%m%d%H%M%S"))

    return redirect('image.html')

