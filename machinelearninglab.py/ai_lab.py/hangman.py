
import random

def hangman():
    heroes = ["BATMAN", "SUPERMAN", "FLASH", "AQUAMAN",
              "IRONMAN", "SPIDERMAN", "THOR"]

    compartments = ["Life Support", "Navigation",
                    "Power Unit", "Defense Grid",
                    "Communication", "Main Core"]

    word = random.choice(heroes)
    hint = random.choice(word)
    guessed = [hint]
    wrong = 0

    print("=== BATMAN VS JOKER ===")
    print("Joker infected Justice League Tower!")
    print("Guess the superhero name to save the tower.")
    print("Hint: One letter is", hint)

    while wrong < 6:
        display = " ".join(
            ch if ch in guessed else "_ " for ch in word
        )
        print("\nWord:", display)
        print("Wrong guesses:", wrong)

        if all(ch in guessed for ch in word):
            print("ANTIVIRUS ACTIVATED!")
            print("Batman saved the tower!")
            print("All compartments recovered!")
            return

        guess = input("Enter a letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Enter a single letter!")
            continue

        if guess in guessed:
            print("Already guessed!")
            continue

        guessed.append(guess)

        if guess in word:
            print("Correct guess!")
        else:
            wrong += 1
            print("Wrong guess!")
            print("Compartment damaged:", compartments[wrong - 1])

    print("\nTOWER DESTROYED!")
    print("All compartments damaged!")
    print("The word was:", word)
    print("JOKER WINS!")

hangman()