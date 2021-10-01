import configparser
import json

import typer

from drivy_tools.config import Config, default_drivy_tools_dir
from drivy_tools.state import state


def create_drivy_folder_and_config_file(config: Config):
    if not default_drivy_tools_dir.exists():
        is_config_wanted = typer.confirm("Config file doesn't exist! Do you want to create?")
        if is_config_wanted:
            default_drivy_tools_dir.mkdir()
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


def delete_config_folder():
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
