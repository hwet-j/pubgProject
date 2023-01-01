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



def pro_anal():
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
    pubgCore = PUBGCore(api_key=api_key, shard='pc-tournament', gzip=True)

    pgc_data = pd.read_csv("C:/Users/HC/PycharmProjects/pubgProject/MatchList/datas/pgc/PGC_MATCH.csv")
    # 전체 데이터를 저장할 데이터 프레임
    all_data = pd.DataFrame()
    # 남은 데이터 확인
    leng = len(pgc_data)

    attack_df = pd.DataFrame()
    blue_df = pd.DataFrame()
    teamCount = {}
    whiteCenter_df = pd.DataFrame()
    blueBorder_df = pd.DataFrame()
    playerMove_df = pd.DataFrame()
    firstVehicle_df = pd.DataFrame()

    # 전체 데이터
    all_attacker_victim_df = pd.DataFrame()


    for cnt, mat in enumerate(pgc_data['match_id']):
        # 이미 저장된 데이터는 생략
        if os.path.isfile(
                "C:/Users/HC/PycharmProjects/pubgProject/MatchList/datas/pgc/Anal/" + mat + ".csv") or cnt == 2:
            print(leng, "개 데이터 중,", cnt + 1, "번째 데이터 SKIP")
            break
        current_match = pubg.match(mat)  # 매치 기록 하나를 가져옴
        telemetry = current_match.get_telemetry()  # 현재 매치의 Telemetry값을 가져옴
        positions = telemetry.player_positions()  # 각플레이어의 위치값을 가져온다.
        circles = telemetry.circle_positions()  # 자기장(원)에 대한 위치 정보를 가져온다. (white, blue, red)
        players = np.array(telemetry.player_names())  # 매치에 참가한 플레이어 목록

        whiteCenter_means = {}
        blueBorder_means = {}
        playerMove_means = {}

        # 플레이어 하나씩 진행
        for player in players:
            curpos = np.array(positions[player])  # 해당 플레이어의 위치 정보를 가져옴

            # 자기장(흰 원)이 존재하지 않는 데이터를 제외
            white_count = 0
            while len(circles['white']) < len(curpos): curpos = curpos[:-1]
            while circles['white'][white_count][4] == 0:
                white_count += 1
            length = len(curpos)
            landing = np.where(curpos[:, 3] < 30000)[0][0]  # z좌표(높이)를 확인해서 비행기에서 내린 이후 특정 높이 이하로 내려온 처음 값을 지정(플에이어 마다 다름)
            # 비행기에서 내린 시점과 자기장 정보가 등록된 정보의 길이를 비교하여 시작점을 지정 -> 일반적으로 자기장이 더욱 짧음 하지만 예외는 존재
            start = landing if landing > white_count else white_count

            # 사람 위치 정보 최대 길이에 맞춰 자기장 정보 가져오기 ( 사실상 흰 자기장의 끝 길이에 맞춤, curpos는 white에 맞춰짐)
            curpos = curpos[start:]  # 설정된 start 값 이전 값은 제외
            whites = np.array(circles['white'])[start:length]
            blues = np.array(circles['blue'])[start:length]

            # 사람 위치 정보를 white, blue 존에서 부터 거리의 차를 x,y축으로 나눠 저장
            white_xDiff = (whites[:, 1] - curpos[:, 1])  # 하얀 자기장 x 좌료 이전값과의 차
            white_yDiff = (whites[:, 2] - curpos[:, 2])  # 하얀 자기장 y 좌표 이전값과의 차
            blue_xDiff = (blues[:, 1] - curpos[:, 1])  # 파란 자기장 x 좌표 이전값과의 차
            blue_yDiff = (blues[:, 2] - curpos[:, 2])  # 파란 자기장 y 좌표 이전값과의 차
            map_id = telemetry.map_id()  # 해당 매치의 맵 이름을 반환
            mapx, mapy = map_dimensions[map_id]
            phases = np.where(whites[1:, 4] - whites[:-1, 4] < 0)[0] + 1  # 자기장 페이즈 구분
            phases = np.append(phases, len(whites))  # 게임 종료 index 추가
            white_means = []
            blue_means = []
            moves = []
            pre = 0  # 이전 자기장을 저장할 변수

            for phase in phases:  # 자기장 별 데이터 분리
                cur_white_xDiff = white_xDiff[pre:phase]  # 현 자기장 페이즈의  x 차
                cur_white_yDiff = white_yDiff[pre:phase]  # 현 자기장 페이즈의  y 차
                cur_blue_xDiff = blue_xDiff[pre:phase]
                cur_blue_yDiff = blue_yDiff[pre:phase]

                # white, blue zone로 부터의 거기를 계산
                whiteCenter_diff = np.sqrt(np.square(cur_white_xDiff) + np.square(cur_white_yDiff)) / whites[pre:phase,
                                                                                                      4]
                blueBorder_diff = (blues[pre:phase, 4] - np.sqrt(
                    np.square(cur_blue_xDiff) + np.square(cur_blue_yDiff))) / blues[pre:phase, 4]
                white_means.append(whiteCenter_diff.mean())
                blue_means.append(blueBorder_diff.mean())
                # 길이가 1일때 NaN값 오류 발생 (길이가 1인 0값으로 나누어 주게 된다.)
                if len(whiteCenter_diff) == 1:
                    moves.append(0)
                else:
                    moves.append((whiteCenter_diff[1:] - whiteCenter_diff[:-1]).mean())

                pre = phase

            # 자기장 페이즈 별로 저장된 정보를
            whiteCenter_means[player] = white_means
            blueBorder_means[player] = blue_means
            playerMove_means[player] = moves

        whiteCenter_df = pd.concat(
            [whiteCenter_df, pd.DataFrame.from_dict(whiteCenter_means, orient='index').T.mean(axis=1)],
            axis=1, sort=False)
        blueBorder_df = pd.concat(
            [blueBorder_df, pd.DataFrame.from_dict(blueBorder_means, orient='index').T.mean(axis=1)],
            axis=1, sort=False)
        playerMove_df = pd.concat(
            [playerMove_df, pd.DataFrame.from_dict(playerMove_means, orient='index').T.mean(axis=1)],
            axis=1, sort=False)

        # 게임 시작 시간
        startTime = pd.to_timedelta(telemetry.started()[telemetry.started().find('T') + 1:-1])
        endTime = telemetry.events[-1].timestamp  # 마지막 이벤트 시간
        endTime = (pd.to_timedelta(endTime[endTime.find('T') + 1:-1]) - startTime).total_seconds()
        circles = telemetry.circle_positions()
        whites = np.array(circles['white'])
        phases = np.where(whites[1:, 4] - whites[:-1, 4] != 0)[0] + 1
        phaseTimes = whites[phases, 0]
        phaseTimes = np.append(phaseTimes, endTime)
        
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

        print(blue_df)

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

        # print(attacker_victim_df)
        all_attacker_victim_df = pd.concat([all_attacker_victim_df, attacker_victim_df], ignore_index=True)
        # print(all_attacker_victim_df)
        # 이해하기 어렵게 작성된 총 이름을 정식 명칭(?)으로 맵핑하기 위한 정보
        weapons = weapon_mapping()
        

        vehicles = telemetry.filter_by('log_vehicle_ride')  # 차량 탑승 데이터
        firstVehicle = {}
        used_teamId = []

        # 팀에서 첫 차량 탑승 경우만 구하기
        for vehicle in vehicles:
            if vehicle['vehicle']['vehicle_type'] != 'WheeledVehicle' or \
                    vehicle['character']['name'] in firstVehicle.keys() or \
                    vehicle['character']['name'][:vehicle['character']['name'].find('_')] in used_teamId: continue
            firstVehicle[vehicle['character']['name'][:vehicle['character']['name'].find('_')]] = \
                ((pd.to_timedelta(vehicle.timestamp[vehicle.timestamp.find('T') + 1:-1]) - startTime).total_seconds(), \
                 vehicle['character']['location']['x'], mapy - vehicle['character']['location']['y'])
            used_teamId.append(vehicle['character']['name'][:vehicle['character']['name'].find('_')])
        firstVehicle_df = pd.concat([firstVehicle_df, pd.DataFrame(firstVehicle).T], axis=0, sort=False)

        print(leng, "개 데이터 중,", cnt + 1, "번 째 데이터 진행 중.....")

    '''firstVehicle_df = firstVehicle_df.T
    firstVehicle_df.columns = ['time', 'x', 'y']
    firstVehicle_df['teamName'] = firstVehicle_df.index
    firstVehicle_team = pd.concat([firstVehicle_df[['teamName', 'time']].groupby('teamName').mean(),
                                   firstVehicle_df[['teamName', 'time']].groupby('teamName').count()], axis=1,
                                  sort=False)
    firstVehicle_team.columns = ['time', 'count']
    firstVehicle_team = firstVehicle_team[firstVehicle_te+am['count'] > 10]'''



    # 완성된 데이터 저장
    # all_attacker_victim_df.to_csv()



