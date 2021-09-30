from pathlib import Path

from pydantic import BaseModel, Field, SecretStr

default_drivy_tools_dir = Path.home().joinpath(".drivy_tools")


class DEFAULT(BaseModel):
    results_dir: Path = default_drivy_tools_dir.joinpath("results")
    async_enabled: bool = True
    random: bool = True


class WebScrapinAPIConfig(BaseModel):
    base_url: str = "www.websrapingapicom/v1?"
    api_key: SecretStr = ""


class HTTPX(BaseModel):
    httpx_max_keepalive_conn = 2
    httpx_max_conn = 5


class Config(BaseModel):
    DEFAULT: DEFAULT = DEFAULT()
    web_scraping_api: WebScrapinAPIConfig = Field(WebScrapinAPIConfig(), alias="https://www.webscrapingapi.com")
    HTTPX: HTTPX = HTTPX()


default_config = Config()
