from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from settings.update_json import *
from imgn.media_json import *
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
# Create your views here.

check_index = -1

def movie(request):
    play_list = directory_list()
    list_name = []
    list_date = []

    for i in range(len(play_list)):
        list_date.append(play_list[i][0:4] + '-' + play_list[i][4:6] + '-' + play_list[i][6:8] + ' (' + play_list[i][8:10] +':' +
                         play_list[i][10:12] +')') # 앞에 14자리 - 등록일
        list_name.append(play_list[i][14:])

    print("현재 등록된 재생목록->")
    print(list_name)  # 저장된 이미지 리스트

    global check_index
    list_index = int(check_index)
    media_list = []
    if (list_index != -1): # 체크된 상태라면 -> 해당 재생목록의 동영상들을 가져오기
        if list_index >= len(play_list):
            pass
        else:
            param_play_list_name = play_list[list_index]
            media_list = video_list_in_bucket(user_id, check_index, param_play_list_name)

    list_dict = {
        'list_name': list_name,  # 재생목록 -> 이름
        'list_date': list_date,  # 재생목록 -> 등록일
        'list_index': list_index,  # 체크 -> 인덱스
        'list_media': media_list,  # 선택된 재생목록 내 동영상
    }

    print("재생목록 내 동영상 리스트->")
    print(media_list)


    context = json.dumps(list_dict)
    return render(request, 'mov.html', {'context': context})


@csrf_exempt
def video_list(request):
    temp = request.POST['index']
    print(temp)


    global check_index
    check_index = temp

    return render(request, 'mov.html')
    #return redirect('movie.html')




@csrf_exempt
def upload_list(request):  # 재생목록 추가 ( GCP에 해당하는 이름의 디렉토리를 만듬)
    if request.method == 'POST':
        if request.is_ajax():
            print(request.POST['list'])    # 리스트 이름
            input = request.POST['list']
            list_name = input # 임시방편
            # -- 업로드 , 이런식으로 하면 오류 없이 디렉토리 생성가능
            now_kst = time_now()  # 현재시간 받아옴
            UPLOAD("ynu-mcl-act", 'test' , user_id + "/PLAY_LIST/" + now_kst.strftime("%Y%m%d%H%M%S") + str(list_name) + "/")
            return redirect('movie.html')
        else:
            print("ajax 통신 실패!")
            return redirect('movie.html')
    else:
        print("POST 호출 실패!")
        return redirect('movie.html')



def directory_list():   # 디렉토리가 '/'로 끝나는 특징을 사용해 디렉토리 이름만 추출
    play_list_name = play_list_in_bucket("ynu-mcl-act")  # 중복 확인을 위해 PLAY_LIST 하위 이름들의 배열
    list_name = []
    for i in range(len(play_list_name)):
        if play_list_name[i][-1:] == '/':
            list_name.append(play_list_name[i][:-1])
    return list_name


@csrf_exempt
def upload_video(request):  # 재생목록에 동영상 업로드
    if request.method == 'POST':
        if request.is_ajax():

            video_name = request.POST['video_name']  # 동영상 이름
            play_list_index = int(request.POST['list_name']) # 재생목록 인덱스
            if (play_list_index == -1):  # 재생목록이 선택되지 않은 상태라면 저장하지 않음
                return redirect('movie.html')
            video = request.FILES.get('video')  # 동영상을 request에서 받아옴
            path = default_storage.save(user_id + "/video", ContentFile(video.read()))
            play_list = directory_list()
            checked_play_list = play_list[play_list_index]
            now_kst = time_now()  # 현재시간 받아옴
            UPLOAD("ynu-mcl-act", user_id + "/video",user_id + "/PLAY_LIST/" + checked_play_list + now_kst.strftime("/%Y%m%d%H%M%S") + video_name)
            os.remove(user_id + "/video")  # 장고에서 중복된 이름의 파일에는 임의로 이름을 변경하기 때문에 임시파일은 제거
            return redirect('movie.html')
        else:
            print("ajax 통신 실패!")
            return redirect('movie.html')
    else:
        print("POST 호출 실패!")
        return redirect('movie.html')


@csrf_exempt
def delete_play_list(request):  # 선택된 재생목록 삭제
    if request.method == 'POST':
        if request.is_ajax():

            delete_index = int(request.POST['play_list_index'])
            play_list = directory_list()
            if (delete_index >= len(play_list)):
                pass
            else:
                delete_name = play_list[delete_index]
                delete_blob("ynu-mcl-act", user_id + "/PLAY_LIST/" + delete_name + "/")

            return redirect('movie.html')
        else:
            print("ajax 통신 실패!")
            return redirect('movie.html')
    else:
        print("POST 호출 실패!")
        return redirect('movie.html')


@csrf_exempt
def delete_video(request):  # 선택된 재생목록 삭제
    if request.method == 'POST':
        if request.is_ajax():

            # 구현 마저하시오


            return redirect('movie.html')
        else:
            print("ajax 통신 실패!")
            return redirect('movie.html')
    else:
        print("POST 호출 실패!")
        return redirect('movie.html')