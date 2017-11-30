"""
CSC 243 Python for Programmers
Created on Nov 20 Mon 13:47:29 2017
@author: Archie Paredes
Binary Search - recursion
"""

def binarySearch(lst, key):
    # Base Case
    if len(lst) == 1:
        if lst[0] == key:
            return(True)
        return(False)

    else:
        middle = int(len(lst)//2)
        # Looks at the second half
        if lst[middle] < key:
            return(binarySearch(lst[middle:],key))
        # Looks at the first half
        elif lst[middle] > key:
            return(binarySearch(lst[:middle],key))
        # If found, return True
        return(True)

lst = [1,2,4,5,6,7,88,979,7655]
key = 999
print(binarySearch(lst, key))
