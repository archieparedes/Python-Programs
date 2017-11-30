"""
CSC 243 Python for Programmers 
Created on Nov Thu 30 14:17:47 2017
@author: Archie Paredes
Log2 Function
"""
def log2(n):
    # Base Cases
    if(n == 1 or n == 0):
        return(0)
    elif(n == 2):
        return(1)
    
    return(1 + log2(n//2))

n = 11 # example
print(log2(n))
