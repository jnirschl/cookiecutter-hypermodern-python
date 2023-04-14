#!/usr/bin/env python3
"""Tests for test_base_class.py."""
import random

import pytest

from {{cookiecutter.package_name}}.subclass import Subclass

@pytest.fixture
def name():
    """Create a random name."""
    return "".join([chr(random.randint(97, 122)) for _ in range(10)])


@pytest.fixture
def value():
    """Create a random name."""
    return random.randint(0, 100)


@pytest.fixture
def subclass(name, value):
    """Create a BaseClass instance."""
    return Subclass(name, value)


class TestBaseClass:
    """Tests for BaseClass."""

    def test_init(self, subclass, name, value):
        """Test BaseClass.__init__()."""
        assert subclass.name == name
        assert subclass.value == value
        assert subclass.__repr__() == f"Subclass(name={name}, value={value})"
        assert subclass.__str__() == f"Subclass\n\tName: {name}\n\tValue: {value}\n"
