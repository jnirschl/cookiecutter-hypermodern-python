"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """{{ cookiecutter.project_name.replace('-', ' ').title() }}."""


if __name__ == "__main__":
    main(prog_name="{{cookiecutter.project_name}}")  # pragma: no cover
