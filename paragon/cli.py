import click
from paragon.benchmark import Benchmark
from paragon.utils import Utils


@click.command()
@click.argument("code", nargs=-1)
@click.option(
    "--accuracy", "-a", required=False, help="Number of iterations", default=1
)
def cli(code, accuracy):
    for i in range(len(code)):
        click.secho(f"Benchmark #{i + 1}", fg="white", bold=True)
        try:
            Benchmark.bench(code[i], accuracy)
        except Exception as e:
            Utils.reset_stdout()
            click.echo(f"Error: {e}", err=True)
            continue


if __name__ == "__main__":
    cli()
