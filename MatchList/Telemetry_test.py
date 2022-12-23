# 대회 기록 - PGC 데이터를 사용
# 데이터 분석에 활용할 데이터를 추출
import sys


def pro_anal():
    import pandas as pd
    from chicken_dinner.pubgapi import PUBG
    from chicken_dinner.pubgapi import PUBGCore
    import os
    # API KEY 설정
    api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2ZGNjNzNhMC0yMDk5LTAxMzctYjNjMi0wMmI4NjZkNzliOGIiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTUxNjk2NzA2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InB1YmctYmVzdC1wbGF5In0.Oz7GmLsWF7038XIO4vKd5sivhLreOnizxTNcARAEFQs'
    # PUBG 인스턴스 가져오기
    pubg = PUBG(api_key=api_key, shard='pc-tournament', gzip=True)

    pgc_data = pd.read_csv("C:/Users/HC/PycharmProjects/pubgProject/MatchList/datas/pgc/PGC_MATCH.csv")
    # 전체 데이터를 저장할 데이터 프레임

    for cnt, mat in enumerate(pgc_data['match_id']):
        # 이미 저장된 데이터는 생략
        current_match = pubg.match(mat)  # 매치 기록 하나를 가져옴
        telemetry = current_match.get_telemetry()  # 현재 매치의 Telemetry값을 가져옴

        attackLog = telemetry.filter_by('log_player_attack')  # 교전 (공격한 경우) 데이터
        # fire_count = telemetry.filter_by('log_weapon_fire_count')  # 교전 (공격한 경우) 데이터

        # print(attackLog)
        unique_check = []
        for log in attackLog:
            try:
                unique_check.append(log['weapon']['attached_items'])
            except:
                None
            # print(log['attack_type'])
        unique_check = sum(unique_check, [])
        # print(unique_check)
        print(list(set(unique_check)))
        # print(list(unique_check))

        sys.exit()

def mat_test(shard, match_ty):
    import pandas as pd
    from chicken_dinner.pubgapi import PUBG
    # API KEY 설정
    api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2ZGNjNzNhMC0yMDk5LTAxMzctYjNjMi0wMmI4NjZkNzliOGIiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTUxNjk2NzA2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InB1YmctYmVzdC1wbGF5In0.Oz7GmLsWF7038XIO4vKd5sivhLreOnizxTNcARAEFQs'
    # PUBG 인스턴스 가져오기
    pubg = PUBG(api_key=api_key, shard=shard, gzip=True)

    if match_ty == 'com':
        pgc_data = pd.read_csv("C:/Users/HC/PycharmProjects/pubgProject/MatchList/datas/pgc/PGC_MATCH.csv")
    else:
        pgc_data = pd.read_csv("C:/Users/HC/PycharmProjects/pubgProject/MatchList/datas/ALL_MATCH.csv")

    for mat in pgc_data['match_id']:
        try:
            current_match = pubg.match(mat)  # 매치 기록 하나를 가져옴
            telemetry = current_match.get_telemetry()  # 현재 매치의 Telemetry값을 가져옴

            attackLog = telemetry.filter_by('log_player_attack')  # 교전 (공격한 경우) 데이터
            # fire_count = telemetry.filter_by('log_weapon_fire_count')  # 교전 (공격한 경우) 데이터

            # print(attackLog)
            unique_check = []
            for log in attackLog:
                unique_check.append(log['vehicle'])

            print(list(set(unique_check)))
        except Exception as e:
            print(e)

    sys.exit()


if __name__ == "__main__":
    # pro_anal()
    # mat_test("pc-tournament", 'com')    # steam, pc-tournament

    import matplotlib.pyplot as plt
    plt.plot([1,2,3])
    plt.show()


    '''
    TelemetryEvent = ({
        "_D": "2022-11-20T15:03:40.910Z",
        "_T": "LogPlayerAttack",
        "attack_id": 620757206,
        "attack_type": "Weapon",
        "attacker": {
            "account_id": "account.db97ab142d4748e694dd3fe24222efdb",
            "health": 77,
            "is_in_blue_zone": False,
            "is_in_red_zone": False,
            "location": {
                "x": 466215.03125,
                "y": 203538.96875,
                "z": 6939.27001953125
            },
            "name": "NAVI_Mell",
            "ranking": 1,
            "team_id": 1,
            "zone": []
        },
        "common": {
            "is_game": 9
        ,
        "fire_weapon_stack_count": 7,
        "vehicle": Null,
        "weapon": {
            "attached_items": [
                "Item_Attach_Weapon_Magazine_ExtendedQuickDraw_Large_C",
                "Item_Attach_Weapon_Muzzle_FlashHider_Large_C",
                "Item_Attach_Weapon_Upper_Holosight_C",
                "Item_Attach_Weapon_Stock_AR_Composite_C",
                "Item_Attach_Weapon_Lower_Foregrip_C"
            ],
            "category": "Weapon",
            "item_id": "Item_Weapon_HK416_C",
            "stack_count": 1,
            "sub_category": "Main"
        }
    })]
    '''