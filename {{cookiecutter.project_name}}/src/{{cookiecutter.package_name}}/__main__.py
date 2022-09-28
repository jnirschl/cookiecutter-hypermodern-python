#!/usr/bin/env python3
"""Command-line interface for {{cookiecutter.package_name}}."""
import logging
from pathlib import Path

import click
from dotenv import find_dotenv
from dotenv import load_dotenv


@click.command()
@click.argument(
    "input-dir", type=click.Path(exists=True, path_type=Path),
)
@click.option(
    "--dry-run", is_flag=True, help="Perform a trial run with no changes made."
)
@click.version_option()
def main(input_dir: Path, dry_run: bool = False,) -> None:
    """Docstring."""
    logger = logging.getLogger(__name__)
    logger.info(f"Input directory: {input_dir}")
    if dry_run:
        logger.info(" Dry run ")


if __name__ == "__main__":
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()