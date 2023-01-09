import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# https://github.com/AIVenture0/PubG-Win-prediction-using-ML/blob/master/PUBG%20Model%20With%20Limited%20Computation.ipynb

# Train, Test 데이터 불러오기
train = pd.read_csv('../datas/train_V2.csv')
test = pd.read_csv('../datas/test_V2.csv')

# 불러온 데이터 shape 확인
# print(train.shape, test.shape)      # (4446966, 29) (1934174, 28)

# 칼럼 확인
# print(train.columns)
"""
'Id', 'groupId', 'matchId', 'assists', 'boosts', 'damageDealt', 'DBNOs',
'headshotKills', 'heals', 'killPlace', 'killPoints', 'kills',
'killStreaks', 'longestKill', 'matchDuration', 'matchType', 'maxPlace',
'numGroups', 'rankPoints', 'revives', 'rideDistance', 'roadKills',
'swimDistance', 'teamKills', 'vehicleDestroys', 'walkDistance',
'weaponsAcquired', 'winPoints', 'winPlacePerc'
       
Data set

DBNOs - 기절시킨 횟수 (죽이지 못함)

assists - 플레이어가 피해를 줬지만 죽이지 못한 횟수(팀이 죽였거나 적군이 뺏엇을 때)

boosts - 부스트 아이탬 사용 횟수

damageDealt - 입힌 피해량(자기 자신에게 입힌 피해량 제외)

headshotKills - 헤드샷으로 킬한 횟수

heals - 체력 회복아이탬 사용횟수

Id - 플레이어 Id

killPlace - 죽인 플레이어 수에 의한 등수(기준을 모름)

killPoints - 플레이어 킬 기반 외부 순위 - Kills-based external ranking of player. (Think of this as an Elo ranking where only kills matter.) If there is a value other than -1 in rankPoints, then any 0 in killPoints should be treated as a “None”.

killStreaks - Max number of enemy players killed in a short amount of time.

kills - Number of enemy players killed.

longestKill - Longest distance between player and player killed at time of death. This may be misleading, as downing a player and driving away may lead to a large longestKill stat.

matchDuration - Duration of match in seconds.

matchId - ID to identify match. There are no matches that are in both the training and testing set.

matchType - String identifying the game mode that the data comes from. The standard modes are “solo”, “duo”, “squad”, “solo-fpp”, “duo-fpp”, and “squad-fpp”; other modes are from events or custom matches.

rankPoints - Elo-like ranking of player. This ranking is inconsistent and is being deprecated in the API’s next version, so use with caution. Value of -1 takes place of “None”.

revives - Number of times this player revived teammates.

rideDistance - Total distance traveled in vehicles measured in meters.

roadKills - Number of kills while in a vehicle.

swimDistance Total distance traveled by swimming measured in meters.

teamKills - Number of times this player killed a teammate.

vehicleDestroys - Number of vehicles destroyed.

walkDistance - Total distance traveled on foot measured in meters.

weaponsAcquired - Number of weapons picked up.

winPoints - Win-based external ranking of player. (Think of this as an Elo ranking where only winning matters.) If there is a value other than -1 in rankPoints, then any 0 in winPoints should be treated as a “None”.

groupId - ID to identify a group within a match. If the same group of players plays in different matches, they will have a different groupId each time.

numGroups - Number of groups we have data for in the match.

maxPlace - Worst placement we have data for in the match. This may not match with numGroups, as sometimes the data skips over placements.

winPlacePerc - The target of prediction. This is a percentile winning placement, where 1 corresponds to 1st place, and 0 corresponds to last place in the match. It is calculated off of maxPlace, not numGroups, so it is possible to have missing chunks in a match.
"""

###############################################################
########## 결측치 제거(전체 데이터 내에서 결측치 제거  ################
###############################################################
# 결측치 확인
# print(train.isnull().sum())
# print(test.isnull().sum())

# 결측치 제거
train.dropna(axis=0, inplace=True)
train.reset_index(drop=True, inplace=True)
# print(train.isnull().sum())

###############################################################
#########################  이상치 제거  #########################
###############################################################

# Train, Test 별 match 수 파악
# print(len(train['matchId'].unique()))
# print(len(test['matchId'].unique()))

