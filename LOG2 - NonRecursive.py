"""
CSC 243 Python for Programmers 
Created on Nov Sat 18 11:25:27 2017
@author: Archie Paredes
Log2 Function
"""
def log2(n):
    count = 0
    
    while n//2 != 0:
        count += 1
        n = n//2
    return(count)
