"""
CSC 243 Python for Programmers HW 1
Created on Tue Sep 26 13:49:53 2017
@author: Archie Paredes
Problem 8, Binary Representation
"""
def main():
    enterNum = int(input("Enter an positive integer: "))
    numToList = list()

    while(enterNum <=0):
        enterNum = int(input("Input was not a postive integer, please input again: "))
    
    convToStr = str(enterNum)

    # For loop to input each digit to a list
    for i in convToStr:         
         numToList.append(i)

    binRep(numToList)

def binRep(numToList):
    expoLen = list()
    lenToStr = str(len(numToList))
    print(lenToStr)
    for j in numToList:
        print(j)
        for i in range(lenToStr):
            print(i)
            #k = j * (2 ** i)
        
    #sum1 = k + k
            
if __name__ == '__main__':
    main()