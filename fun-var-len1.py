#!/usr/bin/python
#20240529 11227058 pythoneval9

def varlen(nu,*list4):
    select_elements = list4[:nu]
    average = sum(select_elements) // len(select_elements)
    return average

list4 = [ 805, 490, 697, 193, 842, 483, 958, 291, 489, 143, 370, 111, 812, 188, 532, 955, 670, 829, 807, 292, 597, 237, 766, 158, 314, 172, 381, 291, 332, 976, 500, 776, 870, 862, 35, 878, -11, 357, 360, 943 ]

user_input = int(input("請輸入一個數字："))
average = varlen(user_input,*list4)
print(f"Average={average}")
