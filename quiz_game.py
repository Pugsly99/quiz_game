print("Welcome to the quiz")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("okay lets play! ")

answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("what does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("what does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("what does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
else:
    print("Incorrect!")
