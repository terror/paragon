"""entry point for the paragon CLI."""
# pylint: disable = no-value-for-parameter

from typing import List
import click
from paragon import Paragon
from paragon.exporter import Exporter
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

    start, current_benchmark = Mark(), [1]

    if code:
        bench_code(code, current_benchmark, accuracy)

    if files:
        bench_files(files, current_benchmark, accuracy)

    if output:
        Exporter.export_results(output)

    print("✨ Done in {:.2f} s ✨".format(start.diff()))


def bench_code(code: List[str], current_benchmark: List[int], accuracy: int):
    """runs benches for all passed in code"""
    for val in code:
        try:
            Paragon.bench(data=(val, val, *current_benchmark), accuracy=accuracy)
        except (NameError, SyntaxError) as error:
            click.echo(f"Error: {error}", err=True)

        current_benchmark[0] += 1


def bench_files(files: List[str], current_benchmark: List[int], accuracy: int):
    """runs benches for all passed in files"""
    for file in files:
        res, name, status = Utils.verify_file(file)

        if not status:
            click.echo(res + "\n", err=True)
            continue

        try:
            Paragon.bench(data=(res, name, *current_benchmark), accuracy=accuracy)
        except (NameError, SyntaxError) as error:
            click.echo(f"Error: {error}", err=True)

        current_benchmark[0] += 1


if __name__ == "__main__":
    cli()
