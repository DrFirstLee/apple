"""Tiny text apples for Python."""

from __future__ import annotations

import sys
from typing import Literal

__all__ = [
    "apple",
    "rotten",
    "green",
    "bite",
    "basket",
    "samsung",
    "angry",
    "cute",
    "sexy",
    "nerd",
    "sleepy",
    "doctor",
    "money",
    "party",
    "love",
    "random",
    "kinds",
    "main",
]
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


SAMSUNG = r"""
          .-.
        .'   `.
        :  S  :
    .-.`.___.'-.
  /               \
 |    SAMSUNG      |
 |      apple       |
  \   no comment   /
    `-.         .-'
        `-------'
""".strip("\n")


ANGRY = r"""
          .-.
        .'!!!`.
        :  ^  :
    .-.`.___.'-.
  /  >       <  \
 |      ___      |
 |     /___\     |
  \   do not    /
    `-. touch .-'
        `-----'
""".strip("\n")


CUTE = r"""
          .-.
        .'   `.
        :  *  :
    .-.`.___.'-.
  /  o       o  \
 |      .-.      |
 |     (   )     |
  \    `-'      /
    `-.  yay  .-'
        `-----'
""".strip("\n")


SEXY = r"""
          .-.
        .'   `.
        :  ~  :
    .-.`.___.'-.
  /  _       _  \
 |  (o)     (-)  |
 |      \_/       |
  \   smooth     /
    `-.  gloss .-'
        `-----'
""".strip("\n")


NERD = r"""
          .-.
        .'   `.
        :  pi :
    .-.`.___.'-.
  /  .--. .--.  \
 |  | 0 || 0 |   |
 |   '--' '--'   |
  \   debug me  /
    `-.       .-'
        `-----'
""".strip("\n")


SLEEPY = r"""
          .-.
        .' z `.
        :  z  :
    .-.`.___.'-.
  /  -       -  \
 |       _       |
 |      (_)      |
  \    later    /
    `-.       .-'
        `-----'
""".strip("\n")


DOCTOR = r"""
          .-.
        .' + `.
        :  +  :
    .-.`.___.'-.
  /      +      \
 |   Dr. Apple   |
 |   eat one/day |
  \   maybe     /
    `-.       .-'
        `-----'
""".strip("\n")


MONEY = r"""
          .-.
        .' $ `.
        :  $  :
    .-.`.___.'-.
  /  $       $  \
 |    premium    |
 |    pricing    |
  \  very ripe  /
    `-.       .-'
        `-----'
""".strip("\n")


PARTY = r"""
          .-.
        .'^_^`.
        :  *  :
    .-.`.___.'-.
  /  \o/   \o/  \
 |    confetti    |
 |   juice time   |
  \  pop pop pop /
    `-.       .-'
        `-----'
""".strip("\n")


LOVE = r"""
          .-.
        .' <3`.
        :  <3 :
    .-.`.___.'-.
  /  _       _  \
 |  ( )     ( )  |
 |      heart     |
  \    seed      /
    `-.       .-'
        `-----'
""".strip("\n")


ArtName = Literal[
    "apple",
    "rotten",
    "green",
    "bite",
    "basket",
    "samsung",
    "angry",
    "cute",
    "sexy",
    "nerd",
    "sleepy",
    "doctor",
    "money",
    "party",
    "love",
    "random",
]


ARTS = {
    "apple": APPLE,
    "rotten": ROTTEN,
    "green": GREEN,
    "bite": BITE,
    "basket": BASKET,
    "samsung": SAMSUNG,
    "angry": ANGRY,
    "cute": CUTE,
    "sexy": SEXY,
    "nerd": NERD,
    "sleepy": SLEEPY,
    "doctor": DOCTOR,
    "money": MONEY,
    "party": PARTY,
    "love": LOVE,
}


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


def samsung() -> str:
    """Print a Samsung apple and return the text."""
    return _print_art(SAMSUNG)


def angry() -> str:
    """Print an angry apple and return the text."""
    return _print_art(ANGRY)


def cute() -> str:
    """Print a cute apple and return the text."""
    return _print_art(CUTE)


def sexy() -> str:
    """Print a glamorous apple and return the text."""
    return _print_art(SEXY)


def nerd() -> str:
    """Print a nerd apple and return the text."""
    return _print_art(NERD)


def sleepy() -> str:
    """Print a sleepy apple and return the text."""
    return _print_art(SLEEPY)


def doctor() -> str:
    """Print a doctor apple and return the text."""
    return _print_art(DOCTOR)


def money() -> str:
    """Print a premium-priced apple and return the text."""
    return _print_art(MONEY)


def party() -> str:
    """Print a party apple and return the text."""
    return _print_art(PARTY)


def love() -> str:
    """Print a love apple and return the text."""
    return _print_art(LOVE)


def random() -> str:
    """Print a random apple and return the text."""
    from random import choice

    return _print_art(choice(tuple(ARTS.values())))


def kinds() -> tuple[str, ...]:
    """Return the available apple names."""
    return (*ARTS.keys(), "random")


def main(kind: ArtName | None = None) -> str:
    """Print an apple from Python or the command line."""
    selected = kind or (sys.argv[1] if len(sys.argv) > 1 else "apple")
    if selected == "random":
        return random()
    return _print_art(ARTS.get(selected, APPLE))