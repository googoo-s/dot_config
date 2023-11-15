import logging

from dot.const import CONFIG_PATH, HOME
from dot.soft import BaseSoft
from dot.utils import make_link, rm_link

EMACS_CONFIG_PATH = CONFIG_PATH.joinpath(".emacs.d")
EMACS_PATH = HOME.joinpath(".emacs.d")


class Emacs(BaseSoft):
    def get_dependency_program_name(self) -> list[str]:
        return []

    def check(self):
        pass

    def install(self):
        logging.warning("emacs install")
        make_link(EMACS_CONFIG_PATH.absolute(), EMACS_PATH.absolute(), True)

    def clean_link(self):
        rm_link(EMACS_PATH.absolute())

    def clean_gen_file(self):
        pass
