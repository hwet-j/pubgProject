# 개인 기록을 가지고 순위를 예측 하는 함수 ( 팀의 평균 )
# https://5quad.github.io/2019/11/29/AIXProject.html

# 메모리 사용량을 줄이는 함수
def reduce_mem_usage(df):
    import numpy as np
    """ iterate through all the columns of a dataframe and modify the data type
        to reduce memory usage.
    """
    # start_mem = df.memory_usage().sum() / 1024**2
    # print('Memory usage of dataframe is {:.2f} MB'.format(start_mem))

    for col in df.columns:
        col_type = df[col].dtype

        if col_type != object:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)
            else:
                if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)

    # end_mem = df.memory_usage().sum() / 1024**2
    # print('Memory usage after optimization is: {:.2f} MB'.format(end_mem))
    # print('Decreased by {:.1f}%'.format(100 * (start_mem - end_mem) / start_mem))

    return df


# 총 이동 거리
def total_distance(df):
    df['total_distance'] = df['ride_distance'] + df['swim_distance'] + df['walk_distance']
    return df['total_distance']


# 1분당 무기 습득 개수
def average_weaponsAcquired(df):
    df['average_weaponsAcquired'] = df.weapons_acquired / (df.duration / 60)
    return df['average_weaponsAcquired']


# 1분당 딜량
def average_damage(df):
    df['average_damage'] = df.damage_dealt / (df.duration / 60)
    return df['average_damage']


# 힐+부스트 당 킬 관여
def healboost_per_kill(df):
    df['healboost_per_kill'] = (df['heals'] + df['boosts']) / df['assists'] + df['kills']
    return df['healboost_per_kill']


# 1분당 이동 거리
def dist_per_game(df):
    df['dist_per_game'] = df['total_distance'] / df['duration']
    return df['dist_per_game']


def predict_rank():
    import pandas as pd
    pd.set_option('mode.chained_assignment', None)
    from sklearn.model_selection import train_test_split
    import tensorflow as tf
    import keras
    from keras.models import Sequential
    from keras.layers import Dense
    import numpy as np
    import pickle
    from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
    from sklearn.linear_model import LinearRegression  # 1. Linear Regression
    from sklearn.linear_model import Lasso  # 2. Lasso
    from sklearn.linear_model import Ridge  # 3. Ridge
    # pip install xgboost
    # pip install lightgbm
    from xgboost.sklearn import XGBRegressor  # 4. XGBoost
    from lightgbm.sklearn import LGBMRegressor  # 5. LightGBM
    from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler
    import matplotlib.pyplot as plt
    import seaborn as sns
    from operator import itemgetter
    from matplotlib.patches import Rectangle
    import warnings
    warnings.filterwarnings('ignore')

    data = pd.read_csv(r"..\datas\pgc\Anal\All\predict_rank.csv")
    # data = reduce_mem_usage(data)

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

    """ 정규화가 필요할 것 같은 칼럼
     # 피해량 관련 ->
     damage_dealt
     damage_taken

     # 거리 관련 -> ??
     longest_kill
     ride_distance
     swim_distance
     walk_distance

     """
    # 시간 관련 -> duration으로 나눠주면 게임 내의 % 계산 가능
    # data['time_survived'] = data['time_survived'] / data['duration']
    # data['time'] = data['time'] / data['duration']
    # data['win_place'] = data['win_place'] / 16

    # 상관관계 분석
    corrAnal = data[['dbnos', 'assists', 'boosts', 'damage_dealt',  # 'death_type',
                     'headshot_kills', 'heals', 'kill_place', 'kill_streaks', 'kills',
                     'longest_kill', 'revives', 'ride_distance',
                     'road_kills', 'swim_distance', 'team_kills', # 'time_survived',
                     'vehicle_destroys', 'walk_distance', 'weapons_acquired',
                     'damage_taken', 'time', 'win_place']]

    # 상관관계 파악(그래프)
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

    # Model
    # 데이터 내에 문자열 데이터 숫자로 변환
    # print(corrAnal.columns)
    # feature, label 분리
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    X = corrAnal.drop("win_place", axis=1)
    # Create new feature
    X['average_weaponsAcquired'] = average_weaponsAcquired(data)
    X['average_damage'] = average_damage(data)
    X['totalDistance'] = total_distance(data)
    X['headshotKillsPerc'] = data.headshot_kills / data.kills
    X['dist_per_sec'] = dist_per_game(data)

    X = X.replace((np.inf, -np.inf, np.nan), 0)
    print(X)
    Y = corrAnal['win_place'].copy()


    # Train, Test 분류
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
    # Test, Validation 분류
    X_test, X_val, Y_test, Y_val = train_test_split(X_test, Y_test, test_size=0.3)

    params = {
        "objective": "regression",
        "metric": "mae",
        "num_leaves": 150,
        "learning_rate": 0.03,
        "bagging_fraction": 0.9,
        "bagging_seed": 0,
        "num_threads": 4,
        "colsample_bytree": 0.5,
        'min_data_in_leaf': 1900,
        'lambda_l2': 9
    }
    import lightgbm as lgb
    reg2 = lgb.LGBMRegressor(params, n_estimators=2000)
    reg2.fit(X_train, Y_train)
    pred2 = reg2.predict(X_test, num_iteration=reg2.best_iteration_)
    from sklearn.metrics import mean_absolute_error
    print(mean_absolute_error(Y_test, pred2))


    '''from sklearn.tree import DecisionTreeRegressor
    DTree_clf = DecisionTreeRegressor()
    DTree_clf.fit(X, Y)

    DTree_pred = DTree_clf.predict(X_test)
    print(list(DTree_pred[:30]))
    print(list(Y_test[:30]))'''

    '''
    # 모델 생성
    model = Sequential()
    model.add(Dense(128, activation='relu', input_shape=(1,)))
    model.add(Dense(128, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(1))

    model.compile(loss='mae', optimizer="adam", metrics=['mae'])

    batch_size = 5000
    epoch = 200
    # history = model.fit(X_train, Y_train, batch_size=batch_size, epochs=epoch, validation_split=0.2, verbose=0)
    #
    # # 예측 값 저장
    # result = pd.DataFrame()
    # result['Id'] = data['name']
    # # maxPlace에 맞춰 예측된 값 반올림 해줌
    # result['win_place'] = data['win_place']
    # # result.to_csv('submission.csv')
    '''

    return None


if __name__ == "__main__":
    predict_rank()
