import random

computer = random.randint(1,100)
number = -1
Guessnumber = 1
while(number != computer):
    number = int(input("Guess the number: "))
    if(number>computer):
        print("Guess lower number...")
        Guessnumber += 1
    elif(number<computer):
        print("Guess higher number...")
    Guessnumber += 1
print(f"Computer Guess the number {computer} and you get this number {Guessnumber}")
