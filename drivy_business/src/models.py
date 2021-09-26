from typing import Any

from pydantic import BaseModel


class Model(BaseModel):
    id: int
    localized_label: str
    car_type_supports_dimensions: bool
    trunk_volume: Any