import random
import time

#Steps to invite player into the game
print("\nThanks for choosing this hangman game")
name = input("What's your name: ")
print("Goodluck" + name + "on your jounery")
time.sleep(2)
print("Ready!!")
time.sleep(3)

#executing the game
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    word_to_guess = ["january", "border", "image", "film", "promise", "kids", "doll", "rhyme", "damage", "plants",
                     "christmas", "flower"]
    word = random.choice(word_to_guess)
    length = len(word)
    count = 0
    display = '_'* length
    already_guessed = []
    play_game = ""

#loop to re-execute the game
def play_loop():
    global play_game
    play_game = input("Do you want to play again? y = yes, n = no")
    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("Do you want to play again? y = yes, n = no")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks for playing")
        exit()



#Initializing all the conditions required for the game
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("Hangman word " + display + "mEnter your guess:\n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid input, Try another letter\n")
        hangman()

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index]+ guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter. \n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess" +str(limit - count)+ "guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess" +str(limit - count)+ "guesses remaining\n")

        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess" + str(limit - count) + "guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess" + str(limit - count) + "guesses remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guesses. You are dead :(\n")
            print("The word was:" ,already_guessed, word)
            play_loop()

    if word == "_" * length:
        print("Congrats!! You guessed correct!")
        play_loop()

    elif count != limit:
        hangman()

main()

hangman()
