import pathlib
import re

from dot import settings

REGEX_GIT_URLS = (
    re.compile(r"^git@([^:]+):(.*?)(.git)?$"),
    re.compile(r"^https?://([^/]+)/(.*?)(.git)?$"),
    re.compile(r"^ssh://git@([^/]+)/(.*?)(.git)?$"),
)

HOME = pathlib.Path(settings.SETTINGS["home"]).expanduser()
PROJECT_PATH = HOME.joinpath("dot_config")
CONFIG_PATH = PROJECT_PATH.joinpath("config")
PROJECT_SETTINGS_PATH = PROJECT_PATH.joinpath("settings.yaml")
WORKSPACE_PATH = HOME.joinpath("workspace")
