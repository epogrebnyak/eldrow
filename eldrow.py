"""Simple Wordle game implementation."""

from pathlib import Path
from random import choice
from typing import List

import requests

URL = (
    "https://gist.githubusercontent.com/"
    "epogrebnyak/c5b4fbd5de58dc3dfab44fa2a4f308f1/raw/"
    "741a2bdd3f963ca452cc270c7b2fc9f60ab0614c/"
    "five_letter_words.txt"
)


def get_word_list(url=URL):
    path = Path("five_letter_words.txt")
    if not path.exists():
        path.write_text(requests.get(url).text)
    return path.read_text().split("\n")


def concat(xs):
    return "".join(xs)


def correct_spot(hidden: str, guess: str) -> str:
    return concat(a if a == b else "_" for (a, b) in zip(hidden, guess))


def just_contains(hidden: str, guess: str) -> str:
    return concat(
        b if (b in hidden) & (a != b) else "." for (a, b) in zip(hidden, guess)
    )


class Wordle:
    def __init__(self, hidden):
        self._hidden = hidden
        self.attempts = []

    def ask(self, guess: str):
        inplace = correct_spot(self._hidden, guess)
        found = just_contains(self._hidden, guess)
        res = guess, inplace, found
        self.attempts.append(res)
        return res

    def reveal(self):
        return self._hidden


def random_wordle(words: List[str]) -> Wordle:
    return Wordle(choice(words))
