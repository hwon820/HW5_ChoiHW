#!/usr/bin/env python
# coding: utf-8

# In[12]:


import csv

f = open('q1.csv', 'r', encoding = 'cp949')
data = csv.reader(f, delimiter=',')

for _ in range(7):
    next(data)
    
tsum = 0
minsum = 0
maxsum = 0
n = 0
    
for row in data:
    if row[2] == '' or row[3] == '' or row[4] == '':
        continue
    else:
        tsum += float(row[2])
        minsum += float(row[3])
        maxsum += float(row[4])
        n += 1
        
f.close()

if __name__ == "__main__":

    print("*** Annual Temperature Report for Seoul in 2022 ***")
    print("Average Temperature: {0:0.2f} Celsius".format(tsum/n))
    print("Average Minimum Temperature: {0:0.2f} Celsius".format(minsum/n))
    print("Average Maximum Temperature: {0:0.2f} Celsius".format(maxsum/n))

