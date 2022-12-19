#!/usr/bin/env python3
# 
# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?

import math

def main():
    print(f"The name of this program is: {__name__}")
 
def primefactors(n):
   while n % 2 == 0:
      print (2),
      n = n / 2
    
   for i in range(3,int(math.sqrt(n))+1,2):
     
      while (n % i == 0):
         print (i)
         n = n / i
    
   if n > 2:
      print (n)
 
n = int(input("Enter a number:\n"))
primefactors(n)


if __name__ == "__main__":
    main()