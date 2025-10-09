import random
number = random.randint(1, 100)
print("Guess the number betwen 1 to 100:")
guess=input()
if(guess.isdigit()):
          while(guess!=number):
                    if(int(guess)<number):
                              print("Too low!")
                              guess=input()
                    elif(int(guess)>number):
                              print("Too high!")
                              guess=input()
                    else:
                              print("Congrats")
                              break
else:
          print("Please enter a valid number")
          guess=input()