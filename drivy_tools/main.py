import asyncio
from typing import List

import typer

from drivy_tools.src.drivy_api import DrivyAPI
from drivy_tools.src.enums import CITY_GENT
from drivy_tools.src.utils import get_all_earnings, save_csv

app = typer.Typer()
estimate_app = typer.Typer()
app.add_typer(estimate_app, name="estimate")


@estimate_app.command("earnings")
def estimate_earnings(brands_to_pass: List[str] = typer.Option([], "--brand-to-pass", "-b")):
    verbose = False
    loop = asyncio.get_event_loop()
    drivy_api = DrivyAPI(verbose=verbose)
    city = CITY_GENT.copy()

    results = loop.run_until_complete(get_all_earnings(drivy_api, city, brands_to_pass, verbose))

    save_csv(header=list(results[0].keys()), results=results, name_of_csv="all_brands")

    loop.run_until_complete(drivy_api.close())


@app.command()
def hello():
    print("Welcome to Drivy analyzer")


def main():
    app()


if __name__ == "__main__":
    app()
