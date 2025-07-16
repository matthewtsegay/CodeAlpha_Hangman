import random

#Predefined list of 5 words

words = ["python","golang","java","javascript","c++"]

# Choose a random word from the list

word_to_guess = random.choice(words)
guessed_letter = []
incorrect_guess = 0
max_attempts = 6

# Create a display version of the word with underscores

display_words = ["_" for _ in word_to_guess]

print("*********  welcome to hangman game             *******")
print("********* Guess the word, one letter at a time *******")
print("*********  you have 6 incorrect guessess        *******\n")

while incorrect_guess < max_attempts and "_" in display_words:
    print("word:",' '.join(display_words))
    print("guessed letter :" ,",".join(guessed_letter))
    guess = input("Enter letter :").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("please enter a single alphabet!\n")
        continue

    if guess in guessed_letter:
        print("you already guess the letter!\n")
        continue

    guessed_letter.append(guess)

    if guess in word_to_guess:
        print("great guess!\n")
        for idx,letter in enumerate(word_to_guess):
            if letter == guess:
                display_words[idx] = guess
    else:
        incorrect_guess += 1
        print(f"wrong guess!, you have only {max_attempts - incorrect_guess}")
   
# Final result     
if "_" not in word_to_guess:
    print("congratulation ! you guess the correct word",word_to_guess)
else:
    print("game over ! you lost the word",word_to_guess)