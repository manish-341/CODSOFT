# Rock-Paper-Scissors Game
import random

user_score = 0
computer_score = 0

choices = ["Rock", "Paper", "Scissors"]

while True:
    user_choice = int(input("\nEnter your Choice: Type 0 for Rock, 1 for Paper, 2 for Scissors: "))

    if user_choice > 2 or user_choice < 0:
        print("You have entered the invalid choice. Computer wins this round.")
        computer_score += 1
    else:
        computer_choice = random.randint(0, 2)
        print("You chose:", choices[user_choice])
        print("Computer chose:", choices[computer_choice])

        if computer_choice == user_choice:
            print("It's a tie.")
        elif computer_choice == 0 and user_choice == 2:
            print("Computer wins this round.")
            computer_score += 1
        elif user_choice == 0 and computer_choice == 2:
            print("You win this round.")
            user_score += 1
        elif computer_choice > user_choice:
            print("Computer wins this round.")
            computer_score += 1
        elif user_choice > computer_choice:
            print("You win this round.")
            user_score += 1

    print(f"Score => You: {user_score} & Computer: {computer_score}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nThanks for Playing!")
        print(f"Final Score => You: {user_score} & Computer: {computer_score}")
        break

        
    
    
    