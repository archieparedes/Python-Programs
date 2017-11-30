"""
CSC 243 Python for Programmers
Updated on Nov 30 Thu 15:27:43 2017
@author: Archie Paredes
Bubble Sort
"""
def BubbleSort(lst):
    for i in range(len(lst) - 1, 0, -1): # Analyze starting from last
        for j in range(i):
            if(lst[j]> lst[j + 1]):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return(lst)

def main():
    items = int(input('How many elements are in your list? '))
    lst = []
    for i in range(items):
        num = int(input("Please enter integer: "))
        lst.append(num)

    print(BubbleSort(lst))
    
if __name__ == '__main__':
    main()
