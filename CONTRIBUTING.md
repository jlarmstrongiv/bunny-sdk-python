# Contributing

## Installing

- `brew install pipx`
- `pipx ensurepath`
- `pipx install poetry==1.8.2`
- `poetry config pypi-token.pypi ***`

- VS Code extensions
  - `tamasfe.even-better-toml`
  - `ms-python.python`
  - `ms-python.vscode-pylance`
  - `ms-python.debugpy`
  - `charliermarsh.ruff`

## Updating

- Update dependencies `poetry update` and manually update `pyproject.toml`
- `poetry lock`
- `poetry install`
- `source .venv/bin/activate`
- `pip install -e .`
- `BUNNY_ACCESS_KEY="***" poetry run python3 tests/main.py`
- `poetry version patch`
- `poetry build`
- `git add -A`
- `git commit -m "message"`
- `git push`
- `poetry publish`
