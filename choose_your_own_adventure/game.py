while True:
    name = input("Type your name: \n")
    print(f"Welcome {name} to this adventure!")

    answer = input("You are on a dirt road, it has come to an end and you can go left or right, type here: \n").lower()

    if answer == "left":
        answer = input("You came to a river, you can walk around it or swim accross, type walk or swim: \n").lower()
        if answer == "walk":
            print("You walked for many miles, ran out of water and were lost")
            break
        elif answer == "swim":
            print("You swam accross and were eaten by an alligator")
        else:
            print("Not a valid option")
            break
    elif answer == "right":
        answer = input("You came to a bridge, it looks wobbly, do you want to cross it or head back (cross/back): \n").lower()
        if answer == "back":
            print("You go back to the main road. And you were given a chanse to quit the game without losing smth")
        elif answer == "cross":
            answer = input("You crossed the bridge and met a strangers.Do you talk to them (yes/no)?: \n").lower()
            if answer == "yes":
                print("You talked with strangers and they gave you gold. YOU WIN!")
            elif answer == "no":
                print("You ignored the strangers and they offended. YOU LOSE!")
            else:
                print("Not a valid option")
        else:
            print("Not a valid option")
    else:
        print("Not a valid option, you lose.")

    print("Thank you for trying.")