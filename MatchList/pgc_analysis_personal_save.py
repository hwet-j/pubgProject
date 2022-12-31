# 대회 기록 - PGC 데이터를 사용
# 데이터 분석에 활용할 데이터를 추출
import sys
import datetime

import matplotlib.pyplot as plt


def createDirectory(folderDirectory):
    import os
    try:
        if not os.path.exists(folderDirectory):
            os.makedirs(folderDirectory)
    except OSError:
        print("경로 생성에 실패하였습니다.")



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
    justAttack_df = pd.DataFrame()

    # 전체 데이터
    attacker_victim_all = pd.DataFrame()
    match_participant_stats_all = pd.DataFrame()
    personal_df = pd.DataFrame(columns=['teamName', 'userName', "damageDealt", "damageTaken", "damageMagnetic", "playCount", "mainWeapon"])


    for cnt, mat in enumerate(pgc_data['match_id']):
        if cnt == 1:
            break
        # 폴더 생성 ( 매치 별 )
        fold_path = "C:/Users/HC/PycharmProjects/pubgProject/MatchList/datas/pgc/Anal/" + mat
        createDirectory(fold_path)

        print(leng, "개 데이터 중,", cnt + 1, "번 째 매치 데이터 진행.....")
        current_match = pubg.match(mat)  # 매치 기록 하나를 가져옴
        telemetry = current_match.get_telemetry()  # 현재 매치의 Telemetry값을 가져옴
        positions = telemetry.player_positions()  # 각플레이어의 위치값을 가져온다.
        circles = telemetry.circle_positions()  # 자기장(원)에 대한 위치 정보를 가져온다. (white, blue, red)
        # 매치에 참가한 플레이어 목록
        players = np.array(telemetry.player_names())
        participants = current_match.participants


        # 게임 시작 시간
        startTime = pd.to_timedelta(telemetry.started()[telemetry.started().find('T') + 1:-1])
        endTime = telemetry.events[-1].timestamp  # 마지막 이벤트 시간
        endTime = (pd.to_timedelta(endTime[endTime.find('T') + 1:-1]) - startTime).total_seconds()
        circles = telemetry.circle_positions()
        whites = np.array(circles['white'])
        phases = np.where(whites[1:, 4] - whites[:-1, 4] != 0)[0] + 1
        phaseTimes = whites[phases, 0]
        phaseTimes = np.append(phaseTimes, endTime)


        """
            첫 차량 탑승 경우만 구하기 (시간 순으로 저장)
            vehicle_df : 한 매치에 대한 정보
            firstVehicle_df : 전체 매치에 대한 정보
    
            :param str name: 플레이어 아이디
            :param str time: 이벤트 발생 시간(차량 탑승 시간)
        """
        vehicles = telemetry.filter_by('log_vehicle_ride')  # 차량 탑승 데이터
        firstVehicle = {}
        used_Id = []

        for vehicle in vehicles:
            if vehicle['vehicle']['vehicle_type'] != 'WheeledVehicle' or vehicle['character']['name'] in firstVehicle.keys() or vehicle['character']['name'] in used_Id:
                continue
            else:
                firstVehicle[vehicle['character']['name']] = (pd.to_timedelta(vehicle.timestamp[vehicle.timestamp.find('T') + 1:-1]) - startTime).total_seconds()
                used_Id.append(vehicle['character']['name'])

        # 현재 매치의 데이터
        vehicle_df = pd.DataFrame(list(firstVehicle.items()), columns=["name", "time"])
        vehicle_df['match_id'] = mat
        # 파일저장 (파일 존재시 SKiP)
        if os.path.isfile(fold_path + "/" + "firstvehicle.csv"):
            None
        else:
            vehicle_df.to_csv(fold_path + "/" + "firstvehicle.csv", index=False)
        # 모든 매치 기록의 데이터 병합
        firstVehicle_df = pd.concat([firstVehicle_df, vehicle_df], axis=0, sort=False,  ignore_index=True)


        """
            공격 로그 (교전횟수 또는 총기 사용량 파악을 위함) -> 총기를 몇번 사용하였는지 확인 가능 / 타격 여부 상관없이 발사 횟수
            attackData : 한 매치에 대한 정보
            justAttack_df : 전체 매치에 대한 정보

            :param str name: 플레이어 아이디
            :param str time: 이벤트 발생 시간(총기 사용)
            :param str teamName: 플레이어의 팀명
            :param float phase: 자기장 페이즈
            :param str match_id: 매치 아이디
        """
        attackLog = telemetry.filter_by('log_player_attack')  # 교전 (공격한 경우) 데이터
        attackData = [(log['attacker']['name'],
                       (pd.to_timedelta(log.timestamp[log.timestamp.find('T') + 1:-1]) - startTime).total_seconds())
                      for log in attackLog if
                      pd.to_timedelta(log.timestamp[log.timestamp.find('T') + 1:-1]) > startTime]
        
        attackData = pd.DataFrame(attackData, columns=['name', 'time'])
        attackData['teamName'] = attackData['name'].str.extract(r'([0-9A-Za-z]+)\_')  # 팀명 추출
        attackData['phase'] = np.nan
        attackData['match_id'] = mat

        for i in range(len(phaseTimes) - 1):
            attackData.loc[
                (attackData['time'] < phaseTimes[i + 1]) & (attackData['time'] > phaseTimes[i]), 'phase'] = i + 1
        attack_df = pd.concat([attack_df, attackData], axis = 0)

        for team in attackData['teamName'].unique():
            try:
                teamCount[team] += 1
            except KeyError:
                teamCount[team] = 1

        # 매치 하나의 데이터 저장 (파일 존재시 SKIP)
        if os.path.isfile(fold_path + "/" + "attack_df.csv"):
            None
        else:
            attack_df.to_csv(fold_path + "/" + "attack_df.csv", index=False)
        # 매치 전체 데이터
        justAttack_df = pd.concat([justAttack_df, attack_df], axis=0, sort=False,  ignore_index=True)
        justAttack_df.drop_duplicates(inplace=True)

        """
            블루존 데미지 (기절 상태에서 입는 피해량은 0으로 나옴 -> 다른 것도 동일 )
            blueData : 한 매치에 대한 정보
            blue_df : 전체 매치에 대한 정보

            :param str victim : 피해자
            :param float damage : 피해량 
            :param str time : 이벤트 발생 시간
            :param str victim_teamName : 팀명
            :param float phase: 자기장 페이즈
            :param str match_id: 매치 아이디
        """
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
        blueData['match_id'] = mat

        # 현재 매치의 bluezone 피해량 데이터 저장
        if os.path.isfile(fold_path + "/" + "blueZone.csv"):
            None
        else:
            blueData.to_csv(fold_path + "/" + "blueZone.csv", index=False)

        # 블루존 피해량 전체
        blue_df = pd.concat([blue_df, blueData], axis=0)
        for team in blueData['victim_teamName'].unique():
            try:
                teamCount[team] += 1
            except KeyError:
                teamCount[team] = 1

        """
            공격자, 피해자 로그 (누가 누구에게 피해를 줬는가 파악 가능 - 매치별 분석도 필요하기 때문에 match_id 저장 )
            attacker_victim_df : 한 매치에 대한 정보
            attacker_victim_all : 전체 매치에 대한 정보

            :param str time : 이벤트 발생 시간(플레이어 끼리 공격을 가한 경우)
            :param str attackter : 공격자
            :param str victim : 피해자
            :param float damage : 피해량 
            :param str hit_type : 사용된 무기
            :param str hit_area : 맞은 부위
            :param str match_id: 매치 아이디
        """
        attacker_victim_data = attacker_victim(telemetry)
        attacker_victim_df = pd.DataFrame()

        for key, value in attacker_victim_data.items():
            for row in value:
                attacker_victim_df = attacker_victim_df.append({"match_id" : mat,
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

        # 매치별 데이터 저장
        if os.path.isfile(fold_path + "/" + "attacker_victim.csv"):
            None
        else:
            attacker_victim_df.to_csv(fold_path + "/" + "attacker_victim.csv", index=False)

        # 전체 데이터 병합
        attacker_victim_all = pd.concat([attacker_victim_all, attacker_victim_df], ignore_index=True)
        # 이해하기 어렵게 작성된 총 이름을 정식 명칭(?)으로 맵핑하기 위한 정보
        weapons = weapon_mapping()
        
        # 플레이어 기록을 저장할 리스트(매치마다 초기화) - 연산을 통해 구해지는 데이터는 제외.
        participants_stats = []
        damage_taken = []


        # 플레이어 하나씩 진행
        for part in participants:
            player = part.name

            # 이미 저장된 데이터는 생략 (구분자는 언더바 2개 "__")
            if os.path.isfile(fold_path + "/" + player + ".csv"):
                print(leng, "개 데이터 중,", cnt + 1, "번째 매치의 플레이어 :", player  ," 의 정보 SKIP")
                continue

            # 어떤 매치의 어떤 플레이어 분석인지 Python console에 Print
            # print("매치 ID : " + mat + "\t플레이어 :" + player)
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

            # 플레이어 별 개인 기록
            player_stats = part.stats
            participants_stats.append(player_stats)
            
            try:        # 자기장에 죽었거나, 1등하며 피해를 입지 않은 경우 로그가 존재 하지 않아 오류 발생
                damage_taken.append(telemetry.damage_taken()[player])
            except:
                damage_taken.append(0)      # 플레이어에게 받은 피해량 0

        """
            각 플레이어의 기록
            match_participant_stats_df : 한 매치에 대한 정보
            match_participant_stats_all : 전체 매치에 대한 정보

            :param int dbnos : Down But Not Out 으로 기절 시켰지만 죽이지 못한 횟수
            :param int assists : 도움을 준횟수(킬관련)
            :param int boosts : 부스트 아이템 사용 횟수
            :param float damage_dealt : 가한 피해량
            :param str death_type : 죽음 종류(자기장, 플레이어...)
            :param int headshot_kills : 헤드샷으로 킬한 수
            :param int heals : 체력 회복 아이탬 사용 횟수
            :param int kill_place : 킬로 매긴 순위 (기준이 모호함 -> 제대로 파악 후 사용)
            :param int kill_streaks : 연속 킬수 (시간에 대한 기준은 모름)
            :param int kills : 킬 수 
            :param float longest_kill : 킬 최대 거리
            :param str name : 플레이어 아이디(게임 아이디)
            :param str player_id : 플레이어 고유 번호
            :param int revives : 팀원을 살린 횟수
            :param float ride_distance : 차량 이동거리
            :param int road_kills : 차량으로 죽인 횟수
            :param float swim_distance : 수영으로 이동한 거리
            :param int team_kills : 팀을 죽인 횟수
            :param float time_survived : 생존 시간
            :param int vehicle_destroys : 차량 파괴 횟수
            :param float walk_distance : 걸어서 이동한 거리
            :param int weapons_acquired : 무기 습득 횟수
            :param int win_place : 게임 내 순위
            :param float damage_taken : 받은 피해량
            :param match_id : 매치 고유번호
            :param str created_at : 게임 생성시간
            :param str map_name : 맵 이름
            :param float duration : 게임 지속시간
            :param str telemetry_link : Telemetry의 url 주소를 저장 ( 이후에 어떻게 사용할지 모르기 때문에 )
        """

        match_participant_stats_df = pd.DataFrame(participants_stats)
        match_participant_stats_df['damage_taken'] = damage_taken
        match_participant_stats_df["match_id"] = mat
        match_participant_stats_df["created_at"] = current_match.created_at
        match_participant_stats_df["map_name"] = telemetry.map_name()
        match_participant_stats_df["duration"] = current_match.duration
        match_participant_stats_df["telemetry_link"] = current_match.telemetry_url

        # 매치별 데이터 저장
        if os.path.isfile(fold_path + "/" + "participant_stats.csv"):
            None
        else:
            match_participant_stats_df.to_csv(fold_path + "/" + "participant_stats.csv", index=False)

        match_participant_stats_all = pd.concat([match_participant_stats_all, match_participant_stats_df], ignore_index=True)

    # 차량 탑승 정보 그룹화 -> 다른 분석 코드에서 작성..
    '''
    firstVehicle_team = pd.concat([firstVehicle_df[['name', 'time']].groupby('name').mean(),
                                   firstVehicle_df[['name', 'time']].groupby('name').count()], axis=1,
                                  sort=False)
    firstVehicle_team.columns = ['time', 'count']
    # firstVe0hicle_team = firstVehicle_team[firstVehicle_team['count'] > 10]        # 게임 참가 횟수 10회 이상 팀만'''




    # 전체 데이터 저장 (있어도 덮어씌우기)
    # match_participant_stats_all.to_csv(r"C:\Users\HC\PycharmProjects\pubgProject\MatchList\datas\pgc\Anal\All_participant_stats.csv", index=False)
    # attacker_victim_all.to_csv(r"C:\Users\HC\PycharmProjects\pubgProject\MatchList\datas\pgc\Anal\All_attacker_victim.csv", index=False)
    # justAttack_df.to_csv(r"C:\Users\HC\PycharmProjects\pubgProject\MatchList\datas\pgc\Anal\All_shooting.csv", index=False)
    # blue_df.to_csv(r"C:\Users\HC\PycharmProjects\pubgProject\MatchList\datas\pgc\Anal\All_bluezone_damage.csv", index=False)
    # firstVehicle_df.to_csv(r"C:\Users\HC\PycharmProjects\pubgProject\MatchList\datas\pgc\Anal\All_first_vehicle.csv", index=False)





if __name__ == "__main__":
    personal_anal()
