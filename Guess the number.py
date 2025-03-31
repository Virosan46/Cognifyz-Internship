# A while loop used to repeat the guess number till getting correct result. And Break is used to
while True:
    guess = int(input("Guess a number between 1 and 100: "))

    if guess > 90:
        print("Too high! Try again.")
    elif 30 <= guess <= 50:  # Check if guess is between 30 and 50
        print("Not much high")
    elif guess < 20:
        print("Too low! Try again.")
    elif guess > 100:
        print("Please Check the number")
    else:
        print("Congratulations! You guessed the correct number!")
        break