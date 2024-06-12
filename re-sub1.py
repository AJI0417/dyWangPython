#!/usr/bin/python
#20240612 11227058 pythoneval11
import sys
import re

def is_valid_parentheses(s):
    tmp = ""
    ans = s
    while ans != tmp:
        tmp = ans
        ans = re.sub(r'\(\)', '', ans)
        ans = re.sub(r'\[\]', '', ans)
        ans = re.sub(r'\{\}', '', ans)
    return ans == ""

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python re-sub1.py <string>")
        sys.exit(1)

    str2 = sys.argv[1]
    if is_valid_parentheses(str2):
        print(f"{str2}\nAns=CORRECT")
    else:
        print(f"{str2}\nAns=ERROR")
