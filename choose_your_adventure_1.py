name = input("Type your name: ")
print(f"Welcome, {name}, to this adventurous journey!")

# Introduction and Background
print("You find yourself at a crossroad. A path stretches out before you, leading to unknown destinations.")

# First Game: Left or Right Path
answer = input("As you stand there, pondering the two paths ahead, which one will you choose? (left/right/antarctica): ").lower()

if answer == 'left':
    print("You decide to take the left path and embark on a new adventure.")

    answer = input("The path leads you to a dense forest. Do you venture deeper into the forest or turn back? (venture/back): ").lower()

    if answer == 'venture':
        print("As you venture deeper into the forest, you discover a hidden cave.")

        answer = input("Inside the cave, you find a glowing crystal. Do you touch it or leave it alone? (touch/leave): ").lower()

        if answer == 'touch':
            print("As your hand touches the crystal, a surge of energy flows through you.")
            print("You gain mystical powers and become a legendary hero!")
            print(f"Congratulations, {name}! You have won the game and unlocked an epic ending!")
        elif answer == 'leave':
            print("You decide not to touch the crystal. You leave the cave and continue your journey.")
            print("The adventure continues...")
        else:
            print("Not a valid option. You lose!")

    elif answer == 'back':
        print("You choose to turn back and find yourself back at the crossroad.")
        print("You decide to take the right path this time.")
        # Continue the story...

    else:
        print("Not a valid option. You lose!")

elif answer == 'right':
    print("You choose the right path and find yourself on a narrow bridge overlooking a chasm.")

    answer = input("The bridge looks unstable. Do you cross it or head back? (cross/back): ").lower()

    if answer == 'cross':
        print("You cautiously cross the bridge and encounter a mysterious stranger.")

        answer = input("The stranger offers you a magical amulet. Do you accept it? (yes/no): ").lower()

        if answer == 'yes':
            print("With the magical amulet in hand, you feel a surge of power.")
            print("You continue your journey with newfound confidence.")
            # Continue the story...
        elif answer == 'no':
            print("You politely decline the offer and continue on your way.")
            # Continue the story...
        else:
            print("Not a valid option. You lose!")

    elif answer == 'back':
        print("You decide not to risk crossing the unstable bridge and turn back.")
        print("You return to the crossroad and choose the left path this time.")
        # Continue the story...

    else:
        print("Not a valid option. You lose!")

elif answer == 'antarctica':
    print("You've chosen to embark on a journey to Antarctica, known for its icy landscapes and hidden treasures.")

    answer = input("Would you like to travel there by aeroplane or ship? (aeroplane/ship): ")

    if answer == 'aeroplane':
        print("It will take you 10 days to fly from India to Antarctica and will cost you 50000$.")
        answer = input("Are you ready for it? (yes/no): ")
        if answer == 'yes':
            print("Finally, you landed successfully and safely on Antarctica!")
            answer = input("You have dug a lot and unearthed 10 billion dollars worth of diamonds. What would you like to do with your wealth now? (I don't know/I know): ")
            if answer == "I don't know":
                print(f"{name}, you are the richest person on the planet now. Enjoy your life as you please!")
            elif answer == 'I know':
                answer = input("What is it? Would you like to share it with us? (yes/no): ")
                if answer == 'yes':
                    print(f"Thanks for sharing your next adventure with us, {name}. We will write your biography using generative AI tools within a week. Enjoy your life!")
                else:
                    print(f"{name}, you declined to share your next adventure. You have chosen to live an ordinary life.")
        else:
            print(f"{name}, you declined to be ready for your adventure to Antarctica. Save up money and let us know when you are ready.")
    
    elif answer == 'ship':
        print("It will take you 2 months to get there and cost you 30000$.")
        answer = input("Are you ready for it? (yes/no): ")
        if answer == 'yes':
            print("After a long journey, you arrived at Antarctica!")
            # Continue the story...
        else:
            print(f"{name}, you declined to be ready for your adventure to Antarctica. Save up money and let us know when you are ready.")
    else:
        print("Not a valid option. You lose!")

else:
    print("Not a valid option. You lose!")

print("Thank you for playing! Remember, every choice shapes your destiny.")
print("Thank you for taking life as a game. Always remember: If you set your dreams ridiculously high, even if you fail, you will fall above everyone else's success!")
