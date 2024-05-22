#!/usr/bin/python
#20240522 11227058 pythoneval8

num = int(input("請輸入一數字"))
print("11227058\t謝祥立\t")
for i in range(1,num+1):
  print("-"*(num-i),end="")
  print(str(i)*(2*i-1),end="")
  print("-"*(num-i))
