import random

#list of 5 predefined words
words = ["hangman","python","codealpha","challenge","programming"]
secret_word = random.choice(words)

# Initial variables
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

# Create a display version of the word with underscores
display_word = ["_" for i in secret_word]

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 chances to guess incorrectly.\n")

# Game loop
while incorrect_guesses < max_attempts and "_" in display_word:
    print("Word: ", end=" ")
    for letter in display_word:
        print(letter, end=" ")
    print() 
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input, Please enter a single letter.\n")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter. Try a new one.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Good guess!\n")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        print(f"Wrong guess! You have {max_attempts - incorrect_guesses} attempts left.\n")

# Final result
if "_" not in display_word:
    print("Congratulations! You guessed the word:", secret_word)
else:
    print("Game Over! The word was:", secret_word)
