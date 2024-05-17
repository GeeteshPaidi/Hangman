from art import pictures
from words import word_list
from random import choice


def main():
    print(pictures[0], "Welcome to Hangman!", "You have 6 lives to guess the word.", "Good luck!", sep="\n")

    word = choice(word_list)
    n = len(word)
    life = 6
    guessing = ["_"] * n
    print("".join(guessing), n)

    while life != 0:
        guess = input("Guess a letter: ")
        if guess in word:
            for i in range(n):
                if word[i] == guess:
                    guessing[i] = guess
            print("".join(guessing))

            if "".join(guessing) == word:
                break

        else:
            life -= 1
            print("That's wrong 😱", pictures[6-life])

    if life == 0:
        print("You lose! 😔 \nThe word was", word)
    else:
        print("You win! 🎉")


if __name__ == "__main__":
    main()
