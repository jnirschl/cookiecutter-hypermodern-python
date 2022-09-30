"""Test cases for the __main__ module."""
import pytest
from click.testing import CliRunner

from {{cookiecutter.package_name}} import __main__


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


class TestMain:
    """Test cases for the main() function."""

    def test_main_dry_run(self, runner: CliRunner) -> None:
        """Test dry run."""
        result = runner.invoke(__main__.main, ["--dry-run"])
        assert result.exit_code == 0

    def test_main_success(self, runner: CliRunner) -> None:
        """Test successful run."""
        result = runner.invoke(__main__.main)
        assert result.exit_code == 0


    def test_main_version(self, runner: CliRunner) -> None:
        """Test version."""
        result = runner.invoke(__main__.main, ["--version"])
        assert result.exit_code == 0
        assert result.output == f"{__main__.__version__}"
