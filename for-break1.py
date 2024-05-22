#!/usr/bin/python
#20240522 11227058 pythoneval8

num = input("請輸入一字串")

for cap in num:
  print(cap,end="")
  if cap != 'h':
    print('=',end="")
  if cap == 'h':
    break
print("=\n",end="")
