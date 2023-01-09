from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv("../datas/p_train.csv")
df = df[['walkDistance', 'total_distance', 'killPlace', 'weaponsAcquired', 'boosts',
     'heals', 'longestKill', 'matchDuration', 'rideDistance', 'damageDealt',
     'kills', 'killStreaks',
     'revives', 'DBNOs', 'assists', 'swimDistance',
     'headshotKills', 'teamKills', 'roadKills', 'winPlacePerc']]

X = df.drop(columns=['winPlacePerc'])
y = df['winPlacePerc']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)
import joblib
# 사용할 데이터를 재선택
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)
rfmodel = RandomForestRegressor(n_estimators=40, min_samples_leaf=3, max_features='sqrt', n_jobs=-1)
rfmodel.fit(X_train, y_train)
joblib.dump(rfmodel, "../datas/models/rf_model.h5")
# rfmodel.save("../datas/rf_model.h5")

print('RandomForest mae train: ', mean_absolute_error(rfmodel.predict(X_train), y_train), 'mae test: ', mean_absolute_error(rfmodel.predict(X_test), y_test))

from lightgbm import LGBMRegressor
lgbm_for_reg= LGBMRegressor(colsample_bytree=0.8, learning_rate=0.03, max_depth=30,
              min_split_gain=0.00015, n_estimators=250, num_leaves=2200, reg_alpha=0.1, reg_lambda=0.001, subsample=0.8,
              subsample_for_bin=45000, n_jobs =-1, max_bin=700, num_iterations=5100, min_data_in_bin=12)
lgbm_for_reg.fit(X, y, verbose=1700, eval_set=[(X, y)], early_stopping_rounds=10)



joblib.dump(lgbm_for_reg, "../datas/models/lgbm_model.h5")

lgbm_pred = lgbm_for_reg.predict(X_test)

print('LGBMRegressor mae train: ', mean_absolute_error(lgbm_for_reg.predict(X_train), y_train), 'mae test: ', mean_absolute_error(lgbm_for_reg.predict(X_test), y_test))












