from random import sample, choice
from eldrow import get_word_list, Wordle

words = get_word_list()
w = Wordle(hidden_word=choice(words))
guesses = sample(words, 6)
for i, guess in enumerate(guesses):
    guess, spots, contains = w.ask(guess)
    print(i+1, "->", guess, spots, contains)
print("   Answer:", w.reveal())
