"""entry point for the paragon CLI."""
# pylint: disable = no-value-for-parameter
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
    "--file",
    "-f",
    required=False,
    nargs=1,
    help="Input file path",
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
def cli(code: str, accuracy: int, file: str, output: str):
    """entry point for the paragon CLI."""

    start = Mark()
    current_benchmark = 1
    for val in code:
        click.secho(f"Benchmark #{current_benchmark}", fg="white", bold=True)
        try:
            Paragon.bench(val, accuracy)
        except SyntaxError as error:
            click.echo(f"Error: {error}", err=True)
        current_benchmark += 1

    if file:
        res, status = Utils.verify_file(file)

        if not status:
            click.echo(res, err=True)
            return

        click.secho(f"Benchmark #{current_benchmark}", fg="white", bold=True)
        try:
            Paragon.bench(res, accuracy)
        except SyntaxError as error:
            click.echo(f"Error: {error}", err=True)

    if output:
        print(output)

    print(f"✨ Done in {start.diff()} s ✨")


if __name__ == "__main__":
    cli()
