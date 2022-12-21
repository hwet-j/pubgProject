
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotAllowed
from django.utils import timezone
import pandas as pd
import csv
from gamer.models import Matchlist, Matchdata
from django.core.paginator import Paginator     # 페이징을 위한 라이브러리
from MatchList.match_save import match_search_save

''' 초기 화면 설정 (제일 첫 화면) '''
def home(request):

    return render(request, 'main.html')


''' gamer 페이지의 첫 화면 '''
def index(request):
    page = request.GET.get('page', '1')  # 페이지
    match_list = Matchlist.objects.order_by('-create_date')     # 앞에 - 가 붙으면 내림 차순
    paginator = Paginator(match_list, 20)  # 페이지당 20개 씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'match_list' : page_obj}
    return render(request, 'gamer/home.html', context)


""" 저장된 csv 파일 불러오기 """
def csvRead(request):
    Matchlist.objects.all().delete()
    match_search_save(['Hwet_J', 'sickhu', '30XXDDD', 'hyeonji'])
    path = "C:/Users/HC/PycharmProjects/pubgProject/MatchList/datas/COMPETITIVE_MATCH.csv"
    file = open(path)
    reader = csv.reader(file)
    # print(reader)     # csv파일을 성공적으로 불러오는지 확인.
    list = []
    for count, row in enumerate(reader):
        if count == 0:      # 칼럼값 제외
            continue
        list.append(Matchlist(user_name = row[0],
                              create_date = row[1],
                              match_id = row[2]))
    Matchlist.objects.bulk_create(list)     # 리스트를 한번에 입력

    return redirect('/gamer/')

def detail(request, match_id):
    Matchdata.objects.all().delete()
    try:
        path = "C:/Users/HC/PycharmProjects/pubgProject/MatchList/datas/match_data/" + match_id +".csv"
        file = open(path)
        reader = csv.reader(file)
        # columns = [col for col in reader.fieldnames]
        # out = [row for row in reader]
        # print(out)
        # context = {'match_data': out}
        # return render(request, 'gamer/match_detail.html', context)

        list = []
        for count, row in enumerate(reader):
            if count == 0:  # 칼럼값 제외
                continue
            survived_time = str(int(row[20]) // 60) + "분 " + str(int(row[20]) % 60) + "초"
            duration_time = str(int(row[25]) // 60) + "분 " + str(int(row[25]) % 60) + "초"
            list.append(Matchdata(user_id=row[0],
                                  kill=row[1],
                                  headkill=row[2],
                                  longestkill=str(round(float(row[3]),2)),
                                  loadkill=row[4],
                                  teamkill=row[5],
                                  assist=row[6],
                                  damagedealt=str(round(float(row[7]),2)),
                                  damagetaken=str(round(float(row[8]),2)),
                                  dbno=row[9],
                                  revive=row[10],
                                  walkdistance=row[11],
                                  ridedistance=row[12],
                                  swimdistance=row[13],
                                  distance=str(round(float(row[14]),3)),
                                  boost=row[15],
                                  heal=row[16],
                                  deathtype=row[17],
                                  acquired=row[18],
                                  teammate=row[19],
                                  timesurvived=survived_time,
                                  ranking=row[21],
                                  map_name=row[22],
                                  game_created=row[23],
                                  game_mode=row[24],
                                  game_duration=duration_time,
                                  ))
        Matchdata.objects.bulk_create(list)
    except Exception as e:
        print(e)

    match_data = Matchdata.objects.order_by("teammate")
    # user_data = Matchdata.objects.filter("Hwet_J")
    context = {'match_data': match_data}
    return render(request, 'gamer/match_detail.html', context)


