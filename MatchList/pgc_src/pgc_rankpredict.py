import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 데이터 불러오기
data = pd.read_csv("../datas/pgc/MATCH_ALL_STAT.csv")

# 결측치 확인
# print(data.isnull().sum())

# 결측치 제거
data.dropna(axis=0, inplace=True)
data.reset_index(drop=True, inplace=True)

###############################################################
#########################  이상치 제거  #########################
###############################################################

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

print(data.columns)
# 이동거리가 없지만 적을 죽임 --> 이상치로 판단한다
# Train, Test 이동거리 (차,수영,걷기 합)
data['total_distance'] = data.ride_distance + data.walk_distance + data.swim_distance
data['kills_without_moving'] = ((data['kills'] > 0) & (data['total_distance'] == 0))
# 이동거리가 0인데 킬수가 존재하는 데이터 counting
# print(test['kills_without_moving'].value_counts())
# 이상치 제거
data.drop(data[data['kills_without_moving'] == True].index, inplace=True)

# 로드킬의 이상치를 판별하기 위해 roadKills counting
# print(data['road_kills'].value_counts())
# 9킬 이상부터 데이터의 수가 적어지므로 10킬 초과부터 이상치로 판단 (낮은 데이터를 전부 제거하면 분별력에서 문제발생가능성이 있다)
data.drop(data[data['road_kills'] > 10].index, inplace=True)

# 최대거리 킬로 판별 -> 핵 또는 기절 시키고 이동해 죽였을 때 거리가 비정상적으로 늘어난 경우 (실제로 간혹 존재할 수 있지만 그냥 제거)
# print(data[data['longest_kill'] >= 800])
# print(len(data[data['longest_kill'] >= 800]))
data.drop(data[data['longest_kill'] >= 800].index, inplace=True)

# 이동거리 관련
''' 경고 메시지 나옴.. (그래프는 표시)
# walkDistance
plt.figure(figsize=(12, 4))
sns.distplot(train['walk_distance'], bins=10)
plt.show()
# rideDistance
plt.subplots(figsize=(12, 4))
sns.distplot(train.ride_distance, bins=10)
plt.show()
# swimDistance
plt.subplots(figsize=(12, 4))
sns.distplot(train.swim_distance, bins=10)
plt.show()'''
# data.drop(data[data['walk_distance'] >= 10000].index, inplace=True)
# data.drop(data[data['ride_distance'] >= 14000].index, inplace=True)
# data.drop(data[data['swim_distance'] >= 1500].index, inplace=True)    # 예전에는 자기장이 물에도 잡혔기 때문에 이를 무시하기 어려움..
# data.drop(data[data['total_distance'] >= 15000].index, inplace=True)

# 무기획득 -> 40회 이상 습득 제거
# print(data["weapons_acquired"].value_counts())
data.drop(data[data.weapons_acquired >= 40].index, inplace=True)

print(data["map_name"].value_counts())
data.loc[data['map_name'] == "Erangel", 'map_name'] = 'Erangel (Remastered)'
print(data["map_name"].value_counts())
# 체력회복 관련
data.drop(data[data.heals >= 40].index, inplace=True)
data.drop(data[data.boosts >= 40].index, inplace=True)

# 범주형 변수 수치?화

# data = pd.get_dummies(data, columns=['map_name'])


# 분석에 사용하지 않을 데이터 제거
data.drop(['death_type', 'name', 'player_id', 'team_name', 'match_id', 'created_at', 'telemetry_link', 'team_roster_id',\
            'team_member', 'team_rank', 'team_kill', 'team_assist', 'team_distance', 'total_distance',
            'team_damagedealt', 'team_damagetaken', 'team_timesurvived', "kills_without_moving"], axis=1, inplace=True)
print(data.columns)