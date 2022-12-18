#!/usr/bin/env python3
# from pprint import pprint

def main():
    print(f"The name of this program is: {__name__}")
    # nums = range(1, 1000)
    total_sum = 0

    # for i in nums:
    for i in range(1000):
        if (i%3 == 0 or i%5 == 0):
            total_sum = total_sum+i
    print(total_sum)


if __name__ == "__main__":
    main()