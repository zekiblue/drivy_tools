import asyncio
import csv
from typing import List

import typer

from drivy_business.src.drivy_api import DrivyAPI
from drivy_business.src.enums import CITY_GENT
from drivy_business.src.utils import get_all_earnings, save_csv

app = typer.Typer()


@app.command("earnings")
def get_earnings():
    verbose = False
    loop = asyncio.get_event_loop()
    drivy_api = DrivyAPI(verbose=verbose)
    city = CITY_GENT.copy()

    results = loop.run_until_complete(get_all_earnings(drivy_api, city, verbose))

    save_csv(header=list(results[0].keys()), results=results, name_of_csv="all_brands")

    loop.run_until_complete(drivy_api.close())


@app.command()
def hello():
    print("Welcome to Drivy analyzer")


def main():
    app()


if __name__ == '__main__':
    app()
