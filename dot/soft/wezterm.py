from dot.const import CONFIG_PATH, HOME
from dot.soft import BaseSoft
from dot.utils import make_link, rm_link

WEZTERM_CONFIG_PATH = CONFIG_PATH.joinpath("wezterm")
WEZTERM_PATH = HOME.joinpath(".config/wezterm")


class Wezterm(BaseSoft):
    def get_dependency_program_name(self) -> list[str]:
        return []

    def check(self):
        pass

    def install(self):
        make_link(WEZTERM_CONFIG_PATH.absolute(), WEZTERM_PATH.absolute(), True)

    def clean_link(self):
        rm_link(WEZTERM_PATH.absolute())

    def clean_gen_file(self):
        pass
