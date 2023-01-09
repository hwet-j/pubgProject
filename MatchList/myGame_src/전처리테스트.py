import re
str = "[정보] 아메리카노 11월 동안 10% 할인!"

# (), [], {}, <> 형태의 괄호와 그 안에 문자 제거
# pattern = r'\([^)]*\)'  # ()
pattern = r'\[[^)]*\]'  # []
# pattern = r'\<[^)]*\>'  # <>
# pattern = r'\{[^)]*\}'  # {}
str = re.sub(pattern=pattern, repl='', string=str)
print(str)


# 원핫 인코딩
from keras.utils import to_categorical
from keras.preprocessing.text import Tokenizer

