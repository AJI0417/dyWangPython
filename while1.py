#!/usr/bin/python
#20240522 11227058 pythoneval8

num = int(input("請輸入一數字"))
total = 0 
i = 1

output_str = "" 

while i <= num:
    total += i
    output_str += str(i)
    if i < num:
        output_str += "+"
    i += 1

print(output_str + f"={total}")
