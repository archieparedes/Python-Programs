"""
CSC 243 Python for Programmers
Created on Oct 22 Sun 10:57:23 2017
@author: Archie Paredes
Problem 6.22 pg 196
"""
# type main() in shell or press f5 to run

def main():
    word = str(input("Enter a word: "))
    if(mirror(word) == False): print("INVALID")

def mirror(word):
    validChar = {'U':'U', 'T':'T', 'W':'W', 'A':'A',
                 'H':'H', 'V':'V' ,'w':'w', 'o':'o',
                 'O':'O', 'd':'b', 'X':'X','x':'x',
                 'v':'v', 'b':'d', 'Y':'Y'} # characters that have mirror image
    lst1 = []

    # checks to see if char from word is a key in validChar
    for i in word:
        if i not in validChar.keys(): return(False)
        else: lst1.append(validChar[i])

    # reverse order         
    lst2 = reversed(lst1)

    # output
    for j in lst2:
        print(j, end = '')
    return(True)
        
if __name__ == '__main__':
    main()
