"""Test cases for the __main__ module."""
import re

from click.testing import CliRunner

from {{cookiecutter.package_name}} import __main__



class TestMain:
    """Test cases for the main() function."""

    def test_main_dry_run(self, runner: CliRunner, temp_dir: str) -> None:
        """Test dry run."""
        result = runner.invoke(__main__.main, [temp_dir, "--dry-run"])
        assert result.exit_code == 0

    def test_main_success(self, runner: CliRunner, temp_dir: str) -> None:
        """Test successful run."""
        result = runner.invoke(__main__.main, [temp_dir])
        assert result.exit_code == 0

    def test_main_version(self, runner: CliRunner, temp_dir: str) -> None:
        """Test version."""
        result = runner.invoke(__main__.main, [temp_dir, "--version"])
        assert result.exit_code == 0
        assert (
            re.search(r"\d+\.\d+\.\d+", result.output)[0] == f"{__main__.__version__}"
        )
