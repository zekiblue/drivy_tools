from typing import Any

import httpx
from pydantic import BaseModel

from drivy_tools.src.config import config
from drivy_tools.src.models import CityDetails, VehicleModel


class DrivyAPI(BaseModel):
    verbose: bool = True
    client: Any

    headers = {
        "authority": "be.getaround.com",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="92", "Opera";v="78"',
        "accept": "application/json, text/javascript, */*; q=0.01",
        # 'x-csrf-token': 'qCsmTOmwAZtBbOO1vvxpQgam7SvnAXJtz37V7cvtVZiE0HCLr9wwCI91tT45MKVc3K4RuJbY95PhQgMblNHoNQ==',
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/92.0.4515.159 Safari/537.36 OPR/78.0.4093.184",
        # 'x-requested-with': 'XMLHttpRequest',
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://be.getaround.com/je-auto-verhuren",
        "accept-language": "en-US,en;q=0.9",
    }

    def __init__(self, **data: Any):
        max_keepalive_conn = data.pop("max_keepalive_connections", config.httpx_max_keepalive_conn)
        max_conn = data.pop("max_connections", config.httpx_max_conn)
        limits = httpx.Limits(max_keepalive_connections=max_keepalive_conn, max_connections=max_conn)
        data["client"] = httpx.AsyncClient(limits=limits)
        super().__init__(**data)

    async def close(self):
        await self.client.aclose()

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
        if "car_model_estimation_result_amount" in response.text:
            earning = response.text.split('"car_model_estimation_result_amount\\">€')[1]
            earning = earning.split("</span")[0].strip()
        else:
            earning = None
        self.print(earning)
        return earning

    async def get_header(self):
        resp = await self.client.get("https://be.getaround.com/je-auto-verhuren", headers=self.headers)

        # print(resp.cookies)
        meta_loc = resp.text.find('meta name="csrf-token"')
        estimate_text = resp.text[meta_loc : meta_loc + 200]
        csrf_token = estimate_text.split('"')[3]
        return csrf_token

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
