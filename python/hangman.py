import random

def choose_word():
    words = ["PYTHON", "JAVA", "HTML", "CSS", "JAVASCRIPT", "ANDROID"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman():
    word_to_guess = choose_word().upper()
    guessed_letters = []
    max_attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while max_attempts > 0:
        guess = input("Guess a letter: ").upper()

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            max_attempts -= 1
            print(f"Incorrect! {max_attempts} attempts remaining.")
        else:
            print("Correct!")

        current_display = display_word(word_to_guess, guessed_letters)
        print(current_display)

        if "_" not in current_display:
            print("Congratulations! You've guessed the word.")
            break

    if "_" in current_display:
        print(f"Sorry, you're out of attempts. The word was {word_to_guess}.")

hangman()