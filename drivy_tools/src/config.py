from pydantic import BaseConfig


class Config(BaseConfig):
    httpx_max_keepalive_conn = 5
    httpx_max_conn = 10


config = Config()
