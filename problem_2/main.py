#!/usr/bin/env python3
#
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# 
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
#
# from pprint import pprint

def main():
    print(f"The name of this program is: {__name__}")

a = 0
b = 1
result = 1
total_num = 0
total_sum = 0

while result < 4000000:
    result = (b + a)
    if result % 2 == 0:
           total_num +=1
           total_sum = total_sum + result

    a = b
    b = result

print("total num:", total_num, "total sum:", total_sum)


if __name__ == "__main__":
    main()