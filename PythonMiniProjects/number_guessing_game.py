import random
# getting the top range

top_range = input("Enter the top range: ")
if top_range.isdigit():
    top_range = int(top_range)
else:
    print("Enter a number next time!")
    quit()


# generating a random number within the top range
random_num = random.randint(0, top_range)



# checking weather the user's guess is same as the random number that has been generated.45
no_of_guesses = 0
while True:
    no_of_guesses += 1
    guess = input("Enter your guess :")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Enter a number next time!")
        quit()

    if guess == random_num:
        print(f"Random number : {random_num}  Your guess :  {guess}")
        print(f"You got it correct in {no_of_guesses} guesses")
        break
    elif guess > top_range:
        print("You are out of range!")
    elif guess>random_num:
        print("You are above the random number !")
    elif guess < random_num:
        print("You are below the random number !")
    else:
        continue
