import asyncio

import typer

from drivy_business.src.drivy_api import DrivyAPI

app = typer.Typer()


@app.command()
def get_cars():
    drivy_api = DrivyAPI()
    asyncio.run(drivy_api.get_models("98"))


if __name__ == '__main__':
    app()
