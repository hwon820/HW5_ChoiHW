#!/usr/bin/env python
# coding: utf-8

# In[3]:


import csv

f = open('q2.csv', 'r', encoding = 'cp949')
data = csv.reader(f, delimiter=',')

for _ in range(7):
    next(data)
    
day_max = -999
max_date = ''
day_min = 999
min_date = ''
    
for row in data:
    #결측치 포함 row 무시
    if row[3] == '' or row[4] == '':
        continue
    #최고 일교차
    if day_max < float(row[4]) - float(row[3]):
        max_date = row[0]
        day_max = float(row[4]) - float(row[3])
    #최저 일교차
    if day_min > float(row[4]) - float(row[3]):
        min_date = row[0]
        day_min = float(row[4]) - float(row[3])
        
f.close()

if __name__ == "__main__":
    print("*** Annual Temperature Report for Seoul in 2022 ***")
    print("Day with the Largest Temperature Variation: {0:s}".format(max_date))
    print("Maximum Temperatrue Difference: {0:0.1f} Celsius".format(day_max))
    print("Day with the Smallest Temperature Variation: {0:s}".format(min_date))
    print("Minimum Temperatrue Difference: {0:0.1f} Celsius".format(day_min))

