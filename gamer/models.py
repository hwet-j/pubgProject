from django.db import models
from django.utils import timezone

# https://wikidocs.net/71306

class Matchlist(models.Model):
    user_name        = models.CharField(max_length=50)
    create_date      = models.CharField(max_length=100)
    match_id         = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name + ",", self.create_date + ",", self.match_id


class Matchdata(models.Model):
    # list            = models.ForeignKey(Matchlist, on_delete=models.CASCADE)
    user_id         = models.CharField(max_length=50, verbose_name = "유저명")
    kill            = models.IntegerField(verbose_name = "킬수")
    headkill        = models.IntegerField(verbose_name = "헤드샷 킬수")
    longestkill     = models.FloatField(verbose_name = "킬 최대거리")
    loadkill        = models.IntegerField(verbose_name = "로드킬")
    teamkill        = models.IntegerField(verbose_name = "팀킬")
    assist          = models.IntegerField(verbose_name = "도움 횟수")
    damagedealt     = models.FloatField(verbose_name = "총 입힌 데미지")
    damagetaken     = models.FloatField(verbose_name = "총 입은 데미지")
    dbno            = models.IntegerField(verbose_name = "부활횟수")
    revive          = models.IntegerField(verbose_name = "부활시킨 횟수")
    walkdistance    = models.FloatField(verbose_name = "걸은거리")
    ridedistance    = models.FloatField(verbose_name = "차량 이동거리")
    swimdistance    = models.FloatField(verbose_name = "수영 이동거리")
    distance        = models.FloatField(verbose_name = "총 이동거리")
    boost           = models.IntegerField(verbose_name = "부스트 아이탬 사용 횟수")
    heal            = models.IntegerField(verbose_name = "체력회복 아이탬 사용 횟수")
    deathtype       = models.CharField(max_length=50, verbose_name = "죽음종류")
    acquired        = models.IntegerField(verbose_name = "무기습득 횟수")
    teammate        = models.CharField(max_length=100, verbose_name = "팀원")
    timesurvived    = models.CharField(max_length=50, verbose_name = "생존시간")
    ranking         = models.IntegerField(verbose_name = "등수")
    map_name        = models.CharField(max_length=50, verbose_name = "맵이름")
    game_created    = models.CharField(max_length=100, verbose_name = "게임시작시간")
    game_mode       = models.CharField(max_length=50, verbose_name = "게임모드")
    game_duration   = models.CharField(max_length=50, verbose_name = "게임지속시간")