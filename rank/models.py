from django.db import models

# Create your models here.

class PersonalData(models.Model):
    """
    dak.gg에서 크롤링 가능한 데이터를 기반으로 순위예측

    dbnos : 기절시킨횟수(죽이지는 못함)
    assists : 도움을 준 횟수
    boosts : 부스트 아이템 사용횟수
    damage_dealt : 가한 데미지
    headshot_kills : 헤드샷으로 죽인 횟수
    heals : 회복 아이템 사용횟수
    kills : 킬수
    longest_kill : 킬 최대거리
    revives : 살려준 횟수
    total_distance : 총 이동거리 (km)
    ride_distance : 차량 이동거리 (km)
    road_kills : 차량으로 죽인 횟수
    swim_distance : 수영 이동거리 (km)
    vehicle_destroys : 차량 파괴횟수
    time_survived : 생존 시간 (s)
    walk_distance : 걸은 거리 (km)
    weapons_acquired : 무기획득 횟수
    team_count : 매치 참가 팀수
    map_name : 맵 이름 (에란겔 : 0 , 미라마 : 1, 태이고 : 2)
    duration : 게임 지속시간 (s)
    win_place : 게임 순위 (예측 파라미터)
    """

    user_id             = models.CharField(max_length=50)
    dbnos               = models.IntegerField()
    assists             = models.IntegerField()
    boosts              = models.IntegerField()
    damage_dealt        = models.IntegerField()
    headshot_kills      = models.IntegerField()
    heals               = models.IntegerField()
    kills               = models.IntegerField()
    longest_kill        = models.FloatField()
    revives             = models.IntegerField()
    total_distance      = models.FloatField()
    ride_distance       = models.FloatField()
    road_kills          = models.IntegerField()
    swim_distance       = models.FloatField()
    vehicle_destroys    = models.IntegerField()
    time_survived       = models.IntegerField()
    walk_distance       = models.FloatField()
    weapons_acquired    = models.IntegerField()
    team_count          = models.IntegerField()
    map_name            = models.CharField(max_length=50)
    duration            = models.IntegerField()
    win_place           = models.IntegerField()

