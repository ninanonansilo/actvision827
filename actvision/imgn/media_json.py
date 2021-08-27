from settings.update_json import *



def img_list_in_bucket(bucket_name): # 버킷안에 저장된 이미지 리스트를 불러냄

    blobs = storage_client.list_blobs("ynu-mcl-act")
    list_blob = []

    except_str = str(user_id + "/IMAGE/")  # 제외시킬 문자열
    for blob in blobs:
        if blob.name.startswith(except_str):
            blob.name = blob.name.replace(except_str, '')
            if blob.name == '':
                pass
            else:
                list_blob.append(blob.name)

    return list_blob



def text_list_in_bucket(bucket_name): # 버킷안에 저장된 이미지 리스트를 불러냄

    blobs = storage_client.list_blobs("ynu-mcl-act")
    list_blob = []

    except_str = str(user_id + "/JSON/TEXT_LIST/")  # 제외시킬 문자열
    for blob in blobs:
        if blob.name.startswith(except_str):
            blob.name = blob.name.replace(except_str, '')
            if blob.name == '':
                pass
            else:
                list_blob.append(blob.name)

    return list_blob


def play_list_in_bucket(bucket_name): # 버킷안에 저장된 재생목록 이름들을 불러냄

    blobs = storage_client.list_blobs("ynu-mcl-act")
    list_blob = []

    except_str = str(user_id + "/PLAY_LIST/")  # 제외시킬 문자열
    for blob in blobs:
        if blob.name.startswith(except_str):
            blob.name = blob.name.replace(except_str, '')
            if blob.name == '':
                pass
            else:
                list_blob.append(blob.name)

    return list_blob


def video_list_in_bucket(bucket_name, index, list_name): # 재생목록안에 저장된 동영상 리스트를 불러냄

    blobs = storage_client.list_blobs("ynu-mcl-act")
    list_blob = []

    except_str = str(user_id + "/PLAY_LIST/" + list_name + "/")  # 제외시킬 문자열
    for blob in blobs:
        if blob.name.startswith(except_str):
            blob.name = blob.name.replace(except_str, '')
            if blob.name == '':
                pass
            else:
                list_blob.append(blob.name[14:])
    print(list_blob)
    return list_blob