"""
CSC 243 Python for Programmers HW 1
Created on Fri Sep 22 14:07:11 2017
@author: Archie Paredes
Problem 7, relitively prime
"""
def main():
    num1 = int(input("Input a first positve integer: "))
    num2 = int(input("Input a second positive integer: "))

    if((num1 <= 0) or (num2 <= 0)):
        while(num1 <= 0):
            num1 = int(input("The first integer was not positive. Input a positive integer: "))
        while(num2 <= 0):
            num2 = int(input("The second integer was not positive. Input a positive integer: "))
    
    if relPrime(num1, num2) == False:
        print("The two numbers are not relitively prime")
    else:
        print("The two numbers are relitively prime")

def relPrime(num1, num2):
    comDiv = list() 
    div1list = list()
    div2list = list()
    iter = 1
    
    # While Loop to find its divisors
    while(iter <= num1):
        if (num1 % iter == 0):
            div1list.append(int(iter))
        iter = iter + 1

    # For Loop for second integer to find its divisors
    iter = 1
    for iter in range(1, num2):
        if (num2 % iter == 0):
            div2list.append(int(iter))

    # For loop that finds common divisor and inputs it in a new list
    for k in div1list:
        for l in div2list:
            if (k == l):
                comDiv.append(int(k)) 

    # Output. Returns boolean value         
    print("List of Common Divisors: ", comDiv)
    if len(comDiv) == 1: return(True) # Single elenment mean 1 is the first and only divisor
    else: return(False)

if __name__ == '__main__':
    main()