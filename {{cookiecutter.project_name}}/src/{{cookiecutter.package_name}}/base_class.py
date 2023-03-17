#!/usr/bin/env python3
"""base_class.py in {{cookiecutter.project_name}}/src/{{cookiecutter.package_name}}."""


class BaseClass(object):
    """Template for a base class."""

    def __init__(self, name: str):
        """Initialize BaseClass."""
        self.name = name

    def __repr__(self) -> str:
        """An unambiguous string representation of the class instance."""
        return f"{self.__class__.__name__}(name={self.name})"

    def __str__(self) -> str:
        """An easy-to-read string representation of the class."""
        return (
            f"{self.__class__.__name__}\n"
            f"\tName: {self.name}\n"
        )