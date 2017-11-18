

def binarySearch(lst, key):
    firstIndex = 0
    endIndex = int(len(lst) - 1)
    middleIndex = int((firstIndex + endIndex) / 2)

    while(firstIndex <= endIndex):
        if(lst[middleIndex] == key):
            return(True)
        elif(key > lst[middleIndex]):
            firstIndex = middleIndex + 1
        else:
            endIndex = middleIndex - 1
    return(False)

lst = [1,2,3,6,7,8,9,10]
key = 9
binarySearch(lst, key)
"""
def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False
	
    while first<=last and not found:
	midpoint = (first + last)//2
	    if alist[midpoint] == item:
	        found = True
	    else:
                if item < alist[midpoint]:
	            last = midpoint-1
	        else:
	            first = midpoint+1
	
    return found
            """
