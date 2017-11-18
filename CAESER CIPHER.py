"""
CSC 243 Python for Programmers
Created on nov 11 Sat 16:49:29 2017
@author: Archie Paredes
Caeser Cipher Dictionary Practice
"""


def main():
    print("This program will translate your string into Caeser Cipher")
    strInput = 'hello' #str(input("Enter a string: "))
    print(caeserCiph(strInput))
    

def caeserCiph(strInput):
    translation = {'a': 'e', 'b':'f', 'c':'g',
                   'd':'h', 'e':'i', 'f':'j',
                   'g':'k', 'h':'l', 'i':'m',
                   'j':'n', 'k':'o', 'l':'p',
                   'm':'q', 'n':'r', 'o':'s',
                   'p':'t', 'q':'u', 'r':'v',
                   's':'w', 't':'x', 'u':'y',
                   'v':'z', 'w':'a', 'x':'b',
                   'y':'c', 'z':'d'}
    
    for i in strInput:
        print(translation[i], end ='')
    return('')
    

if __name__ == '__main__':
    main()
