# Contributing

## Installing

- `brew install pipx`
- `pipx ensurepath`
- `pipx install poetry==1.8.2`
- `poetry config pypi-token.pypi ***`

## Updating

- `poetry install`
- `source .venv/bin/activate`
- `pip install -e .`
- `poetry version patch`
- `poetry build`
- `git add -A`
- `git commit -m "message"`
- `git push`
- `poetry publish`
