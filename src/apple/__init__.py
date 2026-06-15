"""Tiny text apples for Python."""

from __future__ import annotations

from typing import Literal

__all__ = ["apple", "rotten", "green", "bite", "basket", "main"]
__version__ = "0.1.0"


APPLE = r"""
        .-.
      .'   `.
      :  o  :
   .-.`.___.'-.
  /  _       _  \
 |  (_)     (_)  |
 |       <       |
  \   `.___.'   /
   `-._     _.-'
       `---'
""".strip("\n")


ROTTEN = r"""
        .-.
      .'   `.
      :  x  :
   .-.`.___.'-.
  /  _   .-. _  \
 |  ( ) (   ) )  |
 |   \_  `-' _/  |
  \    `---'    /
   `-.  ___  .-'
      `-._.-'
""".strip("\n")


GREEN = r"""
        .-.
      .'   `.
      :  v  :
   .-.`.___.'-.
  /               \
 |    fresh        |
 |      and        |
  \    crisp      /
   `-.         .-'
      `-------'
""".strip("\n")


BITE = r"""
        .-.
      .'   `.
      :  o  :
   .-.`.___.'-.
  /  _       _  \
 |  (_)   .-   |
 |       (      |
  \   `.__)    /
   `-._     _.-'
       `---'
""".strip("\n")


BASKET = r"""
      .-..-.   .-..-.
    .'  `   `.'  `   `.
   /  red     green    \
  |    apples for you   |
   \  .-----------.    /
    `-\___________/-.-'
       |  basket  |
       `---------'
""".strip("\n")


ArtName = Literal["apple", "rotten", "green", "bite", "basket"]


def _print_art(text: str) -> str:
    print(text)
    return text


def apple() -> str:
    """Print a cute apple and return the text."""
    return _print_art(APPLE)


def rotten() -> str:
    """Print a rotten apple and return the text."""
    return _print_art(ROTTEN)


def green() -> str:
    """Print a fresh green apple and return the text."""
    return _print_art(GREEN)


def bite() -> str:
    """Print an apple with a bite and return the text."""
    return _print_art(BITE)


def basket() -> str:
    """Print a basket of apples and return the text."""
    return _print_art(BASKET)


def main(kind: ArtName = "apple") -> str:
    """Print an apple from the command line."""
    arts = {
        "apple": apple,
        "rotten": rotten,
        "green": green,
        "bite": bite,
        "basket": basket,
    }
    return arts.get(kind, apple)()