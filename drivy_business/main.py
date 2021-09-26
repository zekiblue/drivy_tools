import asyncio
from typing import List

import typer

from drivy_business.src.drivy_api import DrivyAPI
from drivy_business.src.enums import year_id_map, km_id_map, CITY_GENT
from drivy_business.src.models import VehicleModel
from drivy_business.src.utils import get_all_earnings

app = typer.Typer()


@app.command()
def get_earnings():
    loop = asyncio.get_event_loop()
    drivy_api = DrivyAPI()
    city = CITY_GENT.copy()

    loop.run_until_complete(get_all_earnings(drivy_api, city))
    # brand_id = 2
    # # models: List[VehicleModel] = asyncio.run(drivy_api.get_models(brand_id))
    # # model_id = models[0].id
    # model_id = 11
    # year_id = list(year_id_map.keys())[0]
    # km_id = list(km_id_map.keys())[0]
    # response = loop.run_until_complete(drivy_api.get_estimated_earning(brand_id, model_id, year_id, km_id, city))
    # loop.run_until_complete(drivy_api.close())


if __name__ == '__main__':
    app()
