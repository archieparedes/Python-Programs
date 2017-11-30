"""
CSC 243 Python for Programmers HW 1
Created on Tue Sep 26 13:49:53 2017
@author: Archie Paredes
Problem 8, Binary Representation
"""
def main():
    enterNum = int(input("Enter an positive integer: "))
    numToList = list()
    strToInt = list()
    lenList = list()

    # Input has to be a positive integer
    while(enterNum <=0):
        enterNum = int(input("Input was not a postive integer, please input again: "))

    # Converts int to a string
    convToStr = str(enterNum)

    # For loop to input each digit to a list of string
    for i in convToStr:         
         numToList.append(i)
         
    # Converts string list to integer class
    for j in numToList:
        strToInt.append(int(j))

    # Length of Int List
    lenOfNTL = len(strToInt) # exponential value

    # Binary to Decimal Conversion
    binRep(strToInt, lenOfNTL)

    # Decimal to Binary Conversion
    decSyst(enterNum)
    
def binRep(strToInt, lenOfNTL):
    print("Binary to Decimal Conversion: ")
    i = 0
    binList = list()
    
    while(i != lenOfNTL):
        k = strToInt[i] * (2**i)
        binList.append(k)
        i = i + 1

    # Output
    print("Decimal System = ", sum(binList))

def decSyst(enterNum):
    print("Decimal to Binary Conversion: ")

    val = int(enterNum)
    bit = int(0)
    bitList = list()

    # Exponential to find greatest bit 
    while((2**bit) < enterNum):
        bit = bit + 1
    
    # Loop that will append 1 or 0. 1 if bit is less than enterNum - enterNum
    while(bit >= 0):
        if((val - (2**bit)) < 0 ):
            bitList.append(0)
        else:
            bitList.append(1)
            val = val - (2**bit)
        bit = bit - 1

    # Output
    print("Binary = ", end='') 
    for i in bitList:
        print(i, end='')
     
if __name__ == '__main__':
    main()
