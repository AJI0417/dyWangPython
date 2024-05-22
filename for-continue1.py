#!/usr/bin/python
#20240522 11227058 pythoneval8

num = input("請輸入一字串")
total = ""
for i in num:
  if i == 'h':
    continue
  total += i+"="
print(total)
