import joblib   # 모델 저장, 불러오기
import pandas as pd
from sklearn.metrics import mean_absolute_error
import numpy as np

data = pd.read_csv("../datas/mydata/All_data.csv")

model = joblib.load("../datas/pgc/rank_predict/lgbm_model.h5")

choose_data = data[['dbnos', 'assists', 'boosts', 'damage_dealt', 'headshot_kills', 'heals',
       'kill_place', 'kill_streaks', 'kills', 'longest_kill', 'revives',
       'ride_distance', 'road_kills', 'swim_distance', 'team_kills',
       'time_survived', 'vehicle_destroys', 'walk_distance',
       'weapons_acquired', 'win_place', 'damage_taken', 'map_name', 'duration',
       'total_distance']]

spac = choose_data[choose_data['map_name'].str.contains("테이고")].index
choose_data.drop(spac, inplace=True)
print(choose_data["map_name"].value_counts())


# 맵 이름을 맵핑하기 위해 설정 (대회 기록으로 학습시킨 데이터를 경쟁전 데이터를 입력하므로 맵의 종류가 다름)
map_ecoding = {'에란겔':0, '미라마':1}
choose_data.replace({"map_name":map_ecoding}, inplace=True)
print(choose_data["map_name"].value_counts())
print(choose_data.info())
test_data = choose_data.drop(columns=['win_place'])
rank_data = choose_data['win_place']

model_predict = model.predict(test_data)
print(np.around(model_predict))

# print(model_predict)
# print(rank_data)

print('mae : ', mean_absolute_error(np.around(model_predict), rank_data))

for i, j in zip(np.around(model_predict), rank_data):
       print(i, j)

