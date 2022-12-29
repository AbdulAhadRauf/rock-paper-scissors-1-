import random
computer = random.choice(['R', 'P', 'S'])
user=input('Rock,Paper,Scissor \n Enter R,P,S')
Flag= False
if user == computer:
  print("Draw")
elif user == "R" and computer =="P" or user =="P" and computer=="S" or user =="S" and computer=="R" :
  Flag=True
else:
  Flag=False

if Flag:
  print(f'C = {computer}, You = {user} You Loose')
else:
  print(f'C = {computer}, You = {user} You win')