# 매치별 참가자 수 파악 (matchId로 그룹화 하여 행개수 파악)
# print(train.groupby('matchId')['matchId'].count())        # 매치별로 파악하기에는 매치수가 너무 많음

train['player_num'] = train.groupby('matchId')['matchId'].transform('count')
test['player_num'] = test.groupby('matchId')['matchId'].transform('count')

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
# print(train['player_num'].value_counts())

# 그래프로 참가인원별 매치수를 표시
# plt.subplots(figsize=(15, 8))
# sns.countplot(x="player_num", data=train[train['player_num'] >= 60])
# plt.show()

# 75명 이하의 데이터는 제거
train.drop(train[train['player_num'] < 75].index, inplace=True)
test.drop(test[test['player_num'] < 75].index, inplace=True)

# 이동거리가 없지만 적을 죽임 --> 이상치로 판단한다
# Train, Test 이동거리 (차,수영,걷기 합)
train['total_distance'] = train.rideDistance + train.walkDistance + train.swimDistance
test['total_distance'] = test.rideDistance + test.walkDistance + test.swimDistance
train['kills_without_moving'] = ((train['kills'] > 0) & (train['total_distance'] == 0))
test['kills_without_moving'] = ((test['kills'] > 0) & (test['total_distance'] == 0))
# 이동거리가 0인데 킬수가 존재하는 데이터 counting
# print(test['kills_without_moving'].value_counts())
# 이상치 제거
train.drop(train[train['kills_without_moving'] == True].index, inplace=True)
test.drop(test[test['kills_without_moving'] == True].index, inplace=True)

# 로드킬의 이상치를 판별하기 위해 roadKills counting
# print(train['roadKills'].value_counts())
# 9킬 이상부터 데이터의 수가 적어지므로 10킬 초과부터 이상치로 판단 (낮은 데이터를 전부 제거하면 분별력에서 문제발생가능성이 있다)
train.drop(train[train['roadKills'] > 10].index, inplace=True)
test.drop(test[test['roadKills'] > 10].index, inplace=True)

# 개인 킬수로 이상치 감지 -> 25킬 이상부터 (낮은 데이터를 전부 제거하면 분별력에서 문제발생가능성이 있다)
# print(test['kills'].value_counts())
train.drop(train[train['kills'] > 25].index, inplace=True)
test.drop(test[test['kills'] > 25].index, inplace=True)

# 최대거리 킬로 판별 -> 핵 또는 기절 시키고 이동해 죽였을 때 거리가 비정상적으로 늘어난 경우 (실제로 간혹 존재할 수 있지만 그냥 제거)
# print(train[train['longestKill'] >= 800])
# print(len(train[train['longestKill'] >= 800]))
train.drop(train[train['longestKill'] >= 800].index, inplace=True)
test.drop(test[test['longestKill'] >= 800].index, inplace=True)

# 이동거리 관련
''' 경고 메시지 나옴.. (그래프는 표시)
# walkDistance
plt.figure(figsize=(12, 4))
sns.distplot(train['walkDistance'], bins=10)
plt.show()
# rideDistance
plt.subplots(figsize=(12, 4))
sns.distplot(train.rideDistance, bins=10)
plt.show()
# swimDistance
plt.subplots(figsize=(12, 4))
sns.distplot(train.swimDistance, bins=10)
plt.show()'''
# 걷기 관련은 괜찮지만 생각보다 차량의 편차가 커 설정에 어려움이있을듯 함..
train.drop(train[train['walkDistance'] >= 10000].index, inplace=True)
test.drop(test[test['walkDistance'] >= 10000].index, inplace=True)
train.drop(train[train['rideDistance'] >= 14000].index, inplace=True)
test.drop(test[test['rideDistance'] >= 14000].index, inplace=True)
train.drop(train[train['swimDistance'] >= 1500].index, inplace=True)    # 예전에는 자기장이 물에도 잡혔기 때문에 이를 무시하기 어려움..
test.drop(test[test['swimDistance'] >= 1500].index, inplace=True)
train.drop(train[train['total_distance'] >= 15000].index, inplace=True)
test.drop(test[test['total_distance'] >= 15000].index, inplace=True)

