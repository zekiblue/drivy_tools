from typing import Any

from pydantic import BaseModel


class VehicleModel(BaseModel):
    id: int
    localized_label: str
    car_type_supports_dimensions: bool
    trunk_volume: Any


class CityDetails(BaseModel):
    name: str
    country: str
    lat: float
    long: float
    registration_country: str
