#!/usr/bin/python
#20240605 11227058 pythoneval10

from moduleself1 import avg1 as ms1avg

nu = int(input("請輸入一數字"))

result = ms1avg(nu)

print(f"Input={nu} Average=%f" % result)
