import pandas as pd
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator     # 페이징을 위한 라이브러리
import csv
from rank.models import PersonalData
from MatchList.django_apply.main import dakggCrawling, predict_one
from rank.forms import ArticleForm
import json


''' 페이지의 첫 화면 '''
def index(request):
    all_match_data = PersonalData.objects.all()
    page = request.GET.get('page', '1')  # 페이지
    paginator = Paginator(all_match_data, 10)  # 페이지당 20개 씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'PersonalData': page_obj}

    return render(request, "rank/rank_home.html", context)

""" 아이디, 플랫폼을 입력받아 데이터를 크롤링하는 작업 및 전체 정보 불러오기 """
def readData(request):
    import os
    import time
    all_match_data = PersonalData.objects.all().values()
    df = pd.DataFrame(all_match_data)

    try:
        df_all = df.drop(columns=['id'])
    except:
        df_all = pd.DataFrame()

    if request.method == "POST":
        name = request.POST['title']
        user_platform = request.POST['select']

    path = "C:/Users/ghlck/PycharmProjects/pubg/MatchList/django_apply/datas/" + name + ".csv"
    all_path = "C:/Users/ghlck/PycharmProjects/pubg/MatchList/django_apply/datas/db_save.csv"
    if os.path.isfile(path):
        # 파일이 존재하면 크롤링 작업을 하지 않도록 설정했지만 이후에 게임을 더 한다면
        # 크롤링 작업이 필요하다.
        # dakggCrawling(name, user_platform)
        df_load = pd.read_csv(path)
        df_all = pd.concat([df_all, df_load], ignore_index=True)
        df_all.drop_duplicates(inplace=True)
        df_all.to_csv(all_path, index=False)
        time.sleep(0.5)

        file = open(all_path, encoding="UTF8")
        reader = csv.reader(file)
    else:
        dakggCrawling(name, user_platform)
        df_load = pd.read_csv(path)
        df_all = pd.concat([df_all, df_load], ignore_index=True)
        df_all.drop_duplicates(inplace=True)
        df_all.to_csv(all_path, index=False)
        time.sleep(0.5)

        file = open(all_path, encoding="UTF8")
        reader = csv.reader(file)

    PersonalData.objects.all().delete()
    # print(reader)     # csv파일을 성공적으로 불러오는지 확인.

    list = []
    for count, row in enumerate(reader):
        if count == 0:
            continue
        list.append(PersonalData(
        user_id =           row[0],
        dbnos =             row[1],
        assists =           row[2],
        boosts =            row[3],
        damage_dealt =      row[4],
        headshot_kills =    row[5],
        heals =             row[6],
        kills =             row[7],
        longest_kill =      row[8],
        revives =           row[9],
        total_distance =    row[10],
        ride_distance =     row[11],
        road_kills =        row[12],
        swim_distance =     row[13],
        vehicle_destroys =  row[14],
        time_survived =     row[15],
        walk_distance =     row[16],
        weapons_acquired =  row[17],
        team_count =        row[18],
        map_name =          row[19],
        duration =          row[20],
        win_place =         row[21]
        ))

    PersonalData.objects.bulk_create(list)  # 리스트를 한번에 입력
    match_data = PersonalData.objects.filter(user_id=name)
    page = request.GET.get('page', '1')  # 페이지
    paginator = Paginator(match_data, 10)  # 페이지당 20개 씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'PersonalData': page_obj}
    return render(request, "rank/rank_home.html", context)


def predict_rank(request, id):
    match_data = PersonalData.objects.filter(id=id).values()
    # object = get_object_or_404(match_data)

    print(match_data[0]['win_place'])
    context = {
        'id' : match_data[0]['id'],
        'pre_ranking' : match_data[0]['win_place']
    }
    return render(request, 'rank/rank_home.html', context)
    # return JsonResponse(data)
    # 같은 홈페이지에 머물기
    # return redirect(request.META.get("HTTP_REFERER", 'redirect_if_referer_not_found'))

# ajax 코드 작성 필요.. json 형식 전송까지 완료ㅇㄱ쇼ㅕ8
def likes(request):
    print("dd")
    if request.META.get("HTTP_X_REQUESTED_WITH") == 'XMLHttpRequest':  # ajax 방식일 때 아래 코드 실행
        # id = request.GET['id']  # 좋아요를 누른 게시물id (blog_id)가지고 오기
        # post = PersonalData.objects.get(id=id)
        # print(post)
        message = "좋아요 취소"
        print("asdf")
        '''user = request.user  # request.user : 현재 로그인한 유저
        if post.like.filter(id=user.id).exists():  # 이미 좋아요를 누른 유저일 때
            post.like.remove(user)  # like field에 현재 유저 추가
            message = "좋아요 취소"  # 화면에 띄울 메세지
        else:  # 좋아요를 누르지 않은 유저일 때
            post.like.add(user)  # like field에 현재 유저 삭제
            message = "좋아요"  # 화면에 띄울 메세지
        # post.like.count() : 게시물이 받은 좋아요 수'''
        context = {'like_count': 1, "message": message}
        return HttpResponse(json.dumps(context), content_type='application/json')