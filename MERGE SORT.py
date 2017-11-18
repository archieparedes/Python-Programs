"""
CSC 243 Python for Programmers 
Created on Nov Tue 07 15:58:37 2017
@author: Archie Paredes
binary search and merge sort
"""
first = lst[0]
middle = len(lst) / 2
last = len(lst) - 1
def Merge(lst, first, middle, last):
    'Merges lst[first...middle] with lst[middle+1...last]'
    i=first
    j=middle+1
    A=[]
    while (i <= middle) and (j <=last):
        if lst[i] <= lst[j]:
            A.append(lst[i])
            i+=1
        else:
            A.append(lst[j])
            j+=1
    if i > middle:
        A=A+lst[j:last+1]
    else:
        A=A+lst[i:middle+1]
    lst[first:last+1]=A   

def search(lst, target, i, j):
    if i > j:                       # base case: empty list
        return -1                    # target cannot be in list

    mid = (i+j)//2                   # index of median of l[i:j]

    if lst[mid] == target:           # target is the median     
        return mid
    if target < lst[mid]:            # search left of median
        return search(lst, target, i, mid-1)
    else:                            # search right of median
        return search(lst, target, mid+1, j)



