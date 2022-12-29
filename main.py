import random
Losses=0
Wins=0
Draws=0
rules=['R', 'P', 'S']
Play_again = "Y"
while (Play_again == "Y"):
  computer = random.choice(rules)
  user=input('Rock,Paper,Scissor\nEnter R,P,S\n')
  user = user.upper()
  if user not in rules:
    print("It seems you entered a different value, Please consider Entering the r,p,s only")
    break
  Flag= False
  if user == computer:
    print("Draw\n")
    Draws=Draws+1
  elif user == "R" and computer =="P" or user =="P" and computer=="S" or user =="S" and computer=="R" :
    Flag=True
    Losses=Losses+1
  else:
    Flag=False
    Wins=Wins+1
  
  if Flag:
    print(f'C = {computer}, You = {user} You Loose\n')
  else:
    print(f'C = {computer}, You = {user} You win\n')
  Play_again = input("You want to play again?\nY or N\n").upper()

if Play_again == "N":
  print(f'{Wins} Wins, {Losses} Losses, {Draws} Draws')
