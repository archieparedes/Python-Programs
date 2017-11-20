"""
CSC 243 Python for Programmers
Created on Nov 20 Mon 09:42:18 2017
@author: Archie Paredes
Fibonacci Number, recursion practice
"""

def fibonacci(n):
    if n == 0: # Base Case 1
        return(0)
    elif n == 1 or n == 2: # Base Case 2
        return(1)
    else:
        return(fibonacci(n-1) + fibonacci(n-2)) # Recursion, calculation for Fibonacci number

def main():
    n = int(input("How many numbers of Fibonacci do you want to print out?: "))
    for i in range(1, n + 1): # Looks at 1 first ending at nth input
        print(fibonacci(i))

if(__name__ == "__main__"):
    main()


