name=input("Hey user say your good name ? ")
print(f"Hey {name} get ready to adventures journey,let's see you win or loose....))")

print(">>>>>>>> START <<<<<<<<<")
answer=input("You are at edge of road , now which direction you want to turn right/left ? >  ").lower()
if answer=="left":
    answer=input("You came at river , now what do you want swim/walk ? > ").lower()
    if answer=="swim":
       answer=input("You crossed the river ...have you find diamond near river found/not found ? > ").lower()
       if answer=="found":
          print("You Won....")   
       else:
            print("You Lost !")
    elif answer=="walk":
       answer=input("You sink in water ...you lost").lower()        

elif answer=="right":
     
    answer=input("You came at Train, now what do you want catch/leave  ? > ").lower()
    if answer=="catch":
       answer=input("You travelled ...now you have to go city and find diamond found/notfound ? > ").lower()
       if answer=="found":
          print("You Won....")   
       else:
            print("You Lost !")
    elif answer=="leave":
       answer=input("You left train ...you lost").lower()     

else:
    print("You choose wrong option...You Lostttt !")


