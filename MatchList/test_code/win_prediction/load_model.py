import pandas as pd
from keras.models import load_model

# model = load_model('../datas/models/lgbm_model.h5')

data = pd.read_csv(r"C:\Users\HC\PycharmProjects\pubgProject\MatchList\datas\pgc\MATCH_ALL_STAT.csv")

print(data.columns)
print(len(data))

data['total_distance']
data = data[['walk_distance', 'total_distance', 'kill_place', 'weaponsAcquired', 'boosts',
     'heals', 'longestKill', 'matchDuration', 'rideDistance', 'damageDealt',
     'numGroups', 'maxPlace', 'player_num', 'kills', 'killStreaks', 'rankPoints',
     'revives', 'dbnos', 'winPoints', 'killPoints', 'assists', 'swimDistance',
     'headshotKills', 'teamKills', 'roadKills', 'winPlacePerc']]

'''
[['DBNOs', 'assists', 'boosts', 'damageDealt', 'headshotKills',
     'heals', 'killPlace', 'killStreaks', 'kills', 'longestKill',
     'matchDuration', 'revives', 'rideDistance', 'roadKills', 'swimDistance', 
     'vehicleDestroys', 'walkDistance', 'weaponsAcquired', 'total_distance']]
     '''