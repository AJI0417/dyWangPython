#!/usr/bin/python
#20240605 11227058 pythoneval10

def avg1(x1=100,x2=50):
    if x1 >= 0 and x2 >=0:
        return (x1+x2) / 2
    else:
        return (100 + x1 + x2) / 3

def sum1 (x1=50,x2=150):
    if x1 >= 0 and x2 >= 0:
        return x1 + x2
    else:
        return 100 + x1 + x2
