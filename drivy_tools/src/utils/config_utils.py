import configparser
import json

import typer

from drivy_tools.config import Config, default_drivy_tools_dir
from drivy_tools.state import state


def create_drivy_folder_and_config_file(config: Config):
    config_file_dir = default_drivy_tools_dir.joinpath("config").with_suffix(".ini")
    if not config_file_dir.exists():
        is_config_wanted = typer.confirm("Config file doesn't exist! Do you want to create?")
        if is_config_wanted:
            default_drivy_tools_dir.mkdir(exist_ok=True)
            config_ = configparser.ConfigParser()
            edit = typer.confirm("Do you want to change default values?")
            for key, value in config.dict().items():
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


def delete_config_folder(delete_folder: bool = False):
    for thing in default_drivy_tools_dir.iterdir():
        if thing.is_file():
            thing.unlink()
        else:
            if delete_folder:
                for th in thing.iterdir():
                    th.unlink()
                thing.rmdir()
    if delete_folder:
        default_drivy_tools_dir.rmdir()
    if state.verbose:
        print("Config file is deleted!")
    return None
