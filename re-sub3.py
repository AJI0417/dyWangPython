#!/usr/bin/python
#20240612 11227058 pythoneval11
import sys
import re

def sum_numbers_in_string(s):
    # 將非數字字元取代成空白
    s = re.sub(r'[^0-9]+', ' ', s)
    # 將連續空白取代成加號
    s = re.sub(r'\s+', '+', s)
    # 刪除字串前後的加號
    s = s.strip('+')
    # 刪除數字前的 0，獨立的 0 不必刪
    s = re.sub(r'\b0+(\d+)', r'\1', s)
    return s

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python re-sub3.py <string>")
        sys.exit(1)

    input_string = sys.argv[1]
    result_string = sum_numbers_in_string(input_string)
    result = eval(result_string)

    print(f"{input_string}\n{result_string}={result}")



