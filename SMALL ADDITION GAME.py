"""
CSC 243 Python for Programmers HW 3
Created on Oct 24 Tue 10:16:42 2017
@author: Archie Paredes
Problem 7.17 pg 236
"""
# type main() in shell or press f5 to run

import random
def main():
    n = int(input("How many addition question(s) do you want to answer? "))
    if n <= 0: pass
    else: game(n)
    
def game(n):
    i = 0
    correct = 0
    
    while(i != n):
        x = random.randrange(0, 9)
        y = random.randrange(0, 9)
        print("What does", x, "+", y, "equal?")
        # second try check
        try:
            answer = int(input("Enter answer: "))
        except:
            answer = int(input("Please write your answer using digits 0 through 9. Try Again!: "))        
        j = x + y
        if(answer == j):
            print("Correct")
            correct += 1
        else: print("Incorrect")
        i = i + 1

    print("You got {} correct answers out of {}".format(correct, n))
    
if __name__ == '__main__':
    main()
