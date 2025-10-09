import random
print("Roll the dice: (y/n)")
dice=input()
while dice!="n" and dice!="N":
          if(dice=="y" or dice=="Y"):
                    print(random.randrange(1, 7,1),random.randrange(1, 7,1))
                    print("Roll the dice: (y/n)")
                    dice=input()
          else:
                  print("invalid")
                  print("Roll the dice: (y/n)")
                  dice=input()
print("Thanks for playing!")