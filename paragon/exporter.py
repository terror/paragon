"""handles all exporting logic"""
import csv
import enum
import json
import click
from paragon import Paragon
from paragon.utils import Utils


class Format(enum.Enum):
    """file types as enums"""

    MARKDOWN = 1
    JSON = 2
    CSV = 3


class Exporter:
    """handles writing to various file formats"""

    @staticmethod
    def export_results(path: str):
        """writes results to a file"""
        _, ext = Utils.get_filename_ext(path)

        if ext not in [".md", ".json", ".csv"]:
            click.echo("Output file must be of type markdown, csv or json.\n", err=True)
            return

        with open(path, "w+") as out:
            Exporter.write(Format(Utils.format_to_int(ext)), out)

        click.echo(f"Successfully exported results to {path}\n")

    @staticmethod
    def write(fmt: Format, out: str):
        """builds and writes different outputs based on file format"""

        results = {
            result["name"]: {"average": result["average"], "range": result["range"]}
            for result in Paragon.results
        }

        if fmt == Format.JSON:
            json.dump(results, out, indent=4)

        if fmt == Format.MARKDOWN:
            table = "| Program | Average [s] | Min [s] | Max [s] |\n|---|---|---|---|\n"
            for key, val in results.items():
                table += f"| `{key}` | {val['average']} | {val['range'][0]} | {val['range'][1]} |\n"
            out.write(table)

        if fmt == Format.CSV:
            writer = csv.DictWriter(
                out, fieldnames=["Program", "Average [s]", "Min [s]", "Max [s]"]
            )

            writer.writeheader()

            for key, val in results.items():
                writer.writerow(
                    {
                        "Program": key,
                        "Average [s]": val["average"],
                        "Min [s]": val["range"][0],
                        "Max [s]": val["range"][1],
                    }
                )
