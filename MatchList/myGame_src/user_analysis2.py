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
    match_participant_stats_all = pd.DataFrame()
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
            h_damagetaken = []
            participants_stats = []
            tot_distance = []

            for participant in match_instance.participants:
                player = participant.name

                player_stats = participant.stats
                participants_stats.append(player_stats)
                print(player_stats)
                tot_distance.append((player_stats["walk_distance"] + player_stats['ride_distance'] + player_stats['swim_distance']))
                # 데이터 프레임에 저장하기 위해 리스트로 작성
                try:        # 오류? 무언가의 이유로 존재하지 않는 유저가 있음 (초기 체력 100이므로 죽었다 가정하고 100)
                    h_damagetaken.append(round(match_telemetry.damage_taken()[player]))
                except:
                    h_damagetaken.append(0)     # 플레이어에게 죽지 않았다 가정하고 0으로 설정 ( 자살하거나 자기장에 죽었다고 가정 )

            # 리스트에 저장된 데이터를 데이퍼 프레임화
            match_participant_stats_df = pd.DataFrame(participants_stats)
            match_participant_stats_df['damage_taken'] = h_damagetaken
            match_participant_stats_df["match_id"] = mat
            match_participant_stats_df["total_distance"] = tot_distance
            match_participant_stats_df["created_at"] = match_instance.created_at
            match_participant_stats_df["map_name"] = match_telemetry.map_name()
            match_participant_stats_df["duration"] = match_instance.duration
            match_participant_stats_df["telemetry_link"] = match_instance.telemetry_url

            # 공통된 match 정보를 입력 ( 비효율적, 다른 방법이 존재하면 변경예정 )
            if match_instance.map_id == "Erangel_Main" or match_instance.map_id == "Baltic_Main":
                match_participant_stats_df["map_name"] = "에란겔"
            elif match_instance.map_id == "Desert_Main":
                match_participant_stats_df["map_name"] = "미라마"
            elif match_instance.map_id == "DihorOtok_Main ":
                match_participant_stats_df["map_name"] = "비켄디"
            elif match_instance.map_id == "Tiger_Main" or match_instance.map_id == "Taego_Main":
                match_participant_stats_df["map_name"] = "테이고"
            else:
                match_participant_stats_df["map_name"] = match_instance.map_id

            match_participant_stats_df.to_csv("../datas/mydata/" + mat + ".csv", index=False, encoding="euc-kr")
            match_participant_stats_all = pd.concat([match_participant_stats_all, match_participant_stats_df],
                                                    ignore_index=True)

            print("CSV파일 저장 완료")
    match_participant_stats_all.to_csv("../datas/mydata/All_data.csv", index=False)



