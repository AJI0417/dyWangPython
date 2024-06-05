#!/usr/bin/python
#20240605 11227058 pythoneval10

import sys

def calculate_average(numbers):
    total = sum(numbers)
    average = int(total / len(numbers))
    return average

def main():
    numbers = []
    strings = []
    
    # 將數字參數和非數字參數分開
    for arg in sys.argv[1:]:
        try:
            numbers.append(int(arg))
        except ValueError:
            strings.append(arg)
    
    # 計算平均值
    if numbers:
        avg = calculate_average(numbers)
        newstr = ''.join(strings)
        print(f"{newstr}={avg}")

main()
