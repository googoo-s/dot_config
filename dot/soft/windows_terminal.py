import logging

from dot.const import CONFIG_PATH, HOME
from dot.soft import BaseSoft
from dot.utils import make_link, rm_link,is_windows

WINDOWS_TERMINAL_CONFIG_PATH = CONFIG_PATH.joinpath("windows_terminal/settings.json")
WINDOWS_TERMINAL_PATH = HOME.joinpath(
    "AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState/settings.json")


class WindowsTerminal(BaseSoft):
    def get_dependency_program_name(self) -> list[str]:
        return []

    def check(self):
        pass

    def install(self):
        if is_windows:
            logging.warning("windows terminal install")
            make_link(WINDOWS_TERMINAL_CONFIG_PATH.absolute(), WINDOWS_TERMINAL_PATH.absolute(), True)

    def clean_link(self):
        if is_windows:
            rm_link(WINDOWS_TERMINAL_PATH.absolute())

    def clean_gen_file(self):
        pass
