import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
actions =[rock, paper, scissors]

user_action = int(input("Choose any of the following, 0 for Rock, 1 for Paper, 2 for scissors \n"))

user_moves = actions[user_action]

print(user_moves)

computer_action = random.randint(0,2)

computer_moves = actions[computer_action]

if user_moves == actions[0] and computer_moves == actions[2]:
    print(f"{computer_moves} \n You won")

elif user_moves == actions[0] and computer_moves == actions[1]:
    print(f"{computer_moves} \n You lost")

elif user_moves == actions[1] and computer_moves == actions[0]:
    print(f"{computer_moves} \n You won")

elif user_moves == actions[1] and computer_moves == actions[2]:
    print(f"{computer_moves} \n You lost")

elif user_moves == actions[2] and computer_moves == actions[0]:
    print(f"{computer_moves} \n You lost")

elif user_moves == actions[2] and computer_moves == actions[1]:
    print(f"{computer_moves} \n You won")

else:
    print(f"{computer_moves} \n Draw")






