import random
computer = random.choice([1,-1,0])
yourstr = input("What you chose: ")
yourdict = {"r":1,"p":-1,"c":0}
reversedict = {1:"rock",-1:"paper",0:"caesar"}
you = (yourdict[yourstr])
print(f"You chose: {reversedict[you]}\n Computer chose: {reversedict[computer]}") 
if (computer==you):
    print("drow the game")
else:
    if(computer==1 and you==-1):
        print("You win!")
    elif(computer==-1 and you==1):
        print("You loose!")
    elif(computer==0 and you==1):
        print("You win!")
    elif(computer==1 and you==0):
        print("You loose!")
    elif(computer==-1 and you==0):
        print("You win!")
    elif(computer==0 and you==-1):
        print("You loose!")
    else:
        print("Something is wrong...")