import asyncio
import configparser
import json
from pathlib import Path
from typing import List, Optional

import typer

from drivy_tools.config import Config, default_config, default_drivy_tools_dir
from drivy_tools.src.drivy_api import DrivyAPI
from drivy_tools.src.enums import CITY_GENT
from drivy_tools.src.utils import get_all_earnings, save_csv, time_it
from drivy_tools.state import state

app = typer.Typer()
estimate_app = typer.Typer()
app.add_typer(estimate_app, name="estimate")


@app.command(name="config")
def config(
    list_: Optional[bool] = typer.Option(False, "--list"), delete: Optional[bool] = typer.Option(False, "--delete")
):
    if not default_drivy_tools_dir.exists():
        is_config_wanted = typer.confirm("Config file doesn't exist! Do you want to create?")
        if is_config_wanted:
            default_drivy_tools_dir.mkdir()
            config_ = configparser.ConfigParser()
            edit = typer.confirm("Do you want to change default values?")
            for key, value in default_config.dict().items():
                if edit:
                    print(f"Section: {key}")
                    for indent_key, indent_val in value.items():
                        value[indent_key] = typer.prompt(indent_key, default=indent_val)
                config_[key] = value
            with open(default_drivy_tools_dir.joinpath("config").with_suffix(".ini"), "w") as configfile:
                config_.write(configfile)
                print("Config file is created!")
            config_.read(default_drivy_tools_dir.joinpath("config").with_suffix(".ini"))
            return json.loads(json.dumps(dict(config_), default=lambda o: dict(o)))
        return None

    if delete:
        for thing in default_drivy_tools_dir.iterdir():
            if thing.is_file():
                thing.unlink()
            else:
                for th in thing.iterdir():
                    th.unlink()
                thing.rmdir()
        default_drivy_tools_dir.rmdir()
        if state.verbose:
            print("Config file is deleted!")
        return None

    if list_:
        config_ = configparser.ConfigParser()
        config_.read(default_drivy_tools_dir.joinpath("config").with_suffix(".ini"))
        print(Config(**dict(config_)).json(indent=4))
        return None

    config_ = configparser.ConfigParser()
    config_.read(default_drivy_tools_dir.joinpath("config").with_suffix(".ini"))
    return Config(**dict(config_))


@estimate_app.command("earnings")
def estimate_earnings(brands_to_pass: List[str] = typer.Option([], "--brand-to-pass", "-b")):
    verbose = False
    loop = asyncio.get_event_loop()
    drivy_api = DrivyAPI(verbose=state.verbose)
    city = CITY_GENT.copy()

    results_dir = Path(state.config["DEFAULT"]["results_dir"])
    results_dir.mkdir(exist_ok=True)

    results = loop.run_until_complete(get_all_earnings(str(results_dir), drivy_api, city, brands_to_pass, verbose))

    save_csv(results_dir=results_dir, header=list(results[0].keys()), results=results, name_of_csv="all_brands")

    loop.run_until_complete(drivy_api.close())


@estimate_app.command("results")
def get_results():
    results_dir = Path(state.config["DEFAULT"]["results_dir"])
    print(list(results_dir.rglob("*")))


@app.command()
def hello():
    print("Welcome to Drivy analyzer")


@app.callback()
def callback(
    verbose: bool = typer.Option(False, "-v", "--verbose", help="Print the details of the running operations")
):
    if verbose:
        state.verbose = True

    state.config = time_it(config)(list_=False, delete=False)
    if state.verbose:
        print(state.config.json(indent=4))
