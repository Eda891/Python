import random
def my_function(choice,computer):
                    print("You choose:  "+emoji[choice]+"\nComputer choose:  "+emoji[computer])
                    if(choice==computer):
                              print("It's a tie")
                    elif(choice=="r" and computer=="p"):
                              print("You lose!")
                    elif(choice=="p" and computer=="s"):
                              print("You lose!")
                    elif(choice=="s" and computer=="r"):
                              print("You lose!")
                    else:
                              print("You win!")
                    yes_no()

def yes_no():
          print("Do you wanna play again(y/n)")
          play=input()
          if(play=="n" or play=="N"): 
                    return print("Thanks for playing!")
          while play!="n" and play!="N":
                    if(play=="y" or play=="Y"):
                              print("Rock, Paper, Scissors(r/p/s):")
                              choice=input()
                              computer=random.choice(list)
                              if(choice not in list):
                                        print("Invalid input try again")
                              else:
                                        my_function(choice,computer)
                    else:
                              print("Invalid input try again")
                              play=input()
                              

list = ("r", "p", "s")
emoji={"r":"✊","p":"✋","s":"✌️"}
print("Rock, Paper, Scissors(r/p/s):")
choice=input()
computer=random.choice(list)
if(choice not in list):
            print("Invalid input try again")
            choice=input()
else:
          my_function(choice,computer)
