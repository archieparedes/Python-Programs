"""
CSC 243 Python for Programmers
Created on Oct 24 Tue 08:07:23 2017
@author: Archie Paredes
Problem 6.24 pg 196
"""
# type names() in shell to run

def names():
    namelist = []
    name = str(input("Enter first name: "))
    if(name!= ""): namelist.append(name)
    while(name != ""):
        name = str(input("Enter next name: "))
        if(name != ""): namelist.append(name)
    
    counter(namelist)

def counter(namelist):
    counters = {}
    keylist = []
    vallist = []
    it = 0

    # counter loop
    for i in namelist:
        if i in counters:
            counters[i] += 1
        else:
            counters[i] = 1
            
    for j in counters.keys():
        keylist.append(j)
    
    for k in counters.values():
        vallist.append(k)

    # output
    while(it < len(keylist)):
        if(vallist[it] == 1): print("There is 1 student name", keylist[it])
        else: print("There are", vallist[it], "students named", keylist[it])
        it += 1
    

names()
