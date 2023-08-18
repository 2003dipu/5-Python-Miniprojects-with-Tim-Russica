name = input("Type your name: ")

print("Welcome ",name,"to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right.\nWhich way would you like to go? (left/right): ").lower()
if answer == 'left':
    answer = input("You come to a river, you can walk around it or swim across?\nType walk to walk around or swim to swim accross(walk/swim): ").lower()
    if answer == 'swim':
        print("------------ You swam across and were eaten by an eligator! -------------------")
    elif answer == 'walk':
        print("----------- You walked for many miles, ran out of water and lost the game of survival !---------")
    else:
        print("----------- Not a valid option. You lose! --------------------------------------")
elif answer == 'right':
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back? (cross/back): ")
    if answer == 'cross':
        answer = input("You cross the bridge and meet a stranger. Do you talk to them? (yes/no): ")
        if answer =='yes':
            answer = input("You talk to the stranger and they give you diamond. Do you want more diamond or go back to home?(diamond/back): ")
            if answer == 'diamond':
                answer = input("You chose to take more risks to earn more diamond. Are you ready?(yes/no): ")
                if answer == 'yes':
                    answer = input("Get ready to travel the entire continent of Antarctica because it is where 80% of the world diamond is. Do you go there by aeroplane or ship across the sea?(aeroplane/ship): ")
                    if answer == 'aeroplane':
                        answer = input("It will take you 10 days to fly from India to Antarctica and will cost you 50000$. Are you ready for it?(yes/no): ")
                        if answer == 'yes':
                            answer = input("Finally you landed successfully and safely on Antarctica! You have dug a lot and unearthed 10 billion dollars worth of diamonds. What would you like to do with your wealth now?(I don't know/ I know): ")
                            if answer == "I don't know":
                                print(f"{name} You are the richest person on the planet now. Enjoy you life as you please !!")
                            elif answer == 'I know':
                                answer = input("What is it? share it with us. We love to hear from you. Would you like to share it?(yes/no): ")
                                if answer == 'yes':
                                    print(f"{name} Thanks for sharing your next adventure with us. We will write your biography using generative AI tools within a week. Enjoy your life sir!!!")
                                else:
                                    print(f"{name}  You declined to share your next adventure. You have chosen to live an ordinary life")
                        else:
                            print(f"{name}  You declined to ready for your adventure to Antarctica. Save up money be let us know when you are ready.")

# You can make the game more long chained, engaging and intersting if you like!            
                    elif answer == 'ship':
                        answer = input("It will take you 2 months to get there and cost you 30000 $. Are you ready for it?(yes/no): ")

            elif answer == 'back':
                        print(f"{name} you can live happily with your family but you give up the opportunity to become the richest person on the planet.\n You lose")
            else:
                print(f"{name}, you declined to seek more diamond. You have chosen to live an ordinary life.\n You lose!!!")

        elif answer =='no':
            print(f"{name} You ignorantly lose the opportunities you can potentially have if you talked to them. You lose!!!. Always be curious!!!")
        else:
            print("----------- Not a valid option. You lose! --------------------------------------")
    elif answer == 'back':
        print("-----------You go back snkeakily from the adventure and lose the diamond! You lose!!!---------")
    else:
        print("----------- Not a valid option. You lose! --------------------------------------")
else:
    print("----------- Not a valid option. You lose! --------------------------------------")
print("Thank you for taking life as a game.\
      Always remember : If you set your dreams ridiculously high even if you fail, you will fall above everyone else's success!")

