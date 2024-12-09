print("Welcome to this Quiz game:) ")

ask = input("Do you want to play Quiz? ")
if ask.lower() != "yes" or "y":
    print(" Okey! Let's Play..")
score= 0
    
question = input("What does CPU stand for? ")
if question.lower() == "central processing unit":
    print("Correct.")
    score += 1
else:
    print("Incorrect")
question = input("What does GPU stand for? ")
if question.lower() == "graphics processing unit":
    print("Correct.")
    score += 1
else:
    print("Incorrect")
question = input("What does RAM stand for? ")
if question.lower() == "random access memory":
    print("Correct.")
    score += 1
else:
    print("Incorrect")
question = input("What does ROM stand for? ")
if question.lower() == "read only memory":
    print("Correct.")
    score += 1
else:
    print("Incorrect")
question = input("What does PU stand for? ")
if question.lower() == "processing unit":
    print("Correct.")
    score += 1
else:
    print("Incorrect")
    
print(f"You got {score} question ")
print(f"You got {(score/5)*100}%" )