#!/usr/bin/env python
import json
import shutil
from pathlib import Path


def reindent_cookiecutter_json():
    """Indent .cookiecutter.json using two spaces.

    The jsonify extension distributed with Cookiecutter uses an indentation
    width of four spaces. This conflicts with the default indentation width of
    Prettier for JSON files. Prettier is run as a pre-commit hook in CI.
    """
    path = Path(".cookiecutter.json")

    with path.open() as io:
        data = json.load(io)

    with path.open(mode="w") as io:
        json.dump(data, io, sort_keys=True, indent=2)
        io.write("\n")


def remove_idea_folder():
    """Remove the idea folder created by the cookiecutter template."""
    path = Path(".idea")
    if path.exists():
        shutil.rmtree(path)


if __name__ == "__main__":
    reindent_cookiecutter_json()
