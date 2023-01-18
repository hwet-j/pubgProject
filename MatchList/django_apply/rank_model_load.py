def load_model(data):
       import joblib   # 모델 저장, 불러오기
       import pandas as pd
       from sklearn.metrics import mean_absolute_error
       import numpy as np

       model = joblib.load("./datas/lgbm_model.h5")

       # 맵 이름을 맵핑하기 위해 설정 (대회 기록으로 학습시킨 데이터를 경쟁전 데이터를 입력하므로 맵의 종류가 다름)
       map_ecoding = {'에란겔':0, '미라마':1, "태이고":2}
       data.replace({"map_name":map_ecoding}, inplace=True)

       test_data = data.drop(columns=['win_place'])
       rank_data = data['win_place']

       model_predict = model.predict(test_data)
       print(np.around(model_predict))

       print('mae : ', mean_absolute_error(np.around(model_predict), rank_data))

       for i, j in zip(np.around(model_predict), rank_data):
              print(int(i), '\t' , j)

def predict_one(row):
       import joblib   # 모델 저장, 불러오기
       import pandas as pd
       from sklearn.metrics import mean_absolute_error
       import numpy as np

       model = joblib.load("./datas/lgbm_model.h5")

       # 맵 이름을 맵핑하기 위해 설정 (대회 기록으로 학습시킨 데이터를 경쟁전 데이터를 입력하므로 맵의 종류가 다름)
       map_ecoding = {'에란겔':0, '미라마':1, "태이고":2}
       row.replace({"map_name":map_ecoding}, inplace=True)

       test_data = row.drop(columns=['win_place'])
       rank_data = row['win_place']

       model_predict = model.predict(test_data)
       print(np.around(model_predict))

       print('mae : ', mean_absolute_error(np.around(model_predict), rank_data))

       for i, j in zip(np.around(model_predict), rank_data):
              print(int(i), '\t' , j)