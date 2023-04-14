#!/usr/bin/env python3
"""Tests for test_base_class.py."""
import random

import pytest

from {{cookiecutter.package_name}}.base_class import BaseClass


@pytest.fixture
def name():
    """Create a random name."""
    return "".join([chr(random.randint(97, 122)) for _ in range(10)])


@pytest.fixture
def base_class(name):
    """Create a BaseClass instance."""
    return BaseClass(name)


class TestBaseClass:
    """Tests for BaseClass."""

    def test_init(self, base_class, name):
        """Test BaseClass.__init__()."""
        assert base_class.name == name
        assert base_class.__repr__() == f"BaseClass(name={name})"
        assert base_class.__str__() == f"BaseClass\n\tName: {name}\n"
