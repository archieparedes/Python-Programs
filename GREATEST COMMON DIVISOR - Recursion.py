"""
CSC 243 Python for Programmers HW 3
Created on Oct 30 Mon 18:33:59 2017
@author: Archie Paredes
Problem 10.20 pg 364
"""

def main():
    print("The program will output the greatest common divisor from two integers")
    a = int(input("Enter a first integer greater than second value: "))
    b = int(input("Enter a second integer value: "))
    while(a < b):
        a = int(input("Enter a first integer greater than second value: "))
    print(rgcd(a,b))

def rgcd(a,b):
    if(b == 0): return(a)
    else: return(rgcd(b,a%b))
    
    
if __name__ == '__main__':
    main()


