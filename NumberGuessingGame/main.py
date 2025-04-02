import random
import time

print("Welcome to this number guessing game!\nA number will be randomly selected between 1-100. Your job is to correctly guess the number\nPlease choose a difficulty level, this will determine how many guesses you have to get the correct number.")
print("Easy: 10 guesses\nMedium: 5 guesses\nHard: 3 guesses")
playing = True

while playing:

    difficultySelected = False
    difficulty = str(input("Please enter a difficulty: ")).upper()


    while not difficultySelected:

        if difficulty == "EASY":
            guesses = int(10)
            difficultySelected = True
        elif difficulty == "MEDIUM":
            guesses = int(5)
            difficultySelected = True
        elif difficulty == "HARD":
            guesses = int(3)
            difficultySelected = True
        else:
            difficulty = str(input("Please enter a valid difficulty: ")).upper()

    if difficulty == "EASY":
        guesses = 10
    elif difficulty == "MEDIUM":
        guesses = 5
    else:
        guesses = 3
    print("Great! You selected ", difficulty, ". This means you have",guesses, "guesses!")

    number = random.randint(1,100)


    for i in range(guesses,-1,-1):
        if i > 0:
            guess = int(input("Please enter your guess: "))
            if guess < number:
                print("That is incorrect, the number is higher. You have",i-1,"guesses left.")
            elif guess == number:
                if (guesses-(i-1)) == 1:
                    print("That is correct! The number was", number, ". You solved it in", (guesses - (i - 1)), "guess!")
                else:
                    print("That is correct! The number was",number,". You solved it in",(guesses-(i-1)),"guesses!")
                break
            elif guess > number:
                print("That is incorrect, the number is lower. You have", i - 1, "guesses left.")
            else:
                print("Something went wrong")
                break
        else:
            print("Unfortunately you have run out of guesses, better luck next time!")

    again = str(input("Would you like to play again? Y/N: ")).upper()
    if again == 'Y':
        pass
    elif again == 'N':
        playing = False
    else:
        print("Something went wrong")
        break






