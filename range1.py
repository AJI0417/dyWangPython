#!/usr/bin/python
#20240522 11227058 pythoneval8

lower = int(input("請輸入一下限值"))
upper = int(input("請輸入一上限值"))

total = 0
for num in range(lower,upper + 1):
  if num % 3 == 0:
    total += num
print("總和=%d" %total)
