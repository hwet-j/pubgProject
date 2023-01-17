import re
import pandas as pd

# 데이터 불러오기
data = pd.read_csv("./datas/crawl_train_data.csv")

pgc_data = pd.read_csv("../datas/pgc/MATCH_ALL_STAT.csv")

pgc_data = pgc_data[pgc_data.map_name != 'Sanhok']
pgc_data.drop(columns = ['death_type', 'kill_place',
                'kill_streaks','name', 'player_id','team_kills',
           'damage_taken', 'team_name', 'match_id', 'created_at',
           'telemetry_link', 'team_roster_id', 'team_member',
           'team_rank', 'team_kill', 'team_assist', 'team_distance',
           'team_damagedealt', 'team_damagetaken', 'team_timesurvived'], inplace=True)

pgc_data['longest_kill'] = round(pgc_data.longest_kill / 1000, 3)
pgc_data['walk_distance'] = round(pgc_data.walk_distance / 1000, 2)
pgc_data['ride_distance'] = round(pgc_data.ride_distance / 1000, 2)
pgc_data['swim_distance'] = round(pgc_data.swim_distance / 1000, 2)
pgc_data['total_distance'] = pgc_data.walk_distance + pgc_data.ride_distance + pgc_data.swim_distance
map_ecoding = {'Erangel':"에란겔", 'Erangel (Remastered)':"에란겔", "Miramar":"미라마"}
pgc_data.replace({"map_name":map_ecoding}, inplace=True)

# 학습을 위한 데이터 ( 경쟁전 및 대회기록 )
data = pd.concat([data, pgc_data], axis=0, ignore_index=True)
data.to_csv("./datas/Train_data.csv", index=False)