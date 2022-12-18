#!/usr/bin/env python3
from pprint import pprint

def main():
    print(f"The name of this program is: {__name__}")

a = 0
b = 1
result = 1
totalnum = 0
totalsum = 0

while result < 4000000:
    result = (b + a)
    if result % 2 == 0:
           totalnum +=1
           totalsum = totalsum + result

    a = b
    b = result

print("total num:", totalnum, "total sum:", totalsum)



if __name__ == "__main__":
    main()