import random

choice = ('r','s','p')

def get_user_choice():
    user_choice = input("Enter ur choice (r/s/p): ").lower()
    if user_choice in choice:
        return user_choice
    else:
        print("Invalid input!")



def determine_winner():
    user_choice = get_user_choice()
    computer_choice = random.choice(choice)
    print(f"Your Choice: {user_choice} and Computer Choice: {computer_choice}")
    if (user_choice == 'r' and computer_choice == 's' or
        user_choice == 's' and computer_choice == 'p' or
        user_choice == 'p' and computer_choice == 'r'):
       return print("U win")

    elif(computer_choice == 'r' and user_choice == 's' or
         computer_choice == 's' and user_choice == 'p' or
         computer_choice == 'p' and user_choice == 'r'):
        return print("Computer Win")

    elif(user_choice == computer_choice):
        return print("Tie")

    else:
        return print("Invaild Input")

def play_game():
    while True:
     determine_winner()
     ask = input("Want to play? (y/n): ").lower()
     if ask == 'y':
        print("Ok let's Play Again")
        continue
        
     elif ask == 'n':
        print("Thank you")
        break
     
     else:
         print("Invaild input")

play_game()
     