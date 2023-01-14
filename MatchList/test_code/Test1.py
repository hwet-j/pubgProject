import re
text = "플랫폼:Steam"

text_front = text[text.find(":")+1:]
text_back = text[:text.find(":")]

print(text_front)
print(text_back)