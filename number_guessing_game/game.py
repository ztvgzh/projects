import random

top_of_range = input("Type the highest number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number larger than zero/0 next time')
        quit()
else:
    print("Please type a number next time")
    quit()

"""we also can use method .randint(0,11), where 11 is IN"""
random_num = random.randrange(0, top_of_range) #11 не входит

guesses = 0
while True:
    guesses +=1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue #будет продолжать спрашивать, пока юзер не введет число
    
    if user_guess == random_num: #сработает как только введут число
        print("Yes, you got it!")
        break #stops program when this condition is done
    elif user_guess > random_num:
        print("You were above the number!")
    else:
        print("You were below the number!")

print(f"You got it in {guesses} guesses")   