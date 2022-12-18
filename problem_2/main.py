#!/usr/bin/env python3
from pprint import pprint

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