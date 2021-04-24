"""entry point for the paragon CLI."""
import click
from paragon.benchmark import Paragon
from paragon.utils import Utils


@click.command()
@click.argument("code", nargs=-1)
@click.option(
    "--accuracy", "-a", required=False, help="Number of iterations", default=1
)
def cli(code: str, accuracy: int):
    """entry point for the paragon CLI.

    :param code: the code to benchmark
    :param accuracy: number of iterations
    """
    for idx, val in enumerate(code):
        click.secho(f"Benchmark #{idx + 1}", fg="white", bold=True)
        try:
            Paragon.bench(val, accuracy)
        except Exception as e:
            Utils.reset_stdout()
            click.echo(f"Error: {e}", err=True)
            continue


if __name__ == "__main__":
    cli()
