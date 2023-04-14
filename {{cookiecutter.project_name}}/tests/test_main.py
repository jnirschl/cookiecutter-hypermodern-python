"""Test cases for the __main__ module."""
import logging
import re
from typing import Any

import pytest
from click.testing import CliRunner

from {{cookiecutter.package_name}} import __main__


@pytest.fixture()
def caplog_info(caplog: Any) -> Any:
    """Capture log messages at the INFO level."""
    caplog.set_level(logging.INFO)
    return caplog


class TestMain:
    """Test cases for the main() function."""

    def test_main_dry_run(
        self, runner: CliRunner, temp_dir: str, caplog_info: Any
    ) -> None:
        """Test dry run."""
        result = runner.invoke(__main__.main, [temp_dir, "--dry-run"])
        assert result.exit_code == 0
        assert "Dry run" in caplog_info.text

    def test_main_success(
        self, runner: CliRunner, temp_dir: str, caplog_info: Any
    ) -> None:
        """Test successful run."""
        result = runner.invoke(__main__.main, [temp_dir])
        assert result.exit_code == 0
        assert "Success" in caplog_info.text

    def test_main_version(self, runner: CliRunner, temp_dir: str) -> None:
        """Test version."""
        result = runner.invoke(__main__.main, [temp_dir, "--version"])
        assert result.exit_code == 0
        assert (
            re.search(r"\d+\.\d+\.\d+", result.output)[0] == f"{__main__.__version__}"
        )

    def test_invalid_input_dir(self, runner: CliRunner, invalid_dir: str) -> None:
        """Fail when input directory does not exist."""
        result = runner.invoke(__main__.main, [invalid_dir])
        assert result.exit_code == 2
        assert "Invalid value for 'INPUT_DIR'" in result.output
