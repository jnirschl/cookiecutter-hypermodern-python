#!/usr/bin/env python3
"""subclass.py in {{cookiecutter.project_name}}/src/{{cookiecutter.package_name}}."""

from .base_class import BaseClass

class Subclass(BaseClass):
    """Template for a subclass."""

    def __init__(self, name: str, value: int):
        """Initialize Subclass."""
        super().__init__(name)
        self.value = value

    def __repr__(self) -> str:
        """An unambiguous string representation of the class instance."""
        return f"{self.__class__.__name__}(name={self.name}, value={self.value})"

    def __str__(self) -> str:
        """An easy-to-read string representation of the class."""
        return (
            f"{self.__class__.__name__}\n"
            f"\tName: {self.name}\n"
            f"\tValue: {self.value}\n"
        )