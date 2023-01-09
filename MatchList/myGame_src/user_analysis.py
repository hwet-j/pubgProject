# 내가 직접 플레이한 (또는 친구들) 데이터를 가지고 분석
# 각 유저의 개인 기록을 가져와 csv로 저장


# 저장된 매치 기록 가져오기
def load_match():
    try:  # 저장된 데이터 전체 불러오기
        load_alldata = pd.read_csv("../datas/COMPETITIVE_MATCH.csv")
    except:  # 저장된 데이터가 없다면 빈 데이터 프레임으로 생성
        load_alldata = pd.DataFrame()

    return load_alldata




if __name__ == "__main__":
    import sys
    import os
    import pandas as pd
    from chicken_dinner.pubgapi import PUBG
    # API KEY 설정
    api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2ZGNjNzNhMC0yMDk5LTAxMzctYjNjMi0wMmI4NjZkNzliOGIiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTUxNjk2NzA2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InB1YmctYmVzdC1wbGF5In0.Oz7GmLsWF7038XIO4vKd5sivhLreOnizxTNcARAEFQs'
    # PUBG 인스턴스 가져오기
    pubg = PUBG(api_key=api_key, shard='steam')

    all_match = load_match()
    user_list = all_match.user_name.unique()        # 플레이어 유니크 값

    # 이후 사용한 무기나 선호 위치 등 추가
    
    # 유저별 분석
    for user in user_list:
        match_data = all_match[all_match["user_name"] == user]
        # 매치 기록 하나씩 가져옴
        for mat in match_data.match_id:     
            # 서로 다른 아이디에 같은 매치를 진행하면 동일한 작업을 반복하므로 동일 매치 기록이 저장된 데이터가 있으면 제외
            if os.path.isfile("../datas/mydata/" + mat + ".csv"):
                print("파일이 존재하여 SKIP")
                continue
            # 매치 인스턴스 불러오기
            try:
                match_instance= pubg.match(mat)
                match_telemetry = match_instance.get_telemetry()
            except Exception as e:
                print(e)
                continue
            # 경쟁전 데이터만 사용
            if match_instance.data['attributes']['matchType'] != "competitive":
                continue
            print(user, match_instance.created_at)
            # 데이터프레임에 저장할 변수 리스트
            h_map_id = []           # 맵이름
            h_user_id = []          # 유저명
            h_kill = []             # 킬 수
            h_headkill = []         # 헤드샷으로 죽인 수
            h_longestkill = []      # 최장거리 킬 거리
            h_loadkill = []         # 차량으로 죽인 횟수
            h_teamkill = []         # 팀원을 죽인 횟수
            h_assist = []           # 어시스트
            h_damagedealt = []      # 입힌 데미지 총량
            h_damagetaken = []      # 입은 피해량
            h_dbno = []             # 기절 횟수 (살아난 횟수)
            h_revive = []           # 살린 횟수
            h_walkdistance = []     # 걸은 거리
            h_ridedistance = []     # 차량 이동거리
            h_swimdistance = []     # 수영 이동거리
            h_distance = []         # 총 이동거리
            h_boost = []            # 부스트 아이탬 사용횟수
            h_heal = []             # 체력회복 아이탬 사용 횟수
            h_deathtype = []        # 죽음의 종류
            h_acquired = []         # 무기 습득 횟수
            h_teammate = []         # 팀 목록
            h_timesurvived = []     # 팀원 생존시간
            h_ranking = []          # 등수

            # print("맵 이름",match_instance.map_id)
            # print("게임 종류", match_instance.game_mode)
            # print("경기 시간", match_instance.duration)
            # print("참가 팀 목록", match_telemetry.rosters())
            # print("참가자", match_instance.participants)
            for participant in match_instance.participants:
                one_user = participant.data

                # 데이터 프레임에 저장하기 위해 리스트로 작성
                h_user_id.append(one_user["attributes"]["stats"]['name'])      
                h_kill.append(one_user["attributes"]["stats"]['kills'])        
                h_headkill.append(one_user["attributes"]["stats"]["headshotKills"])
                h_longestkill.append(round(one_user["attributes"]["stats"]["longestKill"],2))
                h_loadkill.append(one_user["attributes"]["stats"]["roadKills"])
                h_teamkill.append(one_user["attributes"]["stats"]["teamKills"])
                h_assist.append(one_user["attributes"]["stats"]['assists'])
                h_damagedealt.append(round(one_user["attributes"]["stats"]["damageDealt"],2))
                try:        # 오류? 무언가의 이유로 존재하지 않는 유저가 있음 (초기 체력 100이므로 죽었다 가정하고 100)
                    h_damagetaken.append(round(match_telemetry.damage_taken()[one_user["attributes"]["stats"]['name']],2))
                except:
                    h_damagetaken.append(100)
                h_dbno.append(one_user["attributes"]["stats"]["DBNOs"])
                h_revive.append(one_user["attributes"]["stats"]["revives"])
                h_walkdistance.append(round(one_user["attributes"]["stats"]["walkDistance"] / 1000, 3))
                h_ridedistance.append(round(one_user["attributes"]["stats"]["rideDistance"] / 1000, 3))
                h_swimdistance.append(round(one_user["attributes"]["stats"]["swimDistance"] / 1000, 3))
                h_distance.append((h_walkdistance[-1] + h_ridedistance[-1] + h_swimdistance[-1]))
                h_boost.append(one_user["attributes"]["stats"]["boosts"])
                h_heal.append(one_user["attributes"]["stats"]["heals"])
                h_deathtype.append(one_user["attributes"]["stats"]["deathType"])
                h_acquired.append(one_user["attributes"]["stats"]["weaponsAcquired"])
                for ros in match_instance.rosters_player_names.values():
                    if h_user_id[-1] in ros:
                        h_teammate.append(ros)
                h_timesurvived.append(one_user["attributes"]["stats"]["timeSurvived"])
                h_ranking.append(one_user["attributes"]["stats"]["winPlace"])

            # 리스트에 저장된 데이터를 데이퍼 프레임화
            data_df = pd.DataFrame(zip(h_user_id, h_kill, h_headkill, h_longestkill, h_loadkill, h_teamkill, h_assist, h_damagedealt,\
                                       h_damagetaken, h_dbno, h_revive , h_walkdistance, h_ridedistance, h_swimdistance, h_distance, h_boost, \
                                       h_heal, h_deathtype, h_acquired, h_teammate, h_timesurvived, h_ranking))
            data_df.columns = ['user_id', 'kills', 'headshot_kills', 'longest_kill', 'load_kills', 'team_kills', 'assists', 'damage_dealt',\
                                'damage_taken', 'dbnos', 'revives', 'walk_distance', 'ride_distance', 'swim_distance', 'total_distance', 'boosts', \
                                 'heals', 'weapons_acquired', 'time_survived', 'win_place']
            # 공통된 match 정보를 입력 ( 비효율적, 다른 방법이 존재하면 변경예정 )
            if match_instance.map_id == "Erangel_Main" or match_instance.map_id == "Baltic_Main":
                data_df["map_name"] = "에란겔"
            elif match_instance.map_id == "Desert_Main":
                data_df["map_name"] = "미라마"
            elif match_instance.map_id == "DihorOtok_Main ":
                data_df["map_name"] = "비켄디"
            elif match_instance.map_id == "Tiger_Main" or match_instance.map_id == "Taego_Main":
                data_df["map_name"] = "테이고"
            else:
                data_df["map_name"] = match_instance.map_id

                
            data_df["game_created"] = match_instance.created_at
            data_df['game_mode'] = match_instance.game_mode
            data_df["duration"] = match_instance.duration
            data_df.to_csv("../datas/match_data/" + mat + ".csv", index=False, encoding="euc-kr")
            print("CSV파일 저장 완료")



