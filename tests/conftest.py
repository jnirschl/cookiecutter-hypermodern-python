#!/usr/bin/env python3
"""Set up common fixtures and tests for the cookiecutter-hyppermodern-python template.
Portions of this code are from the cookiecutter-datascience project.
"""

import json
import shutil
import sys
from pathlib import Path

import pytest
from cookiecutter import main


CCDS_ROOT = Path(__file__).parents[1].resolve()

args = {
    "project_name": "tesla-coil",
    "author": "Nikola Tesla",
    "github_user": "octocat",
    "description": "A Tesla Coil is a radio frequency oscillator that drives a double-tuned resonant transformer to produce high voltages with low currents",
    "email": "user@mail.com",
    "license": "BSD-3",
    "copyright_year": "1891",
    "version": "1.0.0",
}


def system_check(basename):
    platform = sys.platform
    if "linux" in platform:
        basename = basename.lower()
    return basename


@pytest.fixture()
def custom_args():
    return custom_args


@pytest.fixture()
def default_args():
    with open("cookiecutter.json", "r") as file:
        default_args = json.load(file)
    return default_args


@pytest.fixture(scope="class", params=[{}, args])
def default_baked_project(tmp_path_factory, request):
    temp = tmp_path_factory.mktemp("data-project")
    out_dir = temp.resolve()

    pytest.param = request.param
    main.cookiecutter(
        str(CCDS_ROOT),
        no_input=True,
        extra_context=pytest.param,
        output_dir=out_dir,
        default_config=True,
    )

    pn = pytest.param.get("project_name") or "project-name"

    # project name gets converted to lower case on Linux but not Mac
    pn = system_check(pn)

    proj = out_dir / pn
    request.cls.path = proj
    yield

    # cleanup after
    shutil.rmtree(out_dir)
