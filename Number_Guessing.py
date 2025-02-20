import random

print("Hey I Dare You To Guess Correct Number.....Get Ready Buddy!") 

top_range=int(input("Enter the top range that  you  could guess the number in digit :  "))
if(top_range<0):
    print("Enter the number larger than 0 next time")
    quit()

random_num=random.randint(0,top_range)    
guess=0
while True:
      guess+=1
      user_guess=int(input("Enter your guessed number : "))
      if (user_guess==random_num):
           print("You won the game..!")
           break
      elif(user_guess>random_num):
           print("The number  you entered is greater ")   
      else:
           print("The number you entered is smaller")       

print(f"You guessed the number in {guess} guesses....")