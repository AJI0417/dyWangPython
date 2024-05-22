#!/usr/bin/python
#20240522 11227058 pythoneval8

num = input("請輸入一字串")
for i in range(1,len(num)):
  if num[i] == 'h':
    i += 1
    print("第 %d 字元" % i)
    break
else:
  print("找不到 h 字元")
