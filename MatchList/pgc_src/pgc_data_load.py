# 대회 기록 - PGC 데이터를 사용
# 데이터 분석에 활용할 데이터를 추출
import sys
import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from operator import itemgetter
from matplotlib.patches import Rectangle


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



# 맵과 상관없이 유저의 평균 데이터를 가져온다.
def personal_data():
    import pandas as pd
    from chicken_dinner.pubgapi import PUBG
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


    match_participant_stats_all = pd.read_csv(r"..\datas\pgc\Anal\All\All_participant_stats.csv")
    attacker_victim_all = pd.read_csv(r"..\datas\pgc\Anal\All\All_attacker_victim.csv")
    justAttack_df = pd.read_csv(r"..\datas\pgc\Anal\All\All_shooting.csv")
    blue_df = pd.read_csv(r"..\datas\pgc\Anal\All\All_bluezone_damage.csv")
    firstVehicle_df = pd.read_csv(r"..\datas\pgc\Anal\All\All_first_vehicle.csv")
    # 매치 리스트를 불러와 저장 (매치별 데이터)
    match_list = justAttack_df['match_id'].unique()
    # 자기장이 시작되기 전에 발생한 이벤트는 phase가 None값으로 설정되어 있어 이를 0 값으로 대체
    justAttack_df.fillna(0, inplace=True)


    '''justAttack_df = justAttack_df.groupby(['match_id', 'teamName', 'name', 'phase']).count()
    justAttack_df.columns = ['shoot']       # 발사 횟수를 shoot 칼럼으로 이름 지정
    # 매치별, 아이디별 총기 사용횟수 확인 가능.. -> groupby로 묶으면 출력 및 분석하는데 생각보다 불편함.. 정확히 추출하는 방법을 찾아내거나 기존 DF에서
    # 관련 데이터를 추출해서 분석에 활용할 정보를 찾는게 좋을듯 함.'''

    match_participant_stats_all = pd.merge(match_participant_stats_all, firstVehicle_df, on=['match_id', 'name'])
    match_participant_stats_all.to_csv(r"..\datas\pgc\Anal\All\predict_rank.csv", index=False)




    winner_df = pd.DataFrame()
    loser_df = pd.DataFrame()
    # # 1등 기록만 분류하여 평균
    # for match in match_list:
    #     match_df = match_participant_stats_all[match_participant_stats_all["match_id"] == match]
    #
    #     winner_data = match_df[match_df['win_place'] == 1]
    #     winner_name = list(winner_data['name'])
    #     winner_team = winner_name[0][:winner_name[0].find("_")+1]   # 팀명 + 언더바(_)까지 추출하여 해당 문자열을 포함하는 데이터를 추출
    #
    #     loser_data = match_df[match_df['win_place'] == 16]
    #     loser_name = list(loser_data['name'])
    #     loser_team = loser_name[0][:loser_name[0].find("_") + 1]  # 팀명 + 언더바(_)까지 추출하여 해당 문자열을 포함하는 데이터를 추출
    #
    #     winner_df = pd.concat([winner_df, winner_data], ignore_index=True)
    #     loser_df = pd.concat([loser_df, loser_data], ignore_index=True)
    # print(winner_df['time'].mean())
    # print()
    # print(loser_df['time'].mean())



