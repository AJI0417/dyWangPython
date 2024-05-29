#!/usr/bin/python
#20240529 11227058 pythoneval9

xyz = lambda x, y, z: x + y - 2 * z

# 主程式
def main():
    input_str = input("請輸入三個數字，中間以空白隔開：")

    x, y, z = map(int, input_str.split())

    result = xyz(x, y, z)
    print(f"x+y-2*z={result}")

main()
