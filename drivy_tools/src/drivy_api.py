from typing import Any, List

from pydantic import BaseModel

from drivy_tools.src.client import HTTPClient
from drivy_tools.src.models import CityDetails, VehicleModel
from drivy_tools.src.parsing import parse_text_to_earning


class DrivyAPI(BaseModel):
    verbose: bool = True
    client: Any
    async_enabled: bool = True
    proxies: List[str]

    def __init__(self, **data: Any):
        data["client"] = HTTPClient(async_enabled=data["async_enabled"], proxies=data["proxies"])
        super().__init__(**data)

    async def close(self):
        await self.client.close()

    async def get_estimated_earning(self, brand_id: int, model_id: int, year_id: int, km_id: int, city: CityDetails):
        params = {
            "utf8": "\u2713",
            "car_model_estimation[car_brand_id]": str(brand_id),
            "car_model_estimation[car_model_id]": str(model_id),
            "car_model_estimation[release_year]": str(year_id),
            "car_model_estimation[mileage]": str(km_id),
            "car_model_estimation[city]": city.name,
            "car_model_estimation[city_country]": city.country,
            "car_model_estimation[latitude]": str(city.lat),
            "car_model_estimation[longitude]": str(city.long),
            "car_model_estimation[registration_country]": city.registration_country,
            # "car_model_estimation[with_open_landing_multiplier]": True,
        }
        url = "https://be.getaround.com/car_models/estimated_earnings"

        response = await self.client.get(url, params=params)
        earning = parse_text_to_earning(response.text)
        self.print(earning)
        return earning

    def print(self, anything):
        if self.verbose:
            print(anything)

    async def get_models(self, brand_id):
        params = {"make": str(brand_id)}
        url = "https://be.getaround.com/car_models/models"
        resp = await self.client.get(url, params=params)

        r = resp.json()
        models = []
        for model in r:
            models.append(VehicleModel(**model))

        self.print(models)

        return models
