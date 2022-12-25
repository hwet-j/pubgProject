# 대회 기록 - PGC 데이터를 사용
# 데이터 분석에 활용할 데이터를 추출
import sys
import datetime

import matplotlib.pyplot as plt

def weapon_mapping():
    weapons = {
        "AIPawn_Base_Female_C": "AI Player",
        "AIPawn_Base_Male_C": "AI Player",
        "AirBoat_V2_C": "Airboat",
        "AquaRail_A_01_C": "Aquarail",
        "AquaRail_A_02_C": "Aquarail",
        "AquaRail_A_03_C": "Aquarail",
        "BP_ATV_C": "Quad",
        "BP_BRDM_C": "BRDM-2",
        "BP_Bicycle_C": "Mountain Bike",
        "BP_CoupeRB_C": "Coupe RB",
        "BP_DO_Circle_Train_Merged_C": "Train",
        "BP_DO_Line_Train_Dino_Merged_C": "Train",
        "BP_DO_Line_Train_Merged_C": "Train",
        "BP_Dirtbike_C": "Dirt Bike",
        "BP_DronePackage_Projectile_C": "Drone",
        "BP_Eragel_CargoShip01_C": "Ferry Damage",
        "BP_FakeLootProj_AmmoBox_C": "Loot Truck",
        "BP_FakeLootProj_MilitaryCrate_C": "Loot Truck",
        "BP_FireEffectController_C": "Molotov Fire",
        "BP_FireEffectController_JerryCan_C": "Jerrycan Fire",
        "BP_Helicopter_C": "Pillar Scout Helicopter",
        "BP_IncendiaryDebuff_C": "Burn",
        "BP_JerryCanFireDebuff_C": "Burn",
        "BP_JerryCan_FuelPuddle_C": "Burn",
        "BP_KillTruck_C": "Kill Truck",
        "BP_LootTruck_C": "Loot Truck",
        "BP_M_Rony_A_01_C": "Rony",
        "BP_M_Rony_A_02_C": "Rony",
        "BP_M_Rony_A_03_C": "Rony",
        "BP_Mirado_A_02_C": "Mirado",
        "BP_Mirado_A_03_Esports_C": "Mirado",
        "BP_Mirado_Open_03_C": "Mirado (open top)",
        "BP_Mirado_Open_04_C": "Mirado (open top)",
        "BP_Mirado_Open_05_C": "Mirado (open top)",
        "BP_MolotovFireDebuff_C": "Molotov Fire Damage",
        "BP_Motorbike_04_C": "Motorcycle",
        "BP_Motorbike_04_Desert_C": "Motorcycle",
        "BP_Motorbike_04_SideCar_C": "Motorcycle (w/ Sidecar)",
        "BP_Motorbike_04_SideCar_Desert_C": "Motorcycle (w/ Sidecar)",
        "BP_Motorbike_Solitario_C": "Motorcycle",
        "BP_Motorglider_C": "Motor Glider",
        "BP_Motorglider_Green_C": "Motor Glider",
        "BP_Niva_01_C": "Zima",
        "BP_Niva_02_C": "Zima",
        "BP_Niva_03_C": "Zima",
        "BP_Niva_04_C": "Zima",
        "BP_Niva_05_C": "Zima",
        "BP_Niva_06_C": "Zima",
        "BP_Niva_07_C": "Zima",
        "BP_PickupTruck_A_01_C": "Pickup Truck (closed top)",
        "BP_PickupTruck_A_02_C": "Pickup Truck (closed top)",
        "BP_PickupTruck_A_03_C": "Pickup Truck (closed top)",
        "BP_PickupTruck_A_04_C": "Pickup Truck (closed top)",
        "BP_PickupTruck_A_05_C": "Pickup Truck (closed top)",
        "BP_PickupTruck_A_esports_C": "Pickup Truck (closed top)",
        "BP_PickupTruck_B_01_C": "Pickup Truck (open top)",
        "BP_PickupTruck_B_02_C": "Pickup Truck (open top)",
        "BP_PickupTruck_B_03_C": "Pickup Truck (open top)",
        "BP_PickupTruck_B_04_C": "Pickup Truck (open top)",
        "BP_PickupTruck_B_05_C": "Pickup Truck (open top)",
        "BP_Pillar_Car_C": "Pillar Security Car",
        "BP_PonyCoupe_C": "Pony Coupe",
        "BP_Porter_C": "Porter",
        "BP_Scooter_01_A_C": "Scooter",
        "BP_Scooter_02_A_C": "Scooter",
        "BP_Scooter_03_A_C": "Scooter",
        "BP_Scooter_04_A_C": "Scooter",
        "BP_Snowbike_01_C": "Snowbike",
        "BP_Snowbike_02_C": "Snowbike",
        "BP_Snowmobile_01_C": "Snowmobile",
        "BP_Snowmobile_02_C": "Snowmobile",
        "BP_Snowmobile_03_C": "Snowmobile",
        "BP_Spiketrap_C": "Spike Trap",
        "BP_TslGasPump_C": "Gas Pump",
        "BP_TukTukTuk_A_01_C": "Tukshai",
        "BP_TukTukTuk_A_02_C": "Tukshai",
        "BP_TukTukTuk_A_03_C": "Tukshai",
        "BP_Van_A_01_C": "Van",
        "BP_Van_A_02_C": "Van",
        "BP_Van_A_03_C": "Van",
        "BattleRoyaleModeController_Chimera_C": "Bluezone",
        "BattleRoyaleModeController_Def_C": "Bluezone",
        "BattleRoyaleModeController_Desert_C": "Bluezone",
        "BattleRoyaleModeController_DihorOtok_C": "Bluezone",
        "BattleRoyaleModeController_Heaven_C": "Bluezone",
        "BattleRoyaleModeController_Kiki_C": "Bluezone",
        "BattleRoyaleModeController_Savage_C": "Bluezone",
        "BattleRoyaleModeController_Summerland_C": "Bluezone",
        "BattleRoyaleModeController_Tiger_C": "Bluezone",
        "BlackZoneController_Def_C": "Blackzone",
        "Bluezonebomb_EffectActor_C": "Bluezone Grenade",
        "Boat_PG117_C": "PG-117",
        "Buff_DecreaseBreathInApnea_C": "Drowning",
        "Buggy_A_01_C": "Buggy",
        "Buggy_A_02_C": "Buggy",
        "Buggy_A_03_C": "Buggy",
        "Buggy_A_04_C": "Buggy",
        "Buggy_A_05_C": "Buggy",
        "Buggy_A_06_C": "Buggy",
        "Carepackage_Container_C": "Care Package",
        "Dacia_A_01_v2_C": "Dacia",
        "Dacia_A_01_v2_snow_C": "Dacia",
        "Dacia_A_02_v2_C": "Dacia",
        "Dacia_A_03_v2_C": "Dacia",
        "Dacia_A_03_v2_Esports_C": "Dacia",
        "Dacia_A_04_v2_C": "Dacia",
        "DroppedItemGroup": "Object Fragments",
        "EmergencyAircraft_Tiger_C": "Emergency Aircraft",
        "Jerrycan": "Jerrycan",
        "JerrycanFire": "Jerrycan Fire",
        "Lava": "Lava",
        "Mortar_Projectile_C": "Mortar Projectile",
        "None": "None",
        "PG117_A_01_C": "PG-117",
        "PanzerFaust100M_Projectile_C": "Panzerfaust Projectile",
        "PlayerFemale_A_C": "Player",
        "PlayerMale_A_C": "Player",
        "ProjC4_C": "C4",
        "ProjGrenade_C": "Frag Grenade",
        "ProjIncendiary_C": "Incendiary Projectile",
        "ProjMolotov_C": "Molotov Cocktail",
        "ProjMolotov_DamageField_Direct_C": "Molotov Cocktail Fire Field",
        "ProjStickyGrenade_C": "Sticky Bomb",
        "RacingDestructiblePropaneTankActor_C": "Propane Tank",
        "RacingModeContorller_Desert_C": "Bluezone",
        "RedZoneBomb_C": "Redzone",
        "RedZoneBombingField": "Redzone",
        "RedZoneBombingField_Def_C": "Redzone",
        "TslDestructibleSurfaceManager": "Destructible Surface",
        "TslPainCausingVolume": "Lava",
        "Uaz_A_01_C": "UAZ (open top)",
        "Uaz_Armored_C": "UAZ (armored)",
        "Uaz_B_01_C": "UAZ (soft top)",
        "Uaz_B_01_esports_C": "UAZ (soft top)",
        "Uaz_C_01_C": "UAZ (hard top)",
        "UltAIPawn_Base_Female_C": "Player",
        "UltAIPawn_Base_Male_C": "Player",
        "WeapACE32_C": "ACE32",
        "WeapAK47_C": "AKM",
        "WeapAUG_C": "AUG A3",
        "WeapAWM_C": "AWM",
        "WeapBerreta686_C": "S686",
        "WeapBerylM762_C": "Beryl",
        "WeapBizonPP19_C": "Bizon",
        "WeapCowbarProjectile_C": "Crowbar Projectile",
        "WeapCowbar_C": "Crowbar",
        "WeapCrossbow_1_C": "Crossbow",
        "WeapDP12_C": "DBS",
        "WeapDP28_C": "DP-28",
        "WeapDesertEagle_C": "Deagle",
        "WeapDuncansHK416_C": "M416",
        "WeapFNFal_C": "SLR",
        "WeapG18_C": "P18C",
        "WeapG36C_C": "G36C",
        "WeapGroza_C": "Groza",
        "WeapHK416_C": "M416",
        "WeapJuliesKar98k_C": "Kar98k",
        "WeapK2_C": "K2",
        "WeapKar98k_C": "Kar98k",
        "WeapL6_C": "Lynx AMR",
        "WeapLunchmeatsAK47_C": "AKM",
        "WeapM16A4_C": "M16A4",
        "WeapM1911_C": "P1911",
        "WeapM249_C": "M249",
        "WeapM24_C": "M24",
        "WeapM9_C": "P92",
        "WeapMG3_C": "MG3",
        "WeapMP5K_C": "MP5K",
        "WeapMP9_C": "MP9",
        "WeapMacheteProjectile_C": "Machete Projectile",
        "WeapMachete_C": "Machete",
        "WeapMadsQBU88_C": "QBU88",
        "WeapMini14_C": "Mini 14",
        "WeapMk12_C": "Mk12",
        "WeapMk14_C": "Mk14 EBR",
        "WeapMk47Mutant_C": "Mk47 Mutant",
        "WeapMosinNagant_C": "Mosin-Nagant",
        "WeapNagantM1895_C": "R1895",
        "WeapOriginS12_C": "O12",
        "WeapP90_C": "P90",
        "WeapPanProjectile_C": "Pan Projectile",
        "WeapPan_C": "Pan",
        "WeapPanzerFaust100M1_C": "Panzerfaust",
        "WeapQBU88_C": "QBU88",
        "WeapQBZ95_C": "QBZ95",
        "WeapRhino_C": "R45",
        "WeapSCAR-L_C": "SCAR-L",
        "WeapSKS_C": "SKS",
        "WeapSaiga12_C": "S12K",
        "WeapSawnoff_C": "Sawed-off",
        "WeapSickleProjectile_C": "Sickle Projectile",
        "WeapSickle_C": "Sickle",
        "WeapThompson_C": "Tommy Gun",
        "WeapTurret_KillTruck_Main_C": "Kill Truck Turret",
        "WeapUMP_C": "UMP9",
        "WeapUZI_C": "Micro Uzi",
        "WeapVSS_C": "VSS",
        "WeapVector_C": "Vector",
        "WeapWin94_C": "Win94",
        "WeapWinchester_C": "S1897",
        "Weapvz61Skorpion_C": "Skorpion"
    }
    return weapons


