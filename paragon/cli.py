"""entry point for the paragon CLI."""
# pylint: disable = no-value-for-parameter
from typing import List
import click
from paragon.benchmark import Paragon
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
    for val in code:
        click.secho(f"Benchmark #{current_benchmark}", fg="white", bold=True)
        try:
            Paragon.bench(val, accuracy)
        except (NameError, SyntaxError) as error:
            click.echo(f"Error: {error}", err=True)
        current_benchmark += 1

    if len(files):
        for file in files:
            res, status = Utils.verify_file(file)
            click.secho(f"Benchmark #{current_benchmark}", fg="white", bold=True)

            if not status:
                click.echo(res + "\n", err=True)
                continue

            try:
                Paragon.bench(res, accuracy)
            except (NameError, SyntaxError) as error:
                click.echo(f"Error: {error}", err=True)

            current_benchmark += 1

    if output:
        print(output)

    print(f"\n✨ Done in {start.diff()} s ✨")


if __name__ == "__main__":
    cli()
