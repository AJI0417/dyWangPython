#!/usr/bin/python
#20240605 11227058 pythoneval10

import moduleself1

def main():
    nu = int(input("請輸入一數字"))

    if nu % 2 == 0:
        avg_result = moduleself1.avg1(x1=nu)
        sum_result = moduleself1.sum1(x2=nu)
    else:
        avg_result = moduleself1.avg1(x2=nu)
        sum_result = moduleself1.sum1(x1=nu)
    print("Input=%d Average=%f Sum=%d" % (nu,avg_result,sum_result))

main()
