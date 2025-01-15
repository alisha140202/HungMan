import random
import time

print("Welcome to Hungama Game")
name = input("Enter your name: ")
print("Hello", name, "Best of luck!")
time.sleep(2)
print("Game about to start...")
time.sleep(3)


def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january", "border", "image", "film", "promise", "kids", "lungs", "doll", "rhyme", "damage",
                      "plants"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""


def play_loop():
    global play_game
    play_game = input("Do you want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("Do you want to play again? y = yes, n = no \n")
    if play_game.lower() == "y":
        main()
        hangman()
    elif play_game.lower() == "n":
        print("Thanks for playing! We hope to see you again!")
        exit()


def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is the Hangman Word: " + display + " Enter your guess:\n").strip()

    if len(guess) == 0 or len(guess) >= 2 or not guess.isalpha():
        print("Invalid input, please try a single letter.\n")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        indices = [i for i, letter in enumerate(word) if letter == guess]
        for index in indices:
            display = display[:index] + guess + display[index + 1:]
        print(display + "\n")
    elif guess in already_guessed:
        print("You already guessed that letter. Try another one.\n")
    else:
        count += 1
        if count == 1:
            time.sleep(1)
            print(" _____ \n"
                  " |     \n"
                  " |     \n"
                  " |     \n"
                  " |     \n"
                  " |     \n"
                  " |     \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining.\n")
        elif count == 2:
            time.sleep(1)
            print(" _____ \n"
                  " |   | \n"
                  " |   |\n"
                  " |     \n"
                  " |     \n"
                  " |     \n"
                  " |     \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining.\n")
        elif count == 3:
            time.sleep(1)
            print(" _____ \n"
                  " |   | \n"
                  " |   |\n"
                  " |   | \n"
                  " |     \n"
                  " |     \n"
                  " |     \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining.\n")
        elif count == 4:
            time.sleep(1)
            print(" _____ \n"
                  " |   | \n"
                  " |   |\n"
                  " |   | \n"
                  " |   O \n"
                  " |     \n"
                  " |     \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining.\n")
        elif count == 5:
            time.sleep(1)
            print(" _____ \n"
                  " |   | \n"
                  " |   |\n"
                  " |   | \n"
                  " |   O \n"
                  " |  /|\\\n"
                  " |  / \\\n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:", word)
            play_loop()

    if display == word:
        print("Congrats! You have guessed the word correctly!")
        play_loop()
    elif count != limit:
        hangman()


main()
hangman()
