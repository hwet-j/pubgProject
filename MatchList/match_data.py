import sys

# 저장된 매치 기록 가져오기
def load_match():

    try:  # 저장된 데이터 전체 불러오기
        load_alldata = pd.read_csv("C:/Users/HC/PycharmProjects/pubgProject/MatchList/datas/COMPETITIVE_MATCH.csv")
    except:  # 저장된 데이터가 없다면 빈 데이터 프레임으로 생성
        load_alldata = pd.DataFrame()

    return load_alldata




if __name__ == "__main__":
    import pandas as pd
    from chicken_dinner.pubgapi import PUBG
    # API KEY 설정
    api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2ZGNjNzNhMC0yMDk5LTAxMzctYjNjMi0wMmI4NjZkNzliOGIiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTUxNjk2NzA2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InB1YmctYmVzdC1wbGF5In0.Oz7GmLsWF7038XIO4vKd5sivhLreOnizxTNcARAEFQs'
    # PUBG 인스턴스 가져오기
    pubg = PUBG(api_key=api_key, shard='steam')

    game_id = ['Hwet_J', 'sickhu', '30XXDDD', 'hyeonji']  # 리스트로 작성해서 여러 아이디 데이터 기록얻기.

    all_match = load_match()

    for mat in all_match.match_id:
        match_data = pubg.match(mat)
        match_telemetry = match_data.get_telemetry()
        # for ros in match_data.rosters_player_names.values():
        #     if "Hwet_J" in ros:
        #         print(ros)
        category_list = []
        # print(match_telemetry.filter_by("log_item_equip"))
        # print(match_telemetry.event_types())
        print(match_telemetry.filter_by())

        # for equip, unequip in zip(match_telemetry.filter_by("log_item_equip"), match_telemetry.filter_by("log_item_unequip")):
        #     # category_list.append(equip['item']['sub_category'])
        #     if equip['item']['sub_category'] == "Main":
        #         print(equip['item']["item_id"])



        break
