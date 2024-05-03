import random
import hangman_words
import hangman_art

random_word = random.choice(hangman_words.word_list)
print(hangman_art.hangman_logo)
total_live = 6

# Method-1
word_char = ['_'] * len(random_word)
while '_' in word_char and total_live != 0:
    user_choice = input(f"Guess a letter from a random word that content {len(random_word)} letter:  ").lower()
    if user_choice in random_word:
        for i in range(len(random_word)):
            if random_word[i] == user_choice:
                word_char[i] = user_choice
    else:
        print(hangman_art.stages[6 - total_live + 1])
        total_live -= 1
    print(word_char)

if '_' not in word_char:
    print("Congratulations! You guessed the word.")
else:
    print("You lose! The word was:", random_word)
