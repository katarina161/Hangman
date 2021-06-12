import random
from string import ascii_lowercase


# Write your code here
def print_title():
    print("H A N G M A N")


def get_random_choice(sequence):
    return random.choice(sequence)


def word_guessed(word, chosen_word):
    return word == chosen_word


def play_the_game(word, tries):
    guess_word = "-" * len(word)
    guess_letters = set()
    while tries:
        print()
        print(guess_word)
        letter = input("Input a letter: ")
        if len(letter) != 1:
            print("You should input a single letter")
            continue
        if letter not in ascii_lowercase:
            print("Please enter a lowercase English letter")
            continue
        if letter in guess_letters:
            print("You've already guessed this letter")
            continue

        guess_letters.add(letter)
        if letter not in word:
            tries -= 1
            print("That letter doesn't appear in the word")
            continue
        guess_word = "".join([ch if ch == letter or ch in guess_word else "-" for ch in word])
        if guess_word == word:
            print(f"""You guessed the word {word}!
You survived!""")
            return

    print("You lost!")


if __name__ == "__main__":
    possible_words = ('python', 'java', 'kotlin', 'javascript')
    print_title()
    start_playing = False
    while not start_playing:
        user_input = input('Type "play" to play the game, "exit" to quit: ')
        if user_input == "play":
            start_playing = True
            the_word = get_random_choice(possible_words)
            # guess = input(f"Guess the word: {the_word[:3]}{'-' * (len(the_word) - 3)}: ")
            # print("You survived!" if word_guessed(guess, the_word) else "You lost!")
            play_the_game(the_word, 8)
        elif user_input == "exit":
            break
