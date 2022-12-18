#!/usr/bin/env python3
import math
from pprint import pprint

def main():
    print(f"The name of this program is: {__name__}")
# python program to print prime factors
 
def primefactors(n):
   #even number divisible
   while n % 2 == 0:
      print (2),
      n = n / 2
    
   #n became odd
   for i in range(3,int(math.sqrt(n))+1,2):
     
      while (n % i == 0):
         print (i)
         n = n / i
    
   if n > 2:
      print (n)
 
n = int(input("Enter the number for calculating the prime factors :\n"))
primefactors(n)


if __name__ == "__main__":
    main()