from pydantic import BaseConfig


class Config(BaseConfig):
    httpx_max_keepalive_conn = 2
    httpx_max_conn = 5


config = Config()
