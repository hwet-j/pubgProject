import os
import django
import csv

list = ["solo", 'dlkf', 'dlkf',  "solo", "solo", "solo", "solo", "solo", "solo", 'dlkf']
num = 0
for i in list:
    if i == 'solo':
        print(i)
        del list[num]
        print(num)
        print(list)
    else:
        num += 1
