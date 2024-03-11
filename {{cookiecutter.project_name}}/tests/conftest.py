#!/usr/bin/env python3
"""Configure shared fixtures for {{cookiecutter.package_name}}."""

import os
import random
from pathlib import Path

import pytest
from click.testing import CliRunner
from faker import Faker


os.environ["WANDB_MODE"] = "dryrun"
os.environ["LOGGING_LEVEL"] = "DEBUG"


@pytest.fixture()
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


@pytest.fixture()
def temp_dir(tmp_path_factory) -> str:
    """Create a temporary directory with subdirectories for each class."""
    temp_dir = tmp_path_factory.mktemp("test_dir")

    return temp_dir.as_posix()


@pytest.fixture()
def temp_filepath():
    """Return fake filepath."""
    fake = Faker()
    return fake.file_path(category="image")


@pytest.fixture()
def invalid_dir() -> str:
    """Create a temporary directory with subdirectories for each class."""
    depth = random.randint(1, 5)
    absolute = random.choice([True, False])
    return Path(Faker().file_path(depth=depth, absolute=absolute)).parent.as_posix()
