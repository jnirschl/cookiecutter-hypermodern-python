#!/usr/bin/env python3
"""Tests for project creation.
Portions of this code are from the cookiecutter-datascience project.
"""

import os

import pytest
import tomllib
from conftest import system_check


def no_curlies(filepath):
    """Utility to make sure no curly braces appear in a file.
    That is, was Jinja able to render everything?
    """
    with open(filepath, "r") as f:
        data = f.read()

    template_strings = ["{{", "}}", "{%", "%}"]

    template_strings_in_file = [s in data for s in template_strings]
    return not any(template_strings_in_file)


@pytest.mark.usefixtures("default_baked_project")
class TestCookieSetup(object):
    def test_project_name(self, default_args):
        project = self.path
        # check for input pytest args
        if pytest.param.get("project_name"):
            name = system_check("tesla-coil")
            assert project.name == name
        else:
            assert project.name == default_args["project_name"]

    def test_readme(self, default_args):
        readme_path = self.path.joinpath("README.md")
        assert readme_path.exists()
        assert no_curlies(readme_path)
        if pytest.param.get("project_name"):
            with open(readme_path) as fin:
                friendly_name = pytest.param["project_name"].replace("-", " ").title()
                assert "# " + friendly_name == next(fin).strip()
        else:
            with open(readme_path) as fin:
                friendly_name = default_args["project_name"].replace("-", " ").title()
                assert "# " + friendly_name == next(fin).strip()

    def test_license(self):
        license_path = self.path.joinpath("LICENSE")
        assert license_path.exists()
        assert no_curlies(license_path)

    def test_pyprojecttoml(self, default_args):
        pyproject_path = self.path.joinpath("pyproject.toml")
        assert pyproject_path.exists()
        assert no_curlies(pyproject_path)

        # load pyproject.toml
        with open(pyproject_path, "rb") as file:
            data = tomllib.load(file)

        # test values in pyproject.toml
        if pytest.param.get("project_name"):
            assert data["tool"]["poetry"]["name"] == pytest.param["project_name"]

            author_email = (
                pytest.param.get("author") + " <" + pytest.param.get("email") + ">"
            )
            for k, v in pytest.param.items():
                if k in data["tool"]["poetry"].keys():
                    if k == "author":
                        assert data["tool"]["poetry"]["authors"][0] == author_email
                    else:
                        assert data["tool"]["poetry"][k] == pytest.param[k]
        else:
            author_email = default_args["author"] + " <" + default_args["email"] + ">"
            assert data["tool"]["poetry"]["name"] == default_args["project_name"]
            assert data["tool"]["poetry"]["authors"][0] == author_email

    def test_folders(self):
        expected_dirs = [
            "docs",
            "src",
            "tests",
            ".github",
            ".github/workflows",
        ]

        ignored_dirs = [str(self.path)]

        abs_expected_dirs = [str(self.path.joinpath(d)) for d in expected_dirs]
        abs_dirs, _, _ = list(zip(*os.walk(self.path)))
        assert len(set(abs_expected_dirs + ignored_dirs) - set(abs_dirs)) == 0, print(
            f"SetDiff\t{set(abs_expected_dirs + ignored_dirs).difference(set(abs_dirs))}"
        )
