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

#Write your code below this line 👇
list_game=[rock , paper , scissors]
player_choose=int(input("What do you choose? type 0 for Rock , 1 for paper or 2 for scissors"))
computer_choose = random.randint(0,len(list_game)-1)
if player_choose >= 3 or player_choose < 0:
    print("you typed vaild number you loss!")
else:
    print(list_game[player_choose])
    print("computer choose")
    print(list_game[computer_choose])
    if computer_choose==0 and player_choose == 2:
        print("computer win!")
    elif computer_choose == 0 and player_choose == 1:
        print("you win!")
    elif computer_choose == 0 and player_choose == 0:
        print("its a tie!")


