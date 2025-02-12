#!/usr/bin/env python3
"""Command-line interface for {{cookiecutter.package_name}}."""
from pathlib import Path
from typing import Optional

import click
from dotenv import find_dotenv
from dotenv import load_dotenv
from loguru import logger

from {{cookiecutter.package_name}} import __version__

@click.command()
@click.argument(
    "input-dir", type=click.Path(file_okay=False, exists=True, path_type=Path)
)
@click.option(
    "--output-dir", type=click.Path(file_okay=False, exists=False, path_type=Path)
)
@click.option("--dry-run", is_flag=True, help="Perform a trial run with no changes.")
@click.option("--debug", is_flag=True, help="Enable debug/test mode.")
@click.version_option(__version__)
def main(
    input_dir: Path,
    output_dir: Optional[Path] = None,
    dry_run: bool = False,
    debug: bool = False,
) -> None:
    """Docstring."""
    output_dir = input_dir if output_dir is None else output_dir.resolve()

    project_dir = Path(__file__).resolve().parents[2]
    log_dir = project_dir.joinpath("logs")
    (
        None
        if debug
        else logger.add(
            log_dir.joinpath(f"{Path(__file__).stem}.log"),
            rotation="1 week",
            level="INFO",
        )
    )

    logger.info(f"Input dir: {input_dir}")
    logger.info(f"Output dir: {output_dir}")

    if dry_run:
        logger.info("Dry run: no changes will be made.")
        return


if __name__ == "__main__":
    load_dotenv(find_dotenv())

    main()
