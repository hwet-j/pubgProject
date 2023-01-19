import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 데이터 불러오기
data = pd.read_csv("./datas/crawl_train_data.csv")

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

# print(data.columns)
# 이동거리가 없지만 적을 죽임 --> 이상치로 판단한다
data['kills_without_moving'] = ((data['kills'] > 0) & (data['total_distance'] == 0))
# 이동거리가 0인데 킬수가 존재하는 데이터 counting
# print(data['kills_without_moving'].value_counts())
# 이상치 제거
data.drop(data[data['kills_without_moving'] == True].index, inplace=True)
data.drop(columns=['kills_without_moving'], inplace=True)

# 로드킬의 이상치를 판별하기 위해 roadKills counting
# print(data['road_kills'].value_counts())
# 9킬 이상부터 데이터의 수가 적어지므로 10킬 초과부터 이상치로 판단 (낮은 데이터를 전부 제거하면 분별력에서 문제발생가능성이 있다)
data.drop(data[data['road_kills'] > 10].index, inplace=True)

# 최대거리 킬로 판별 -> 핵 또는 기절 시키고 이동해 죽였을 때 거리가 비정상적으로 늘어난 경우 (실제로 간혹 존재할 수 있지만 그냥 제거)
# print(data[data['longest_kill'] >= 0.8])
# print(len(data[data['longest_kill'] >= 0.8]))
data.drop(data[data['longest_kill'] >= 0.8].index, inplace=True)

# 이동거리 관련
''' # 경고 메시지 나옴.. (그래프는 표시)
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
# data.drop(data[data['walk_distance'] >= 4.5].index, inplace=True)
# data.drop(data[data['ride_distance'] >= 12.5].index, inplace=True)
# data.drop(data[data['swim_distance'] >= 0.5].index, inplace=True)
# data.drop(data[data['total_distance'] >= 15].index, inplace=True)

# 무기획득 -> 30회 이상 습득 제거
# print(data["weapons_acquired"].value_counts())
data.drop(data[data.weapons_acquired >= 30].index, inplace=True)

# 체력회복 관련
data.drop(data[data.heals >= 40].index, inplace=True)
data.drop(data[data.boosts >= 40].index, inplace=True)

from keras.utils import to_categorical
# 맵 이름을 맵핑하기 위해 설정 (대회 기록이므로 맵이 사실상 2개지만 아마 이벤트성으로 사녹을 진행한 듯함)
map_ecoding = {'에란겔':0, '미라마':1, '태이고':2}
data.replace({"map_name":map_ecoding}, inplace=True)
print(data["map_name"].value_counts())

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
import joblib   # 모델 저장

X = data.drop(columns=['win_place'])
y = data.win_place
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)

# 모델 생성
rfmodel = RandomForestRegressor(n_estimators=40, min_samples_leaf=3, max_features='sqrt', n_jobs=-1)
rfmodel.fit(X_train, y_train)
# 모델 저장
joblib.dump(rfmodel, "./datas/rf_model.h5")
# MAE 확인 (오차 절대 평균)
print('RandomForest mae train: ', mean_absolute_error(rfmodel.predict(X_train), y_train), 'mae test: ', mean_absolute_error(rfmodel.predict(X_test), y_test))

from lightgbm import LGBMRegressor
lgbm_for_reg= LGBMRegressor(colsample_bytree=0.8, learning_rate=0.03, max_depth=30,
              min_split_gain=0.00015, n_estimators=250, num_leaves=2200, reg_alpha=0.1, reg_lambda=0.001, subsample=0.8,
              subsample_for_bin=45000, n_jobs =-1, max_bin=700, num_iterations=5100, min_data_in_bin=12)
lgbm_for_reg.fit(X, y, verbose=1700, eval_set=[(X, y)], early_stopping_rounds=10)

# 모델 저장
joblib.dump(lgbm_for_reg, "./datas/lgbm_model.h5")
# MAE 확인
lgbm_pred = lgbm_for_reg.predict(X_test)
print('LGBMRegressor mae train: ', mean_absolute_error(lgbm_for_reg.predict(X_train), y_train), 'mae test: ', mean_absolute_error(lgbm_for_reg.predict(X_test), y_test))


