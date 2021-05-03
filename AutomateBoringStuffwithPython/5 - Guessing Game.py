''' 
    This is a simple Guessing Game based on Automate the Boring Stuff with Python
    Implements random, input/output, selection, repetition, and handling exceptions
'''
import random as rnd 

name = input("My name: ")
print("Hello "+name)

answer = rnd.randint(1,100)
win = False
print("Guess My Secret Number!!")

for i in range(10):
    print("You have "+ str(10-i) +" guesses left!")
    try:
        guess = int(input("Your Guess: "))
        if guess==answer:
            win = True
            break
    except TypeError:
        continue
if win :
    print("You win! The Secret Number is "+ str(answer))
else:
    print("You ran out of guesses!\n The Answer is "+str(answer))