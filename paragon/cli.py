"""entry point for the paragon CLI."""
# pylint: disable = no-value-for-parameter

from typing import List
import click
from paragon import Paragon
from paragon.mark import Mark
from paragon.utils import Utils


@click.command()
@click.argument("code", nargs=-1)
@click.option(
    "--accuracy",
    "-a",
    required=False,
    default=1,
    help="Number of iterations",
)
@click.option(
    "--files",
    "-f",
    required=False,
    multiple=True,
    help="Input file path(s)",
    type=click.Path(),
)
@click.option(
    "--output",
    "-o",
    required=False,
    nargs=1,
    help="Output file path",
    type=click.Path(),
)
def cli(code: List[str], accuracy: int, files: List[str], output: str):
    """entry point for the paragon CLI."""

    # nothing to benchmark
    if len(code) == 0 and len(files) == 0:
        click.echo("You must provide python code to benchmark.", err=True)
        return

    start, current_benchmark = Mark(), 1

    if code:
        bench_code(code, current_benchmark, accuracy)

    if files:
        bench_files(files, current_benchmark, accuracy)

    if output:
        print(output)

    print(f"✨ Done in {start.diff()} s ✨")


def bench_code(code: List[str], current_benchmark: int, accuracy: int):
    """runs benches for all passed in code"""
    for val in code:
        click.secho(f"Benchmark #{current_benchmark}: {val}", fg="white", bold=True)
        try:
            Paragon.bench(code=val, accuracy=accuracy)
        except (NameError, SyntaxError) as error:
            click.echo(f"Error: {error}", err=True)
        current_benchmark += 1


def bench_files(files: List[str], current_benchmark: int, accuracy: int):
    """runs benches for all passed in files"""
    for file in files:
        res, name, status = Utils.verify_file(file)

        click.secho(f"Benchmark #{current_benchmark}: {name}", fg="white", bold=True)

        if not status:
            click.echo(res + "\n", err=True)
            continue

        try:
            Paragon.bench(code=res, accuracy=accuracy)
        except (NameError, SyntaxError) as error:
            click.echo(f"Error: {error}", err=True)

        current_benchmark += 1


if __name__ == "__main__":
    cli()
