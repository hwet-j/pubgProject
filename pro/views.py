from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from pro.models import PgcList, MatchData, Video
from django.core.paginator import Paginator     # 페이징을 위한 라이브러리
import csv

''' 초기 화면 설정 (제일 첫 화면) '''
def home(request):
    return render(request, 'main.html')

''' 페이지의 첫 화면 '''
def index(request):
    page = request.GET.get('page', '1')  # 페이지
    match_list = PgcList.objects.order_by('-create_date')     # 앞에 - 가 붙으면 내림 차순
    paginator = Paginator(match_list, 20)  # 페이지당 20개 씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'PgcList' : page_obj}
    return render(request, 'pro/home.html', context)


""" 저장된 csv 파일 불러오기 """
def csvRead(request):
    PgcList.objects.all().delete()

    path = "C:/Users/HC/PycharmProjects/pubgProject/MatchList/datas/pgc/PGC_MATCH.csv"
    file = open(path)
    reader = csv.reader(file)
    print(reader)     # csv파일을 성공적으로 불러오는지 확인.
    list = []
    for count, row in enumerate(reader):
        if count == 0:      # 칼럼값 제외
            continue
        list.append(PgcList(tournament_type = row[0],
                            match_id = row[1],
                            create_date = row[2]))
    PgcList.objects.bulk_create(list)     # 리스트를 한번에 입력

    MatchData.objects.all().delete()
    path2 = "C:/Users/HC/PycharmProjects/pubgProject/MatchList/datas/pgc/MATCH_ALL_STAT.csv"
    file2 = open(path2)
    reader2 = csv.reader(file2)
    print(reader2)
    list2 = []
    for count, row in enumerate(reader2):
        if count == 0:
            continue
        list2.append(MatchData(
        match_id       = row[25]     ,#매치 아이디
        created_at     = row[26]     ,#게임 생성시간
        user_name      = row[11]     ,#유저명
        kill           = row[9]      ,#킬수
        headkill       = row[5]      ,#헤드샷 킬수
        longestkill    = round(float(row[10]),2)    ,#킬 최대거리
        loadkill       = row[15]     ,#로드킬
        teamkill       = row[17]     ,#팀킬
        assist         = row[1]      ,#도움 횟수
        damagedealt    = round(float(row[3]),2)      ,#총 입힌 데미지
        damagetaken    = round(float(row[23]),2)    ,#총 입은 데미지
        dbno           = row[0]      ,#부활 횟수
        revive         = row[13]     ,#부활 시킨 횟수
        walkdistance   = row[20]     ,#걸은 거리
        ridedistance   = row[14]     ,#차량 이동 거리
        swimdistance   = row[16]     ,#수영 이동 거리
        distance       = round(float(row[20])+float(row[14])+float(row[16]),2)    ,#총 이동 거리
        boost          = row[2]      ,#부스트 아이탬 사용 횟수
        heal           = row[6]      ,#체력 회복 아이탬 사용 횟수
        deathtype      = row[4]      ,#죽음 종류
        acquired       = row[21]     ,#무기 습득 횟수
        team_member    = row[31]     ,#팀원
        team_name      = row[24]     ,#팀이름
        team_kill      = row[33]     ,#팀 총 킬수
        team_assist    = row[34]     ,#팀 총 어시스트
        team_distance  = row[35]     ,#팀 평균 이동 거리
        team_damagedealt  = round(float(row[36]),2)  ,#팀 총 가한 데미지
        team_damagetaken  = round(float(row[37]),2)  ,#팀 총 입은 데미지
        team_timesurvived = row[38]  ,#팀 평균 생존 시간
        timesurvived      = row[18]  ,#생존 시간
        ranking           = row[22]  ,#등수
        vehicle_destroys  = row[19]  ,#차량 파괴 횟수
        map_name          = row[27]  ,#맵이름
        game_duration     = row[28]  ,#게임 지속 시간
        ))
    MatchData.objects.bulk_create(list2)  # 리스트를 한번에 입력

    return redirect('/pro/')


def detail(request, match_id):
    match_data = MatchData.objects.filter(match_id=match_id)
    video_path = "videos/pgc/" + match_id + ".html"
    context = {'match_data': match_data, "video" : video_path }
    return render(request, 'pro/pro_detail.html', context)


