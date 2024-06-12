#!/usr/bin/python
#20240612 11227058 pythoneval11
import sys
import re

def remove_al_strings(s):
    # 使用正則表達式來找到所有 AL 子串並消去它們
    pattern = re.compile(r'(?i)A[^AL]*L')
    tmp = ""
    ans = s
    while ans != tmp:
        tmp = ans
        ans = re.sub(pattern, '', ans)
    return ans

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python re-sub2.py <string>")
        sys.exit(1)

    input_string = sys.argv[1]
    result_string = remove_al_strings(input_string)

    print(f"{input_string}\n{result_string}")
