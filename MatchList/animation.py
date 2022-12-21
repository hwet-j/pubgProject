# PUBG 분석 도구 (https://chicken-dinner.readthedocs.io/en/latest/index.html 참고)
from chicken_dinner.pubgapi import PUBG
from chicken_dinner.constants import COLORS
from chicken_dinner.constants import map_dimensions
from chicken_dinner.models.match import Match  # URL과 request를 활용하여 데이터를 가져올 수도 있다. (모듈 활용으로 간단하게 진행)
from chicken_dinner.models import Player

import pandas as pd
import numpy as np
from tqdm import tqdm     # 진행도를 나타내주는 라이브러리
# 시간관련 모듈
import time
from datetime import datetime
# 스케일링
from sklearn.preprocessing import MinMaxScaler

# 시각화 패키지
import matplotlib as mlp
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib import patheffects

import pprint
pp = pprint.PrettyPrinter(indent=5)

import warnings
warnings.filterwarnings('ignore')
# api key 설정 및 데이터 요청


# 저장된 모든 매치 기록을 애니메이션 화
def all_match_animation():
    import pandas as pd
    import os
    from chicken_dinner.pubgapi import PUBG

    api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2ZGNjNzNhMC0yMDk5LTAxMzctYjNjMi0wMmI4NjZkNzliOGIiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTUxNjk2NzA2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InB1YmctYmVzdC1wbGF5In0.Oz7GmLsWF7038XIO4vKd5sivhLreOnizxTNcARAEFQs'

    pubg = PUBG(api_key=api_key, shard='steam')
    # 전체 데이터 불러오기
    load_alldata = pd.read_csv("datas/ALL_MATCH.csv")
    # 매치 정보의 유니크 값 가져오기
    match_list = load_alldata.match_id.unique()
    # 분석에 의미없는 연습게임 목록을 저장할 리스트
    unnecessary_list = []

    # 매치 하나씩 작업
    for count, mat in enumerate(match_list):
        if os.path.isfile("animation/" + str(mat) + ".html"):
            print(len(match_list), "개 파일 중 ", count+1, "번째 데이터 SKIP")
            continue
        else:
            match_data = pubg.match(mat)
            match_telemetry = match_data.get_telemetry()

            if match_telemetry.map_id() in ["Range_Main"] or match_data.game_mode == 'tdm':
                unnecessary_list.append(mat)
                print(len(match_list), "개 파일 중 ", count + 1, "번째 데이터 SKIP")
                continue

            my_team = list(load_alldata["user_name"][load_alldata["match_id"] == mat])
            # 내팀 highlight 설정
            for ros, player in match_data.rosters_player_names.items():
                if any(name in player for name in my_team):
                    highlight_user = player
                    print(highlight_user)
                    break




            match_telemetry.playback_animation("animation/" + str(mat) + ".html", \
                                                   highlight_teams = highlight_user,
                                                  highlight_winner = False,
                                                  label_highlights = True,
                                                  # use_hi_res = True,
                                                  size = 7,
                                                  dpi = 100,
                                                 fps = 45)
            print(len(match_list), "개 파일 중 ", count+1, "번째 데이터 ANIMATION 작업 완료")

    training_list = pd.Series(unnecessary_list)
    training_list.to_csv("datas/unnecessary.csv", index=False)


# PGC 매치 기록을 애니메이션 화
def pgc_match_animation():
    import pandas as pd
    import os
    from chicken_dinner.pubgapi import PUBG

    api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2ZGNjNzNhMC0yMDk5LTAxMzctYjNjMi0wMmI4NjZkNzliOGIiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTUxNjk2NzA2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InB1YmctYmVzdC1wbGF5In0.Oz7GmLsWF7038XIO4vKd5sivhLreOnizxTNcARAEFQs'

    pubg = PUBG(api_key=api_key, shard='pc-tournament', gzip=True)
    # 전체 데이터 불러오기
    load_alldata = pd.read_csv("C:/Users/HC/PycharmProjects/pubgProject/MatchList/datas/pgc/PGC_MATCH.csv")
    # 매치 정보의 유니크 값 가져오기
    match_list = load_alldata.match_id.unique()

    # 매치 하나씩 작업
    for count, mat in enumerate(match_list):
        # if os.path.isfile("animation/pgc/" + str(mat) + ".html"):
        #     print(len(match_list), "개 파일 중 ", count+1, "번째 데이터 SKIP")
        #     continue
        # else:
        if count not in [229]:
            continue
        else:
            print(len(match_list), "개 파일 중 ", count + 1, "번째 데이터 시작")
            match_data = pubg.match(mat)
            match_telemetry = match_data.get_telemetry()

            match_telemetry.playback_animation("animation/pgc/" + str(mat) + ".html", \
                                                   # highlight_teams = highlight_user,
                                                  highlight_winner = True,
                                                  label_highlights = True,
                                                  # use_hi_res = True,
                                                  size = 8,
                                                  dpi = 100,
                                                 fps = 45)
            print(len(match_list), "개 파일 중 ", count+1, "번째 데이터 ANIMATION 작업 완료")
            # try:
            #     print(len(match_list), "개 파일 중 ", count + 1, "번째 데이터 시작")
            #     match_data = pubg.match(mat)
            #     match_telemetry = match_data.get_telemetry()
            #
            #     match_telemetry.playback_animation("animation/pgc/" + str(mat) + ".html", \
            #                                            # highlight_teams = highlight_user,
            #                                           highlight_winner = True,
            #                                           label_highlights = True,
            #                                           # use_hi_res = True,
            #                                           size = 8,
            #                                           dpi = 100,
            #                                          fps = 45)
            #     print(len(match_list), "개 파일 중 ", count+1, "번째 데이터 ANIMATION 작업 완료")
            # except Exception as e:
            #     print(e)
            #     print(len(match_list), "개 파일 중 ", count+1, "번째 데이터 ANIMATION 작업 오류!!!!!!!!!!\n")


if __name__ == "__main__":
    # all_match_animation()
    pgc_match_animation()