def attacker_victim(tele, include_pregame=False):
    start = datetime.datetime.strptime(tele.filter_by("log_match_start")[0].timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")
    damages = {}
    attack_events = tele.filter_by("log_player_attack")
    attackers = {}
    for event in attack_events:
        attackers[event.attack_id] = event.attacker

    damage_events = tele.filter_by("log_player_take_damage")
    for event in damage_events:
        try:
            attacker = event.attacker.name
        except AttributeError:
            continue
        if attacker != "":
            timestamp = datetime.datetime.strptime(event.timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")
            #  게임 시작 후 지속된 시간
            dt = (timestamp - start).total_seconds()
            if (not include_pregame and dt < 0) or event.attack_id == -1:
                continue
            if attacker not in damages:
                damages[attacker] = []
            # inconsistencies here can sometimes result in missing attack ids
            try:
                attacker_data = attackers[event.attack_id]
            except KeyError:
                continue
            damages[attacker].append(
                (
                    dt,                         # 시간
                    attacker_data.name,         # 공격자 이름
                    event.victim.name,          # 피해자 이름
                    event.damage,               # 피해량
                    event.damage_causer_name,   # 피해 원인
                    event.damage_reason,        # 피해 종류 (맞은 부위 등..)

                )
            )
    return damages


# 맵과 상관없이 유저의 평균 데이터를 가져온다.
def personal_anal():
    import pandas as pd
    from chicken_dinner.pubgapi import PUBG
    from chicken_dinner.pubgapi import PUBGCore
    from chicken_dinner.constants import map_dimensions
    import time
    import numpy as np
    import os
    import warnings
    warnings.filterwarnings('ignore')

    # API KEY 설정
    api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2ZGNjNzNhMC0yMDk5LTAxMzctYjNjMi0wMmI4NjZkNzliOGIiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTUxNjk2NzA2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InB1YmctYmVzdC1wbGF5In0.Oz7GmLsWF7038XIO4vKd5sivhLreOnizxTNcARAEFQs'
    # PUBG 인스턴스 가져오기
    pubg = PUBG(api_key=api_key, shard='pc-tournament', gzip=True)

    pgc_data = pd.read_csv("C:/Users/HC/PycharmProjects/pubgProject/MatchList/datas/pgc/PGC_MATCH.csv")
    # 남은 데이터 확인
    leng = len(pgc_data)

    attack_df = pd.DataFrame()
    blue_df = pd.DataFrame()
    teamCount = {}
    firstVehicle_df = pd.DataFrame()

    # 전체 데이터
    all_attacker_victim_df = pd.DataFrame()
    personal_df = pd.DataFrame(columns=['teamName', 'userName', "damageDealt", "damageTaken", "damageMagnetic", "playCount", "mainWeapon"])


    for cnt, mat in enumerate(pgc_data['match_id']):
        current_match = pubg.match(mat)  # 매치 기록 하나를 가져옴
        telemetry = current_match.get_telemetry()  # 현재 매치의 Telemetry값을 가져옴
        positions = telemetry.player_positions()  # 각플레이어의 위치값을 가져온다.
        circles = telemetry.circle_positions()  # 자기장(원)에 대한 위치 정보를 가져온다. (white, blue, red)
        players = np.array(telemetry.player_names())  # 매치에 참가한 플레이어 목록

        # 게임 시작 시간
        startTime = pd.to_timedelta(telemetry.started()[telemetry.started().find('T') + 1:-1])
        endTime = telemetry.events[-1].timestamp  # 마지막 이벤트 시간
        endTime = (pd.to_timedelta(endTime[endTime.find('T') + 1:-1]) - startTime).total_seconds()
        circles = telemetry.circle_positions()
        whites = np.array(circles['white'])
        phases = np.where(whites[1:, 4] - whites[:-1, 4] != 0)[0] + 1
        phaseTimes = whites[phases, 0]
        phaseTimes = np.append(phaseTimes, endTime)

        # 플레이어 하나씩 진행
        for player in players:
            # 이미 저장된 데이터는 생략
            if os.path.isfile("C:/Users/HC/PycharmProjects/pubgProject/MatchList/datas/pgc/Anal/" + mat + "_" + player + ".csv"):
                print(leng, "개 데이터 중,", cnt + 1, "번째 매치의 플레이어 :", player  ," 의 정보 SKIP")
                continue
            print("C:/Users/HC/PycharmProjects/pubgProject/MatchList/datas/pgc/Anal/" + mat + "_" + player + ".csv")
            curpos = np.array(positions[player])  # 해당 플레이어의 위치 정보를 가져옴

            # 자기장(흰 원)이 존재하지 않는 데이터를 제외
            white_count = 0
            while len(circles['white']) < len(curpos): curpos = curpos[:-1]
            while circles['white'][white_count][4] == 0: white_count += 1
            length = len(curpos)
            landing = np.where(curpos[:, 3] < 30000)[0][0]  # z좌표(높이)를 확인해서 비행기에서 내린 이후 특정 높이 이하로 내려온 처음 값을 지정(플에이어 마다 다름)
                                                            # 비행기에서 내린 시점과 자기장 정보가 등록된 정보의 길이를 비교하여 시작점을 지정 -> 일반적으로 자기장이 더욱 짧음 하지만 예외는 존재
            start = landing if landing > white_count else white_count

            # 사람 위치 정보 최대 길이에 맞춰 자기장 정보 가져오기 ( 사실상 흰 자기장의 끝 길이에 맞춤, curpos는 white에 맞춰짐)
            curpos = curpos[start:]  # 설정된 start 값 이전 값은 제외
            whites = np.array(circles['white'])[start:length]
            blues = np.array(circles['blue'])[start:length]

            # 사람 위치 정보를 white, blue 존에서 부터 거리의 차를 x,y축으로 나눠 저장
            map_id = telemetry.map_id()  # 해당 매치의 맵 이름을 반환
            mapx, mapy = map_dimensions[map_id]
            phases = np.where(whites[1:, 4] - whites[:-1, 4] < 0)[0] + 1  # 자기장 페이즈 구분

            vehicles = telemetry.filter_by('log_vehicle_ride')  # 차량 탑승 데이터
            firstVehicle = {}
            used_Id = []

            # 팀에서 첫 차량 탑승 경우만 구하기
            for vehicle in vehicles:
                if vehicle['vehicle']['vehicle_type'] != 'WheeledVehicle' or vehicle['character']['name'] in \
                        firstVehicle.keys() or vehicle['character']['name'] in used_Id:
                    continue
                else:
                    firstVehicle[vehicle['character']['name']] = (pd.to_timedelta(vehicle.timestamp[vehicle.timestamp.find('T') + 1:-1]) - startTime).total_seconds()
                    used_Id.append(vehicle['character']['name'])
            vehicle_df = pd.DataFrame(list(firstVehicle.items()), columns=["name", "time"])
            firstVehicle_df = pd.concat([firstVehicle_df, vehicle_df], axis=0, sort=False,  ignore_index=True)


        
        # 공격 로그 (교전횟수 또는 총기 사용량 파악을 위함) 
        attackLog = telemetry.filter_by('log_player_attack')  # 교전 (공격한 경우) 데이터
        attackData = [(log['attacker']['name'],
                       (pd.to_timedelta(log.timestamp[log.timestamp.find('T') + 1:-1]) - startTime).total_seconds())
                      for log in attackLog if
                      pd.to_timedelta(log.timestamp[log.timestamp.find('T') + 1:-1]) > startTime]
        attackData = pd.DataFrame(attackData, columns=['name', 'time'])
        attackData['teamName'] = attackData['name'].str.extract(r'([0-9A-Za-z]+)\_')  # 팀명 추출
        attackData['phase'] = np.nan

        for i in range(len(phaseTimes) - 1):
            attackData.loc[
                (attackData['time'] < phaseTimes[i + 1]) & (attackData['time'] > phaseTimes[i]), 'phase'] = i + 1
        attack_df = pd.concat([attack_df, attackData], axis = 0)

        for team in attackData['teamName'].unique():
            try:
                teamCount[team] += 1
            except KeyError:
                teamCount[team] = 1

        # 블루존 데미지 (기절해서 입는 피해량은 0으로 나옴)
        blueZoneLog = telemetry.filter_by("log_player_take_damage")

        blueData = [(log['victim']['name'], log['damage'],
                       (pd.to_timedelta(log.timestamp[log.timestamp.find('T') + 1:-1]) - startTime).total_seconds())
                      for log in blueZoneLog if
                      pd.to_timedelta(log.timestamp[log.timestamp.find('T') + 1:-1]) > startTime and
                    log['damage_type_category'] == "Damage_BlueZone"]

        blueData = pd.DataFrame(blueData, columns=['victim', 'damage', 'time'])
        blueData['victim_teamName'] = blueData['victim'].str.extract(r'([0-9A-Za-z]+)\_')  # 팀명 추출
        blueData['phase'] = np.nan
        for i in range(len(phaseTimes) - 1):
            blueData.loc[
                (blueData['time'] < phaseTimes[i + 1]) & (blueData['time'] > phaseTimes[i]), 'phase'] = i + 1
        blue_df = pd.concat([blue_df, blueData], axis=0)
        for team in blueData['victim_teamName'].unique():
            try:
                teamCount[team] += 1
            except KeyError:
                teamCount[team] = 1

        # 공격자, 피해자 로그 (누가 누구에게 피해를 줬는가 파악 가능
        attacker_victim_data = attacker_victim(telemetry)
        attacker_victim_df = pd.DataFrame()

        for key, value in attacker_victim_data.items():
            for row in value:
                attacker_victim_df = attacker_victim_df.append({"match_id": mat,
                                                                "time": row[0],
                                                                "attacker": row[1],
                                                                "victim": row[2],
                                                                "damage": row[3],
                                                                "hit_type": row[4],
                                                                "hit_area": row[5],
                                                                }, ignore_index=True)
        for i in range(len(phaseTimes) - 1):
            attacker_victim_df.loc[
                (attacker_victim_df['time'] < phaseTimes[i + 1]) & (
                            attacker_victim_df['time'] > phaseTimes[i]), 'phase'] = i + 1

        all_attacker_victim_df = pd.concat([all_attacker_victim_df, attacker_victim_df], ignore_index=True)
        # 이해하기 어렵게 작성된 총 이름을 정식 명칭(?)으로 맵핑하기 위한 정보
        weapons = weapon_mapping()

        print(leng, "개 데이터 중,", cnt + 1, "번 째 매치 데이터 진행 중.....")

    firstVehicle_team = pd.concat([firstVehicle_df[['name', 'time']].groupby('name').mean(),
                                   firstVehicle_df[['name', 'time']].groupby('name').count()], axis=1,
                                  sort=False)
    firstVehicle_team.columns = ['time', 'count']
    print(firstVehicle_team)
    # firstVehicle_team = firstVehicle_team[firstVehicle_team['count'] > 10]        # 게임 참가 횟수 10회 이상 팀만






if __name__ == "__main__":
    personal_anal()
