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

choice_list = [rock, paper, scissors]
should_continue = True

while should_continue:
    user_choice = input("Want to play rock,paper,scissors, type 'y' to play or 'n' to exit: ").lower()
    if user_choice == "y":
        player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
        print(choice_list[player_choice])
        computer_choice = random.randint(0, 2)
        if player_choice == computer_choice:
            print(choice_list[computer_choice])
            print("Draw")
        elif (player_choice == 0) and (computer_choice == 1):
            print(choice_list[computer_choice])
            print("You lose")
        elif (player_choice == 0) and (computer_choice == 2):
            print(choice_list[computer_choice])
            print("You win")
        elif (player_choice == 1) and (computer_choice == 0):
            print(choice_list[computer_choice])
            print("You win")
        elif (player_choice == 1) and (computer_choice == 2):
            print(choice_list[computer_choice])
            print("You lose")
        elif (player_choice == 2) and (computer_choice == 0):
            print(choice_list[computer_choice])
            print("You lose")
        elif (player_choice == 2) and (computer_choice == 1):
            print(choice_list[computer_choice])
            print("You win")
        else:
            print("give proper input")
    else:
        should_continue = False
