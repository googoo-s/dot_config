import logging

from dot.const import CONFIG_PATH, HOME
from dot.settings import SETTINGS
from dot.soft import BaseSoft
from dot.utils import create_file_from_template, make_link, rm, rm_link

GIT_CONFIG_PATH = CONFIG_PATH.joinpath("git")


class Git(BaseSoft):
    def get_dependency_program_name(self) -> list[str]:
        return ["git"]

    def check(self):
        pass

    def install(self):
        logging.warning("git install")
        create_file_from_template(
            GIT_CONFIG_PATH.joinpath(".gitconfig.jinja").absolute(),
            GIT_CONFIG_PATH.joinpath(".gitconfig").absolute(),
            SETTINGS["git"],
        )
        make_link(GIT_CONFIG_PATH.joinpath(".gitconfig").absolute(), HOME.joinpath(".gitconfig").absolute(), True)

    def clean_link(self):
        rm_link(HOME.joinpath(".gitconfig").absolute())

    def clean_gen_file(self):
        rm(GIT_CONFIG_PATH.joinpath(".gitconfig").absolute())
