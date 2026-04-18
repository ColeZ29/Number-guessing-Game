import random
print("Welcome to the Number Guessing Game!")
print("ChatGPT is thinking of number from 1 to 100")
print("You need to guess it correctly to save the world")
print("Please select a difficulty Level:")
print("1:Easy Mode(10 Guesses)")
print("2:Medium Mode(5 Guesses)")
print("3:Hard Mode (3 Guesses)")
c=int(input("enter your Difficulty Level: "))
b=int(input("enter your guess: "))
a=int(random.randint(0,100))
e=0
if c==1:
    d=9
if c==2:
    d=4
if c==3:
    d=2
while a != b:
    if b<a:
        print("Your number is too low.")
        b=int(input("enter your guess: "))
        d=d-1
        e=e+1
    if b>a:
        print("Your number is too High.")
        b=int(input("enter your guess: "))
        d=d-1
        e=e+1
    if b==a:
        print("You guessed correctly.")
        print("You guessed it correctly in", e,"attempts")
    if d==0:
        print("You ran out of attempts. Game Over")
        break
        
        
   
