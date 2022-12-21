from django.db import models

# Create your models here.
class PgcList(models.Model):
    """
        match_id            매치 아이디
        tournament_type     대회 종류
        create_date         생성 시간
    """

    match_id         = models.CharField(max_length=100)
    tournament_type  = models.CharField(max_length=50)
    create_date      = models.CharField(max_length=50)

    def __str__(self):
        return self.tournament_type + ",", self.create_date + ",", self.match_id

class MatchData(models.Model):
    """
        match_id            매치 아이디
        created_at          게임 생성시간
        user_name           유저명
        kill                킬수
        headkill            헤드샷 킬수
        longestkill         킬 최대거리
        loadkill            로드킬
        teamkill            팀킬
        assist              도움 횟수
        damagedealt         총 입힌 데미지
        damagetaken         총 입은 데미지
        dbno                부활 횟수
        revive              부활 시킨 횟수
        walkdistance        걸은 거리
        ridedistance        차량 이동 거리
        swimdistance        수영 이동 거리
        distance            총 이동 거리
        boost               부스트 아이탬 사용 횟수
        heal                체력 회복 아이탬 사용 횟수
        deathtype           죽음 종류
        acquired            무기 습득 횟수
        team_member         팀원
        team_name           팀명
        team_kill           팀 총 킬수
        team_assist         팀 총 어시스트
        team_distance       팀 평균 이동 거리
        team_damagedealt    팀 총 가한 데미지
        team_damagetaken    팀 총 입은 데미지
        team_timesurvived   팀 평균 생존 시간
        timesurvived        생존 시간
        ranking             등수
        vehicle_destroys    차량 파괴 횟수
        map_name            맵이름
        game_duration       게임 지속 시간
    """

    match_id            = models.CharField(max_length=100)
    created_at          = models.CharField(max_length=50)
    user_name           = models.CharField(max_length=50)
    kill                = models.IntegerField()
    headkill            = models.IntegerField()
    longestkill         = models.FloatField()
    loadkill            = models.IntegerField()
    teamkill            = models.IntegerField()
    assist              = models.IntegerField()
    damagedealt         = models.FloatField()
    damagetaken         = models.FloatField()
    dbno                = models.IntegerField()
    revive              = models.IntegerField()
    walkdistance        = models.FloatField()
    ridedistance        = models.FloatField()
    swimdistance        = models.FloatField()
    distance            = models.FloatField()
    boost               = models.IntegerField()
    heal                = models.IntegerField()
    deathtype           = models.CharField(max_length=50)
    acquired            = models.IntegerField()
    team_member         = models.CharField(max_length=100)
    team_name           = models.CharField(max_length=50)
    team_kill           = models.IntegerField()
    team_assist         = models.IntegerField()
    team_distance       = models.FloatField()
    team_damagedealt    = models.FloatField()
    team_damagetaken    = models.FloatField()
    team_timesurvived   = models.FloatField()
    timesurvived        = models.FloatField()
    ranking             = models.IntegerField()
    vehicle_destroys    = models.IntegerField()
    map_name            = models.CharField(max_length=50)
    game_duration       = models.FloatField()
    # CSV파일에 존재하는 칼럼이지만, 백엔드에서 사용하지 않을것 같은데이터.. (만약 사용하게 될 수 있으니 작성)
    # kill_place, kill_streaks, player_id, telemetry_link, team_roster_id
    # player_id의 정보다 telemetry_link를 활용해서 매치 내에 자세한 정보를 추출 가능



class Video(models.Model):
    caption         = models.CharField(max_length=100)
    video           = models.FileField(upload_to="video/%y")
    thumb           = models.FileField(upload_to="thumb/%y", blank=True)
    def __str__(self):
        return self.caption
