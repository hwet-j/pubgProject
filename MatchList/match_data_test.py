# 대회 기록 - PGC 데이터를 사용




# PGC 매치기록을 가져오는 함수
# 대회종류, 대회 시간, 매치 아이디
def pgc_match_list():
    import pandas as pd
    import requests
    import time
    # API KEY 설정
    api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2ZGNjNzNhMC0yMDk5LTAxMzctYjNjMi0wMmI4NjZkNzliOGIiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTUxNjk2NzA2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InB1YmctYmVzdC1wbGF5In0.Oz7GmLsWF7038XIO4vKd5sivhLreOnizxTNcARAEFQs'

    headers = {'accept': 'application/vnd.api+json',
               'Authorization': f'Bearer {api_key}'}


    url = "https://api.pubg.com/tournaments"
    r = requests.get(url, headers=headers)
    pgc = r.json()
    # PGC 경기만 사용 / 어떤 대회인지와 대회 시간 -> 대회 API검색은 대회 졸류로 검색됨
    pgc_league = {league['attributes']['createdAt']: league['id'] for league in pgc['data'] if '-pgc' in league['id']}

    # createdAt, id 데이터를 저장할 딕셔너리
    league_type = []
    match_id = []
    created_at = []
    for league in pgc_league.values():
        url = "https://api.pubg.com/tournaments/" + league
        r = requests.get(url, headers=headers)
        leg_json = r.json()
        # 각 경기 데이터 추가
        for item in leg_json['included']:
            league_type.append(league)
            match_id.append(item['id'])
            created_at.append(item['attributes']['createdAt'])

        time.sleep(15)

    pgc_matchId_df = pd.DataFrame(
        {'league_type': league_type, 'match_id': match_id, 'created_at': created_at})
    pgc_matchId_df.to_csv("C:/Users/HC/PycharmProjects/pubgProject/MatchList/datas/pgc/PGC_MATCH.csv", index=False)
    return None


