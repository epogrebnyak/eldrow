from random import sample
from eldrow import get_word_list, random_wordle

words = get_word_list()
w = random_wordle(words)
for i, guess in enumerate(sample(words, 6)):
    guess, spots, contains = w.ask(guess)
    print(f"{i+1}: {guess} {spots} {contains}")
print(" Answer:", w.reveal())
