"""Create own dictionary based on 
https://raw.githubusercontent.com/dwyl/english-words/master/words.txt
"""

from pathlib import Path

import requests


def is_alpha(word):
    return all(c.isalpha() for c in word)


def no_repeats(word):
    for i, char in enumerate(word):
        if char in (word[0:i] + word[i + 1 :]):
            return False
    return True


def is_valid(word):
    return len(word) == 5 and word[0].islower() and is_alpha(word) and no_repeats(word)


p = Path("words.txt")
if not p.exists():
    r = requests.get(
        "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"
    )
    all_words = r.text.split("\n")
    p.write_text(all_words)
    Path("five_letter_words.txt").write_text("\n".join(map(is_valid, all_words)))
