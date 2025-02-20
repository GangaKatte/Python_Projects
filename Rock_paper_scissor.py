import random

print("Let's Play Rock-Paper-Scissors!")
user_win = 0
computer_win = 0
choices = ['rock', 'paper', 'scissors']

while True:
    user_input = input("Enter your choice (Rock/Paper/Scissors) or 'Quit' to exit: ").lower()

    if user_input == "quit":
        break

    if user_input not in choices:
        print("Invalid input! Please enter Rock, Paper, or Scissors.")
        continue

    computer_input = random.choice(choices)
    print(f"Computer chose: {computer_input.capitalize()}")

    if user_input == computer_input:
        print("It's a tie!")
    elif (user_input == "rock" and computer_input == "scissors") or \
         (user_input == "paper" and computer_input == "rock") or \
         (user_input == "scissors" and computer_input == "paper"):
        print("You won!")
        user_win += 1
    else:
        print("You lost..!")
        computer_win += 1

print(f"Final Score - You: {user_win}, Computer: {computer_win}")
print("Thanks for playing!")