def moveRoute():
    import pandas as pd
    from chicken_dinner.pubgapi import PUBG
    from chicken_dinner.pubgapi import PUBGCore
    from chicken_dinner.constants import map_dimensions
    import time
    import numpy as np
    import os
    import matplotlib.image as mpimg
    import matplotlib.pyplot as plt
    import warnings
    import random
    warnings.filterwarnings('ignore')

    # API KEY 설정
    api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2ZGNjNzNhMC0yMDk5LTAxMzctYjNjMi0wMmI4NjZkNzliOGIiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTUxNjk2NzA2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InB1YmctYmVzdC1wbGF5In0.Oz7GmLsWF7038XIO4vKd5sivhLreOnizxTNcARAEFQs'
    # PUBG 인스턴스 가져오기
    pubg = PUBG(api_key=api_key, shard='pc-tournament', gzip=True)

    pgc_data = pd.read_csv("C:/Users/HC/PycharmProjects/pubgProject/MatchList/datas/pgc/PGC_MATCH.csv")

    # 남은 데이터 확인
    leng = len(pgc_data)

    for cnt, mat in enumerate(pgc_data['match_id']):
        # 이미 저장된 데이터는 생략
        if cnt != 0:
            continue
        current_match = pubg.match(mat)  # 매치 기록 하나를 가져옴
        telemetry = current_match.get_telemetry()  # 현재 매치의 Telemetry값을 가져옴
        positions = telemetry.player_positions()  # 각플레이어의 위치값을 가져온다.
        circles = telemetry.circle_positions()  # 자기장(원)에 대한 위치 정보를 가져온다. (white, blue, red)
        map_id = telemetry.map_id()  # 해당 매치의 맵 이름을 반환
        mapx, mapy = map_dimensions[map_id]
        whites = np.array(circles['white'])
        whites[:,2] = mapy - whites[:,2]
        phases = np.where(whites[1:,4] - whites[:-1,4] != 0)[0] + 1

        fig = plt.figure(figsize=(12,8))
        ax = fig.add_axes([0, 0, 1, 1])
        ax.axis('off')      # 축 삭제

        if map_id == "Desert_Main":
            img_path = "C:/Users/HC/PycharmProjects/pubgProject/MatchList/datas/images/maps/Miramar_Main_No_Text_Low_Res.png"
        else:
            img_path = "C:/Users/HC/PycharmProjects/pubgProject/MatchList/datas/images/maps/Erangel_Main_No_Text_Low_Res.png"
        img = mpimg.imread(img_path)
        ax.imshow(img, extent=[0, mapx, 0, mapy])

        for phase in phases:
            white_circle = plt.Circle((whites[phase][1], whites[phase][2]), whites[phase][4],
                                      edgecolor="w", linewidth=0.7, fill=False, zorder=5)
            ax.add_patch(white_circle)

        startTime = pd.to_timedelta(telemetry.started()[telemetry.started().find('T') + 1:-1])
        unequips = telemetry.filter_by('log_item_unequip')
        landing_locations = {unequip['character']['name']:
                                 (unequip['character']['location']['x'], mapy - unequip['character']['location']['y'],
                                  (pd.to_timedelta(unequip.timestamp[
                                                   unequip.timestamp.find('T') + 1:-1]) - startTime).total_seconds(),
                                  unequip['character']['team_id'])
                             for unequip in unequips if
                             unequip['item']['item_id'] == 'Item_Back_B_01_StartParachutePack_C'}
        landing_locations = pd.DataFrame(landing_locations).T.reset_index()
        landing_locations.columns = ['name', 'x', 'y', 'time', 'teamId']
        landing_locations['teamId'] = landing_locations['teamId'].astype('int64')
        landing_locations['teamName'] = landing_locations['name'].str.extract(r'([0-9A-Za-z]+)\_')


        COLORS = ["chocolate", "red", "bisque", "darkorange", "gold", "blue", "yellow", "olivedrab", "lightgreen",\
                  "lime", "aquamarine", "darkslategray", "cadetblue", "deepskyblue", "steelblue", "indigo", "violet", "mediumorchid"]
        random.shuffle(COLORS)

        # key로 정렬(팀별 분석 진행을 위해)
        positions = dict(sorted(positions.items()))
        num2 = 0
        for num1, player in enumerate(positions.keys()):
            # 팀별로 다른 색 지정
            team_name = player[:player.find("_")]
            if num1 == 0 or team_name == be_team_name:  # 첫 부분, 이전과 팀명이 동일하면 그대로
                be_team_name = team_name    # 이전 데이터의 팀명 저장
                curpos = np.array(positions[player])
                curpos[:, 2] = mapy - curpos[:, 2]
                curlanding = landing_locations[landing_locations['name'] == player]
                curpos = curpos[curpos[:, 0] > curlanding['time'].values[0]]
                ax.plot(curpos[:, 1], curpos[:, 2], '--', c=COLORS[num2], linewidth=2, zorder=15)  # zorder는 layer의 위치 순서(필요에 따라 원하는 팀의 정보를 가장 앞에 표시 가능.
            else:
                num2 += 1
                be_team_name = team_name        # 이전 데이터의 팀명 저장
                curpos = np.array(positions[player])
                curpos[:, 2] = mapy - curpos[:, 2]
                curlanding = landing_locations[landing_locations['name'] == player]
                curpos = curpos[curpos[:, 0] > curlanding['time'].values[0]]
                ax.plot(curpos[:, 1], curpos[:, 2], '--', c=COLORS[num2], linewidth=2, zorder=15)   # zorder는 layer의 위치 순서(필요에 따라 원하는 팀의 정보를 가장 앞에 표시 가능.
                ax.text(curpos[0, 1], curpos[0, 2], team_name, fontsize=10, c=COLORS[num2], zorder=30,
                        bbox = dict(boxstyle="round", ec = (0.2, 0.3, 0.3), fc = (0.4, 0.4, 0.35)))         # bbox는 텍스트 문구를 박스안에 넣어줌.

        plt.show()

if __name__ == "__main__":
    pro_anal()
    # moveRoute()