# appple

Print cute text apples from Python.

## Install

```bash
pip install appple
```

The PyPI distribution name is `appple`, while the Python import name remains `apple`.

## Usage

```python
import apple

apple.apple()
apple.rotten()
apple.green()
apple.bite()
apple.basket()
apple.samsung()
apple.angry()
apple.cute()
apple.sexy()
apple.nerd()
apple.sleepy()
apple.doctor()
apple.money()
apple.party()
apple.love()
apple.random()
```

Each function prints the apple art and also returns it as a string.

To see every available apple name:

```python
apple.kinds()
```

## Command Line

```bash
appple
appple samsung
appple angry
appple random
```

## Build and Publish

```bash
python -m pip install --upgrade build twine
python -m build
python -m twine upload dist/*
```