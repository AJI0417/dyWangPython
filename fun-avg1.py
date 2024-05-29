#!/usr/bin/python
#20240529 11227058 pythoneval9

def avg1(x1=100,x2=50):
    if x1 >= 0 and x2 >= 0:
        return (x1 + x2) / 2
    else:
        return (100 + x1 + x2) / 3

def main():
    input_str = input("請輸入兩個數字，中間以空白隔開：")
    input_list = input_str.split()
    
    if len(input_list) == 2:
        num1 = float(input_list[0])
        num2 = float(input_list[1])
        result = avg1(num1, num2)
        print("Average=%f" % result)
    elif len(input_list) == 1:
        num1 = float(input_list[0])
        result = avg1(num1)
        print("Average=%f" % result)
    else:
        result = avg1()
        print("Average=%d" % result)
main()
