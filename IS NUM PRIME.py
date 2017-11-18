"""
CSC 243 Python for Programmers HW 1
Created on Sat Nov 18 17:00:52 2017
@author: Archie Paredes
Is the number inputed prime? returns a boolean value
"""
def main():
    numInput = int(input("Enter a postive integer: "))
    while(numInput <= 0):
        numInput = int(input("Input was not positive. Enter a postive integer: "))
    if prime(numInput) == True:
        print("The number inputed is prime")
    else: print("The number inputed is not prime")

def prime(numInput):     
    i = True
    x = 2
    while(i == True):
        if(numInput%x == 0):
            i = False
        else:
            x += 1
            if x == numInput:
                return(True)
    return(i)
        
if __name__ == '__main__':
    main()
