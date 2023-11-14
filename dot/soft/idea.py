import logging

from dot.const import CONFIG_PATH, HOME
from dot.soft import BaseSoft
from dot.utils import make_link, rm_link

IDEA_CONFIG_PATH = CONFIG_PATH.joinpath("idea")
IDEA_VIM_PATH = HOME.joinpath(".ideavimrc")


class IDEA(BaseSoft):
    def get_dependency_program_name(self) -> list[str]:
        return []

    def check(self):
        pass

    def install(self):
        logging.warning("ideavimrc install")
        make_link(IDEA_CONFIG_PATH.joinpath(".ideavimrc").absolute(), IDEA_VIM_PATH.absolute(), True)

    def clean_link(self):
        rm_link(IDEA_VIM_PATH.absolute())

    def clean_gen_file(self):
        pass