# 개인 기록을 가지고 순위를 예측 하는 함수 ( 팀의 평균 )
def predict_rank():
    from sklearn.model_selection import train_test_split

    data = pd.read_csv(r"..\datas\pgc\Anal\All\predict_rank.csv")
    '''
        일반적으로
            r이 -1.0과 -0.7 사이면, 강한 음적 선형관계,
            r이 -0.7과 -0.3 사이면, 뚜렷한 음적 선형관계,
            r이 -0.3과 -0.1 사이면, 약한 음적 선형관계,
            r이 -0.1과 +0.1 사이면, 거의 무시될 수 있는 선형관계,
            r이 +0.1과 +0.3 사이면, 약한 양적 선형관계,
            r이 +0.3과 +0.7 사이면, 뚜렷한 양적 선형관계,
            r이 +0.7과 +1.0 사이면, 강한 양적 선형관계

        순위가 1~16위로 숫자가 낮을수록 잘했다는 의미 이므로 반대로 해석하면 된다. 
        음의 상관관계 -> 양의 상관관계

        dbnos              -0.330664        음의 상관관계
        assists            -0.338207        음의 상관관계
        boosts             -0.420644        음의 상관관계
        damage_dealt       -0.492121        음의 상관관계
        headshot_kills     -0.243569        약한 음의 상관관계
        heals              -0.239659        약한 음의 상관관계
        kill_place          0.582664        양의 상관관계
        kill_streaks       -0.345609        음의 상관관계
        kills              -0.407835        음의 상관관계
        longest_kill       -0.309572        음의 상관관계
        revives            -0.183836        약한 음의 상관관계
        ride_distance       0.016419        관게 없음
        road_kills         -0.003751        관계 없음
        swim_distance      -0.007492        관계 없음
        team_kills          0.006575        관계 없음
        time_survived      -0.709716        강항 음의 상관관계
        vehicle_destroys   -0.160648        약한 음의 상관관계
        walk_distance      -0.452229        음의 상관관계
        weapons_acquired   -0.101177        약한 음의 상관관계
        damage_taken       -0.361826        음의 상관관계
        time                0.010637        관계없음 (차량탑승 시간)
    '''
    death_type = {
        'byplayer': 0,
        'alive': 1,
        'byzone': 2,
        'suicide': 3
    }
    # 상관관계 분석
    corrAnal = data[['dbnos', 'assists', 'boosts', 'damage_dealt', 'death_type',
                                       'headshot_kills', 'heals', 'kill_place', 'kill_streaks', 'kills',
                                       'longest_kill', 'revives', 'ride_distance',
                                       'road_kills', 'swim_distance', 'team_kills', 'time_survived',
                                       'vehicle_destroys', 'walk_distance', 'weapons_acquired',
                                       'damage_taken', 'time', 'win_place']]
    corrAnal['death_type'] = corrAnal['death_type'].map(lambda x: death_type[x])
    '''
    cor = corrAnal.corr()
    # print(cor['win_place'])
    
    sns.set(style="white")

    f, ax = plt.subplots(figsize=(14, 14))
    cmap = sns.diverging_palette(200, 10, as_cmap=True)

    mask = np.zeros_like(cor, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    sns.heatmap(cor, mask=mask, cmap=cmap, center=0.5, square=True,
                linewidths=0.5, cbar_kws={"shrink": 0.75}, annot=True)

    plt.title('ranking correlation', size=30)
    ax.set_xticklabels(list(corrAnal.columns), size=14, rotation=90)
    ax.set_yticklabels(list(corrAnal.columns), size=14, rotation=0)

    for temp_num in range(len(corrAnal.columns)):
        ax.add_patch(Rectangle((temp_num, temp_num), 1, 1, fill=False,
                               edgecolor='black', lw=1, clip_on=False, alpha=0.5))

    plt.show()'''


    # 모델 생성
    # 데이터 내에 문자열 데이터 숫자로 변환
    print(corrAnal.columns)
    # feature, label 분리
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    winner_rank_f = corrAnal.drop("win_place", axis=1)

    """ 정규화가 필요할 것 같은 칼럼
    # 피해량 관련 ->
    damage_dealt
    damage_taken
    
    # 거리 관련 -> ??
    longest_kill
    ride_distance
    swim_distance
    walk_distance
    
    # 시간 관련 -> duration으로 나눠주면 게임 내의 % 계산 가능
    time_survived
    time
    """

    winner_rank_f = scaler.fit_transform(winner_rank_f)
    print(winner_rank_f)
    winner_rank_l = corrAnal['win_place'].copy()
    # # Train, Test 분류
    # X_train, X_test, Y_train, Y_test = train_test_split(winner_rank_f, winner_rank_l, test_size=0.3, random_state=42)
    # # Test, Validation 분류
    # X_test, X_val, Y_test, Y_val = train_test_split(X_test, Y_test, test_size=0.3)



    return
    






if __name__ == "__main__":
    # personal_data()
    predict_rank()