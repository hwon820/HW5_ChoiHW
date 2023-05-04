#!/usr/bin/env python
# coding: utf-8

# In[43]:


import csv

f = open('q4.csv', 'r', encoding = 'UTF8')
data = csv.reader(f, delimiter=',')
next(data)

result = []
n1 = n2 = n3 = n4 =0

for row in data:
        if row[1] == '1호선':
            result.append([1, row[3], int(row[-3]) + int(row[-2])])
            n1 += 1
        if row[1] == '2호선':
            result.append([2, row[3], int(row[-3]) + int(row[-2])])
            n2 += 1
        if row[1] == '3호선':
            result.append([3, row[3], int(row[-3]) + int(row[-2])])
            n3 += 1
        if row[1] == '4호선':
            result.append([4, row[3], int(row[-3]) + int(row[-2])])
            n4 += 1
        else:
            continue

result.sort(key = lambda x : [x[0], x[2]])
f.close()

if __name__ == "__main__":
    print("*** Subway Report for Seoul on March 2023 ***")
    print("Line 1:")
    print("Busiest Station: {0:s} ({1:d})".format(result[:n1][-1][1],result[:n1][-1][2]))
    print("Least used Station: {0:s} ({1:d})".format(result[:n1][0][1],result[:n1][0][2]))
    print("Line 2:")
    print("Busiest Station: {0:s} ({1:d})".format(result[n1:n1+n2][-1][1],result[n1:n1+n2][-1][2]))
    print("Least used Station: {0:s} ({1:d})".format(result[n1:n1+n2][0][1],result[n1:n1+n2][0][2]))
    print("Line 3:")
    print("Busiest Station: {0:s} ({1:d})".format(result[n1+n2:n1+n2+n3][-1][1],result[n1+n2:n1+n2+n3][-1][2]))
    print("Least used Station: {0:s} ({1:d})".format(result[n1+n2:n1+n2+n3][0][1],result[n1+n2:n1+n2+n3][0][2]))
    print("Line 4:")
    print("Busiest Station: {0:s} ({1:d})".format(result[n1+n2+n3:][-1][1],result[n1+n2+n3:][-1][2]))
    print("Least used Station: {0:s} ({1:d})".format(result[n1+n2+n3:][0][1],result[n1+n2+n3:][0][2]))

