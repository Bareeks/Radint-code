import random
from random import randint

x = randint(1,100)
y = randint(1,100)
print("Your first number is:", x)
print("Your second number is:", y)
v = input("What is the addition of both numbers?: ")
c = x + y

if c == int(v):
    print("Correct...Good Job!")
else:
    print("You are a dumb brain")
    
    