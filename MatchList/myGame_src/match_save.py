# 입력 : 게임 아이디
# 출력 : 매치 리스트 ( 전체 데이터는 안들어옴 - 어느 기간동안의 정보가 들어오는 지 정확히 파악 못함. )
def match_search_save(game_id):
    import pandas as pd
    from chicken_dinner.pubgapi import PUBG
    # API KEY 설정
    api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2ZGNjNzNhMC0yMDk5LTAxMzctYjNjMi0wMmI4NjZkNzliOGIiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTUxNjk2NzA2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InB1YmctYmVzdC1wbGF5In0.Oz7GmLsWF7038XIO4vKd5sivhLreOnizxTNcARAEFQs'
    # PUBG 인스턴스 가져오기
    pubg = PUBG(api_key=api_key, shard='steam')

    try:  # 저장된 데이터 전체 불러오기
        load_alldata = pd.read_csv("../datas/ALL_MATCH.csv")
    except:  # 저장된 데이터가 없다면 빈 데이터 프레임으로 생성
        load_alldata = pd.DataFrame()

    # 데이터가 존재하면
    if load_alldata.empty:
        all_data = pd.DataFrame()
    else:
        all_data = load_alldata

    # 아이디 하나씩 작업 (프레임 생성 및 csv파일 저장)
    for g_id in game_id:
        try:    # 아이디 별 저장된 데이터 불러오기
            personal_data = pd.read_csv("../datas/" + g_id + ".csv")
        except: # 저장된 데이터가 없다면 빈 데이터 프레임으로 생성
            personal_data = pd.DataFrame()

        # 아이디로 필터
        player_data = pubg.players_from_names(g_id)[0]
        find_match_id = player_data.match_ids       # 플레이어의 검색가능한 매치 리스트 반환

        match_list = []
        time_list = []                              # 매치 생성 시간을 저장할 리스트
        name_list = []                              # 검색 플레이어 이름

        for one_match in find_match_id:
            if pubg.match(one_match).game_mode in ["tdm"]:#  or pubg.match(one_match).map_id in ["Range_Main", "DihorOtok_Main", "Summerland_Main", "Savage_Main"]:
                continue
            match_list.append(one_match)
            time_list.append(pubg.match(one_match).created_at)  # 생성 시간 리스트
            name_list.append(g_id)

        # 한 아이디로 검색되는 정보 저장
        data = pd.DataFrame({'user_name':name_list, 'created_at':time_list, "match_id": match_list})
        
        # 이전 데이터가 존재한다면 데이터 합치기
        if personal_data.empty:
            pass
        else:
            data = pd.concat([personal_data, data], ignore_index=True)
            data.drop_duplicates(inplace=True)

        # 전체 데이터를 하나의 데이터 프레임에 저장
        all_data = pd.concat([all_data, data], ignore_index=True)
        # 아이디 별 데이터 저장
        data.to_csv("../datas/" + g_id + ".csv", index=False)
        
    # 중복 데이터가 있다면 삭제 (전부 동일한 정보만)
    all_data.drop_duplicates(inplace=True)
    all_data.to_csv("../datas/ALL_MATCH.csv", index=False)
    print("저장완료")


def competitive_save(game_id):
    import pandas as pd
    from chicken_dinner.pubgapi import PUBG
    # API KEY 설정
    api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2ZGNjNzNhMC0yMDk5LTAxMzctYjNjMi0wMmI4NjZkNzliOGIiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTUxNjk2NzA2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InB1YmctYmVzdC1wbGF5In0.Oz7GmLsWF7038XIO4vKd5sivhLreOnizxTNcARAEFQs'
    # PUBG 인스턴스 가져오기
    pubg = PUBG(api_key=api_key, shard='steam')

    try:  # 저장된 데이터 전체 불러오기
        load_alldata = pd.read_csv("../datas/COMPETITIVE_MATCH.csv")
        
        index_list = []
        # 오류가 발생하거나 경쟁전 데이터가 아닌경우 삭제
        for count, inst in enumerate(load_alldata['match_id']):
            try:
                if pubg.match(inst).data['attributes']['matchType'] != "competitive":
                    index_list.append(count)
                else:
                    None
            except:
                index_list.append(count)

        load_alldata.drop(index = index_list, inplace=True)
        load_alldata.reset_index(drop=True, inplace=True)
    except Exception as e:  # 저장된 데이터가 없다면 빈 데이터 프레임으로 생성
        load_alldata = pd.DataFrame()
        print('오류', e)

    # 데이터가 존재하면
    if load_alldata.empty:
        all_data = pd.DataFrame()
    else:
        all_data = load_alldata

    # 아이디 하나씩 작업 (프레임 생성 및 csv파일 저장)
    for g_id in game_id:
        try:  # 아이디 별 저장된 데이터 불러오기
            personal_data = pd.read_csv("../datas/COMPETITIVE_" + g_id + ".csv")
        except:  # 저장된 데이터가 없다면 빈 데이터 프레임으로 생성
            personal_data = pd.DataFrame()

        # 아이디로 필터
        player_data = pubg.players_from_names(g_id)[0]
        find_match_id = player_data.match_ids  # 플레이어의 검색가능한 매치 리스트 반환

        match_list = []
        time_list = []  # 매치 생성 시간을 저장할 리스트
        name_list = []  # 검색 플레이어 이름

        for one_match in find_match_id:
            # 경쟁전이 아닌 데이터 제외
            if pubg.match(one_match).game_mode in ["tdm"] or pubg.match(one_match).data['attributes']['matchType'] != "competitive":  # or pubg.match(one_match).map_id in ["Range_Main", "DihorOtok_Main", "Summerland_Main", "Savage_Main"]:
                continue
            match_list.append(one_match)
            time_list.append(pubg.match(one_match).created_at)  # 생성 시간 리스트
            name_list.append(g_id)

        # 한 아이디로 검색되는 정보 저장
        data = pd.DataFrame({'user_name': name_list, 'created_at': time_list, "match_id": match_list})

        # 이전 데이터가 존재한다면 데이터 합치기
        if personal_data.empty:
            pass
        else:
            data = pd.concat([personal_data, data], ignore_index=True)
            data.drop_duplicates(inplace=True)

        # 전체 데이터를 하나의 데이터 프레임에 저장
        all_data = pd.concat([all_data, data], ignore_index=True)
        # 아이디 별 데이터 저장
        data.to_csv("../datas/COMPETITIVE_" + g_id + ".csv", index=False)

    # 중복 데이터가 있다면 삭제 (전부 동일한 정보만)
    all_data.drop_duplicates(inplace=True)
    all_data.to_csv("../datas/COMPETITIVE_MATCH.csv", index=False)
    print("저장완료")

if __name__ == "__main__":
    # 게임 아이디 설정 및 매치리스트 함수 실행
    game_id = ['Hwet_J', 'sickhu', '30XXDDD', 'hyeonji']  # 리스트로 작성해서 여러 아이디 데이터 기록얻기.
    match_search_save(game_id)
    competitive_save(game_id)
    print('종료')