# 각 매치당 플레이어들의 기록을 가져오는 함수
# 매치 별 기본적인 개인 기록을 가져와 저장한다. ( telemetry를 사용해 복잡한 정보는 여기서 추출 하지 않음 )
def pro_match_data():
    import pandas as pd
    from chicken_dinner.pubgapi import PUBG
    from chicken_dinner.pubgapi import PUBGCore
    import time
    import os
    # API KEY 설정
    api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2ZGNjNzNhMC0yMDk5LTAxMzctYjNjMi0wMmI4NjZkNzliOGIiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTUxNjk2NzA2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InB1YmctYmVzdC1wbGF5In0.Oz7GmLsWF7038XIO4vKd5sivhLreOnizxTNcARAEFQs'

    # PUBG 인스턴스 가져오기
    pubg = PUBG(api_key=api_key, shard='pc-tournament', gzip=True)
    pubgCore = PUBGCore(api_key=api_key, shard='pc-tournament', gzip=True)

    pgc_data = pd.read_csv("C:/Users/HC/PycharmProjects/pubgProject/MatchList/datas/pgc/PGC_MATCH.csv")

    all_data = pd.DataFrame()

    # 매치 정보
    match_id = []               # 매치 아이디
    created_at = []             # 생성시간
    map_name = []               # 맵 이름  
    duration = []               # 지속 시간
    telemetry_link = []         # Telemetry 주소
    leng = len(pgc_data)

    for cnt, mat in enumerate(pgc_data['match_id']):
        if os.path.isfile("C:/Users/HC/PycharmProjects/pubgProject/MatchList/datas/pgc/" + mat + ".csv"):
            print(leng, "개 데이터 중,", cnt+1, "번째 데이터 SKIP")
            continue
        print(leng, "개 데이터 중,", cnt+1, "번 째 데이터 진행 중.....")

        # 매치 참가자 개인 기록 (stat 정보를 불러와 한번에 DataFrame으로 생성)
        # player_id = []              # 플레이어 아이디
        # player_kill = []            # 플레이어 킬수
        # player_headshot =[]         # 헤드샷
        # player_loadkill = []        # 로드킬
        # player_teamkill = []        # 팀킬
        # player_longestkill = []     # 최장 킬 거리
        # player_assist = []          # 어시스트
        # player_damagedealt = []     # 가한 데미지
        player_damagetaken = []  # 받은 데미지
        # player_dbno = []            # 기절 했지만 살아난 횟수
        # player_revive = []          # 살린 횟수
        # player_walkdistance = []    # 걸은 거리
        # player_ridedistance = []    # 차량 이동거리
        # player_swimdistance = []    # 수영 이동거리
        # player_distance = []        # 총 이동거리
        # player_heal = []            # 회복 아이탬 사용
        # player_boost = []           # 부스트 아이탬 사용
        # player_acquired = []        # 무기 획득
        # player_timesurvived = []    # 생존 시간
        ## 마지막 총, 자기장 안에 있던 시간 등 추가

        # 매치 참가자의 팀 기록
        team_roster_id = []  # 팀 아이디 주소 값
        team_name = []  # 팀 이름
        team_name2 = []  # 팀 이름
        team_member = []  # 팀 목록
        team_rank = []  # 팀 순위
        team_kill = []  # 팀 종합 킬
        team_assist = []  # 팀 종합 어시스트
        team_distance = []  # 팀 종합 이동거리
        team_damagedealt = []  # 팀 종합 가한 데미지
        team_damagetaken = []  # 팀 종합 받은 데미지
        team_timesurvived = []  # 팀 종합 생존시간

        # 참가자 기록
        participant_stats = []

        # API 정보 불러오기
        match = pubg.match(mat)
        match_telemetry = match.get_telemetry()
        # 매치 정보
        # match_id, created_at, map_name, duration, telemetry_link
        match_id.append(match.id)
        created_at.append(match.created_at)
        map_name.append(match.map_name)
        duration.append(match.duration)
        telemetry_link.append(match.telemetry_url)

        # 팀, 개인 기록 정보
        # match_id, player_id, team_roster_id, team_name, team_member, team_rank, team_kill
        # team_assist, team_distance, team_damagedealt, team_damagetaken, team_timesurvived
        # ..................
        rosters = match.rosters
        for ros in range(len(rosters)):
            # 팀 정보
            roster = rosters[ros]
            roster_participant = roster.participants
            rost_stats = roster.stats

            team_roster_id.append(roster.id)
            team_member.append(roster.player_names)
            team_name.append(team_member[-1][0][0:team_member[-1][0].find("_")])  # 팀명
            team_rank.append(rost_stats['rank'])

            # Team 데이터에 저장할 변수 설정
            total_kill = 0
            total_assist = 0
            avg_distance = 0
            total_damagedealt = 0
            total_damagetaken = 0
            avg_timesurvivied = 0

            for part in range(len(roster_participant)):
                # 개인 정보
                participant = roster_participant[part]
                part_stats = participant.stats
                try:
                    player_damagetaken.append(match_telemetry.damage_taken()[part_stats["name"]])
                except:
                    player_damagetaken.append(100)
                participant_stats.append(part_stats)
                team_name2.append(team_name[-1])
                total_kill += part_stats['kills']
                total_assist += part_stats['assists']
                avg_distance += part_stats['ride_distance'] + part_stats['swim_distance'] + part_stats['walk_distance']
                total_damagedealt +=part_stats['damage_dealt']
                total_damagetaken += player_damagetaken[-1]
                avg_timesurvivied += part_stats['time_survived']

            # 평균값은 맴버 수만큼 나눠 계산
            avg_distance /= len(team_member[-1])
            avg_timesurvivied /= len(team_member[-1])
            team_kill.append(total_kill)
            team_assist.append(total_assist)
            team_distance.append(avg_distance)
            team_damagedealt.append(total_damagedealt)
            team_damagetaken.append(total_damagetaken)
            team_timesurvived.append(avg_timesurvivied)

        # 매치 기록
        # match_info = pd.DataFrame(
        #     {'match_id': match_id, 'created_at': created_at, 'map_name': map_name, 'duration': duration,
        #      'telemetry_link': telemetry_link}
        # )

        # 매치 팀 기록
        match_roster_stats = pd.DataFrame(
            {'team_roster_id': team_roster_id, 'team_name': team_name, 'team_member': team_member, 'team_rank': team_rank,
             'team_kill': team_kill, 'team_assist': team_assist, 'team_distance': team_distance,
             'team_damagedealt': team_damagedealt, 'team_damagetaken': team_damagetaken, 'team_timesurvived': team_timesurvived}
        )

        # 매치 개인 기록
        match_participant_stats = pd.DataFrame(participant_stats)
        match_participant_stats["damage_taken"] = player_damagetaken
        match_participant_stats["team_name"] = team_name2
        match_participant_stats["match_id"] = match_id[-1]
        match_participant_stats["created_at"] = created_at[-1]
        match_participant_stats["map_name"] = map_name[-1]
        match_participant_stats["duration"] = duration[-1]
        match_participant_stats["telemetry_link"] = telemetry_link[-1]

        # row 생략 없이 출력 / col 생략 없이 출력
        # pd.set_option('display.max_rows', None)
        # pd.set_option('display.max_columns', None)

        # 인덱스 기준으로 join
        match_data = pd.merge(match_participant_stats, match_roster_stats, how='inner', on='team_name')
        # print(match_data)
        all_data = pd.concat([all_data, match_data], axis=0)
        match_data.to_csv("C:/Users/HC/PycharmProjects/pubgProject/MatchList/datas/pgc/" + mat + ".csv", index=False)
        time.sleep(2)


    # 중복 데이터가 있다면 삭제
    all_data.drop_duplicates(inplace=True)
    all_data.to_csv("C:/Users/HC/PycharmProjects/pubgProject/MatchList/datas/pgc/MATCH_ALL_STAT.csv", index=False)
    print("저장완료")

if __name__ == "__main__":
    # pgc_match_list()
    pro_match_data()
