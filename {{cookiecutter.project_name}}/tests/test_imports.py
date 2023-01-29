#!/usr/bin/env python3
"""test_imports.py in tests."""

import pytest


@pytest.mark.smoke
def test_imports():
    """Test package imports."""
    import {{cookiecutter.package_name}}  # noqa: F401
