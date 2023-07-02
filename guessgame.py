import numpy as np 
x = np.random.randint(10)
print("Hello! Let's play a game!")
y = int(input("Enter your number"))
if (x == y):
    print("You guessed it right!")
else:
    print("Sorry Buddy! It was", x)