# eldrow
Demo of Wordle game for educational purposes

- uses 8389 words collection distilled from from https://github.com/dwyl/english-words
- `Wordle` class holds secret word (can be chosen at random) and attempt history
- `.ask()` method provides result
- `___m_` is letters on own spot and  `m.op.` is letters contained in a hidden word
- `.reveal()` tells you the hidden word


```python
import random
from eldrow import get_word_list, Wordle

words = get_word_list()
w = Wordle(hidden_word=random.choice(words))
guesses = random.sample(words, 6)
for i, guess in enumerate(guesses):
    guess, spots, contains = w.ask(guess)
    print(i+1, "->", guess, spots, contains)
print("   Answer:", w.reveal())
```

Output:

```
$ python example.py
1 -> coyan _o___ .....
2 -> animo ___m_ ....o
3 -> egrid _____ e....
4 -> pocky po___ .....
5 -> paler p____ ...e.
6 -> myops ____s m.op.
   Answer: poems
```