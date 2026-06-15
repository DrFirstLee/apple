# apple

Print cute text apples from Python.

## Install

```bash
pip install apple
```

If the `apple` name is already taken on PyPI, rename the project in `pyproject.toml` before publishing.

## Usage

```python
import apple

apple.apple()
apple.rotten()
apple.green()
apple.bite()
apple.basket()
```

Each function prints the apple art and also returns it as a string.

## Command Line

```bash
apple
```

## Build and Publish

```bash
python -m pip install --upgrade build twine
python -m build
python -m twine upload dist/*
```