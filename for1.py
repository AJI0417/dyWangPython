#!/usr/bin/python
#20240522 11227058 pythoneval8

string_input = input("請輸入一字串")

output_str = "" 

for i in range(1, len(string_input) - 1):
    output_str += string_input[i] + "="

print(output_str)
