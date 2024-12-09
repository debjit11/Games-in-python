name = input("What's your name: ")
print(f"Welcome {name} to this adventure!")

answer = input("You are on dirt road ,it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can work around it or swim accross? Type walk around and swim to swim accross: ")
    if answer.lower() == "swim":
        print("You swam accross and ware enten by an alligator.")
    elif answer.lower() == "walk":
        print("You works for many miles,run out the water and you loss the game.")
    else:
        print("Not a valid option.You lose")
elif answer.lower() == "right":
    answer = input("You come to the bridge, it looks wobbly, do you want to cross it or head back (cross/back) ?")
    if answer.lower() == "back":
        print("You go back and lose.")
    elif answer.lower() == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)?")
        if answer.lower() == "yes" or "y":
            print("You talk to the stranger and they give you gold. You Win!")
        elif answer.lower() == "no" or "n":
            print("You ignore the stranger and they are offered and you lose. ")
        else:
            print("Not valid option. You lose ")
print(f"Thanks you for trying {name}.")
        
    
    