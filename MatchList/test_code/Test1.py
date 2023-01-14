import re
import pandas as pd
text = "플랫폼:Steam"

text_front = text[text.find(":")+1:]
text_back = text[:text.find(":")]

print(text_front)
print(text_back)

# 데이터 불러오기
data = pd.read_csv("../datas/pgc/MATCH_ALL_STAT.csv")
data['team_count'] = 16
data.to_csv("../datas/pgc/MATCH_ALL_STAT.csv", index=False)