# 무기획득 -> 40회 이상 습득 제거
# print(train["weaponsAcquired"].value_counts())
train.drop(train[train.weaponsAcquired >= 40].index, inplace=True)
test.drop(test[test.weaponsAcquired >= 40].index, inplace=True)

# 체력회복 관련
train.drop(train[train.heals >= 40].index, inplace=True)
test.drop(test[test.heals >= 40].index, inplace=True)
train.drop(train[train.boosts >= 40].index, inplace=True)
test.drop(test[test.boosts >= 40].index, inplace=True)

# 범주형 변수 수치?화
train = pd.get_dummies(train, columns=['matchType'])
test = pd.get_dummies(test, columns=['matchType'])
# 직접 레이블을 지정해줘도 되지만 0,1,2,3 으로 설정하게되면 서로 관계성이 있다고 판단될 수 있기 때문에 dummy화 한다. (Ex. 1+3 = 4)

###############################################################
#########################  모델 생성  ##########################
###############################################################
# print(train.info())
# Feature 선택 (분석에 사용할 데이터 선택)
test_id = test['Id']    # 추후에 id로 predict한 결과 비교
train.drop(['kills_without_moving', 'Id', 'groupId', 'matchId', 'matchType_crashfpp', 'matchType_crashtpp', 'matchType_duo', 'player_num',\
            'matchType_duo-fpp', 'matchType_flarefpp', 'matchType_flaretpp', 'matchType_normal-duo-fpp', 'matchType_normal-squad',\
            'matchType_normal-squad-fpp', 'matchType_solo', 'matchType_solo-fpp', 'matchType_squad', 'matchType_squad-fpp',\
            'maxPlace', 'numGroups', 'rankPoints', 'winPoints'], axis=1, inplace=True)
test.drop(['kills_without_moving', 'Id', 'groupId', 'matchId', 'matchType_crashfpp', 'matchType_crashtpp', 'matchType_duo', 'player_num',\
            'matchType_duo-fpp', 'matchType_flarefpp', 'matchType_flaretpp', 'matchType_normal-duo-fpp', 'matchType_normal-squad',\
            'matchType_normal-squad-fpp', 'matchType_solo', 'matchType_solo-fpp', 'matchType_squad', 'matchType_squad-fpp',\
           'maxPlace', 'numGroups', 'rankPoints', 'winPoints'], axis=1, inplace=True)


# print(len(train))
# print(len(test))
# kaggle_data = pd.concat([train, test], axis=0)
# print(len(kaggle_data))

# train.to_csv("../datas/p_train.csv", index=False)
# test.to_csv("../datas/p_test.csv", index=False)
print(train.columns)
# kaggle_data.to_csv("../datas/Kaggle_data.csv", index=False)
import sys
sys.exit()

sample = 500000
df_sample = train.sample(sample)


from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

y = df_sample['winPlacePerc']
X = df_sample.drop(columns=['winPlacePerc'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)

model1 = RandomForestRegressor(n_estimators=40, min_samples_leaf=3, max_features='sqrt', n_jobs=-1)

model1.fit(X_train, y_train)

importance = model1.feature_importances_
# 중요도를 나타내는 값을 데이터프레임화
data = pd.DataFrame(sorted(zip(model1.feature_importances_, X.columns)), columns=['Value', 'Feature'])
# 그래프화
# plt.figure(figsize=(20, 10))
# sns.barplot(x="Value", y="Feature", data=data.sort_values(by="Value", ascending=False))
# plt.show()

# 중요도가 높은 상위 칼럼난 추출
new_data = data.sort_values(by='Value', ascending=False)[:25]
cols = new_data.Feature.values
print(cols)
# 사용할 데이터를 재선택
X_train, X_test, y_train, y_test = train_test_split(X[cols], y, test_size=0.3, random_state=123)
model2 = RandomForestRegressor(n_estimators=40, min_samples_leaf=3, max_features='sqrt', n_jobs=-1)
model2.fit(X_train, y_train)

print('mae train: ', mean_absolute_error(model2.predict(X_train), y_train), 'mae val: ', mean_absolute_error(model2.predict(X_test), y_test))
