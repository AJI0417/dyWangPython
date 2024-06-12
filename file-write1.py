#!/usr/bin/python
#20240612 11227058 pythoneval11
import sys

def main():
    Fname = sys.argv[1]
    f = open(f'{Fname}.txt','w+')
    text = "3-9 153 11227058 謝祥立"
    f.write(text)
    f.close()
    
main()
