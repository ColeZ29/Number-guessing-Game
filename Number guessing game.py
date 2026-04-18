import random
print("This is a guessing game")
print("guess a number between 1 and 100")
b=int(input("enter your guess: "))
a=int(random.randint(0,100))
print("Choose your difficultly")
while a != b:
    if b<a:
        print("Your number is low.")
        b=int(input("enter your guess: "))
    if b>a:
        print("Your number is High.")
        b=int(input("enter your guess: "))
    if b==a:
        print("Your number is the correct guess.")
   
