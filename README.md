# eldrow
Demo of Wordle game for educational purposes

## `eldrow` (reverse of `wordle`):

- uses 8389 words collection distilled from from https://github.com/dwyl/english-words
- `Wordle` class holds secret word (that can be chosen at random) and guess attempts history
- `.ask()` method provides feedback on your guess
- `___m_` is letters on own spot and `m.op.` is letters contained in a hidden word at different spots
- `.reveal()` tells you the hidden word

## Simple code

```python
from eldrow import Wordle

w = Wordle(hidden_word="swipe")
print(w.ask("piano")) # guess 1
print(w.ask("sword")) # guess 2
print(w.ask("swipe")) # guess 3
```

Output:

```
('piano', '_____', 'pi...')
('sword', 'sw___', '.....')
('swipe', 'swipe', '.....')
```

## More code

```python
import random
from eldrow import get_word_list, Wordle

# make a Wordle with a hidden word
words = get_word_list()
w = Wordle(hidden_word=random.choice(words))

# make 6 random guesses
guesses = random.sample(words, 6)
for i, guess in enumerate(guesses):
    guess, spots, contains = w.ask(guess)
    print(i+1, "->", guess, spots, contains)
print("   Answer:", w.reveal())
```

Output:

```
1 -> coyan _o___ .....
2 -> animo ___m_ ....o
3 -> egrid _____ e....
4 -> pocky po___ .....
5 -> paler p____ ...e.
6 -> myops ____s m.op.
   Answer: poems
```
