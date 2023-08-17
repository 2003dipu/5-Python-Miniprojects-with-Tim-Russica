print("Welcome to my Computr Quiz Game!")

playing = input("Do you want to play the game?(yes/no) : " ).lower()

if playing != "yes":
    quit()

print("Okay! Let's play: ")
score = 0

print("------------------1 'st Question--------------------")
answer = input("What does CPU stand for? : ").lower()
if answer == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
print("------------------2' nd Question--------------------")
answer = input("What does GPU stand for? : ").lower()
if answer == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("------------------3'rd Question--------------------")
answer = input("What does RAM stand for? : ").lower()
if answer == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("------------------4'th Question--------------------")
answer = input("What does PSU stand for? : ").lower()
if answer == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
print(f"----------------  You score is {score}  ------------")
print("----------------  You got " + str((score/4)*100) + "%  ------------")