print("Hey Hi User....Welcome To Quiz World")
user=input("Do you ready to play game with me ?  ")

if (user.upper() != "YES"):
    quit()

else:
    print("Let's Begin The Game..!")
score=0    

q1_ans=input("what is the longest river in the world ?  ")
if (q1_ans.upper() == "NILE"):
    print("You are right..you playing good...!")
    score+=1
else:
    print("You are wrong....")


q2_ans=input("what is the largest planet in the solar system ?  ")
if (q2_ans.upper() == "JUPITER"):
    print("You are right..you playing good...!")
    score+=1
else:
    print("You are wrong....")


q3_ans=input("what is the largest organ in the human body ?  ")
if (q3_ans.upper() == "SKIN"):
    print("You are right..you playing good...!")
    score+=1
else:
    print("You are wrong....")


q4_ans=input("what is the highest moutain in the world ?  ")
if (q4_ans.upper() == "MOUNT EVEREST"):
    print("You are right..you playing good...!")
    score+=1
else:
    print("You are wrong....")


print("Game is over....check your Results") 
print(f"Score :) {score}")  
print(f"You got :{((score/400)*100)*100}%") 

    
