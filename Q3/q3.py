#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv

f = open('q3.csv', 'r', encoding = 'UTF8')
data = csv.reader(f, delimiter=',')
next(data)

sub = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

for row in data:
    if row[1] == '1호선':
        sub[1] += int(row[-3]) + int(row[-2])
    if row[1] == '2호선':
        sub[2] += int(row[-3]) + int(row[-2])
    if row[1] == '3호선':
        sub[3] += int(row[-3]) + int(row[-2])
    if row[1] == '4호선':
        sub[4] += int(row[-3]) + int(row[-2])
    if row[1] == '5호선':
        sub[5] += int(row[-3]) + int(row[-2])
    if row[1] == '6호선':
        sub[6] += int(row[-3]) + int(row[-2])
    if row[1] == '7호선':
        sub[7] += int(row[-3]) + int(row[-2])
    if row[1] == '8호선':
        sub[8] += int(row[-3]) + int(row[-2])
    if row[1] == '9호선':
        sub[9] += int(row[-3]) + int(row[-2])
    else:
        continue
        
value = list(sub.values())
value.sort()

for k, v in sub.items():
    if v == value[-1]:
        keymax1 = k
        valmax1 = v
    if v == value[-2]:
        keymax2 = k
        valmax2 = v
    if v == value[0]:
        keymin1 = k
        valmin1 = v
    if v == value[1]:
        keymin2 = k
        valmin2 = v
        
f.close()

if __name__ == "__main__":
    print("*** Subway Report for Seoul on March 2023 ***")
    print("1st Busiest Line: Line {0:d} ({1:d})".format(keymax1, valmax1))
    print("2nd Busiest Line: Line {0:d} ({1:d})".format(keymax2, valmax2))
    print("1st Least used Line: Line {0:d} ({1:d})".format(keymin1, valmin1))
    print("2nd Lesat used Line: Line {0:d} ({1:d})".format(keymin2, valmin2))

