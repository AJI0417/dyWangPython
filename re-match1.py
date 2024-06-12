#!/usr/bin/python
#20240612 11227058 pythoneval11
import sys
import re

def main():
    pattern = r'^h.*d$'
    match = re.match(pattern, sys.argv[1], re.IGNORECASE)
    if match:
        print(match.group())
    else:
        print("找不到字串", sys.argv[1])
        
main()
