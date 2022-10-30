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

user_wins = 0
computer_wins = 0
draws = 0
game_images = [rock, paper, scissors]

while True:
    user_choice = int(input('Type 0 for rock, 1 for paper, or 2 for scissors. or 9 to quit: '))
    if user_choice == 9:
      break
    elif int(user_choice) not in [0, 1, 2, 9]:
      continue

    print(game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice >= 3 or user_choice < 0: 
        print("You typed an invalid number!") 
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
        user_wins += 1
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
        computer_wins += 1
    elif computer_choice > user_choice:
        print("You lose")
        computer_wins += 1
    elif user_choice > computer_choice:
        print("You win!")
        user_wins += 1
    elif computer_choice == user_choice:
        print("It's a draw")
        draws += 1
print(f'wins: {user_wins}\nlosses: {computer_wins}\ndraws: {draws}')


