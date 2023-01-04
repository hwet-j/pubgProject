import pandas as pd




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

# 결측치 확인
# print(train.isnull().sum())
# print(test.isnull().sum())

# 결측치 제거
train.dropna(axis=0, inplace=True)
train.reset_index(drop=True, inplace=True)
# print(train.isnull().sum())

# Train, Test 별 match 수 파악
# print(len(train['matchId'].unique()))
# print(len(test['matchId'].unique()))

# 매치별 참가자 수 파악 (matchId로 그룹화 하여 행개수 파악)
# print(train.groupby('matchId')['matchId'].count())

train['player_num'] = train.groupby('matchId')['matchId'].transform('count')
test['player_num'] = test.groupby('matchId')['matchId'].transform('count')

import matplotlib.pyplot as plt
import seaborn as sns
# 플레이어 수가 ? 이상인 정보만 표시
# plt.subplots(figsize=(15, 8))
# sns.countplot(x="player_num", data=train[train['player_num'] >= 75])
# plt.show()
# https://github.com/AIVenture0/PubG-Win-prediction-using-ML/blob/master/PUBG%20Model%20With%20Limited%20Computation.ipynb

# Train, Test 이동거리 (차,수영,걷기 합)
train['total_distance']=train.rideDistance+train.walkDistance+train.swimDistance
test['total_distance']=test.rideDistance+test.walkDistance+test.swimDistance

# 이동거리가 없지만 적을 죽임 --> 이상치로 판단한다.( 찾아서 제거 )
# train, test
train['kills_without_moving']=((train['kills']>0)&(train['total_distance']==0))
test['kills_without_moving']=((test['kills']>0)&(test['total_distance']==0))
print(test['kills_without_moving'].value_counts())
print()