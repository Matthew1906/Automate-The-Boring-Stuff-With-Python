# def findResult(n,x,y,z):
#     print(x,y,z,n)

# findResult(100,100,100,11)

# import pandas, sys, os, math, seaborn, time, random, pyperclip

# Check for Errors -> using try catch block

def divideBy(num):
    try:
        return 199/num
    except ZeroDivisionError:
        return "Error"

print(divideBy(100))
print(divideBy(0))
# error = crashes and terminate the program

# Perfect for input validation !!

def printNumber(num):
    try:
        print(num+1)
    except TypeError:
        print("Error")

printNumber(100)
printNumber("havana o nana")

'''
Type Error : wrong object type
Value Error : correct type, wrong value
ZeroDivisionError : division by zero 

''' 
