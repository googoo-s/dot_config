import logging

from dot.const import CONFIG_PATH, HOME
from dot.settings import SETTINGS
from dot.soft import BaseSoft
from dot.utils import create_file_from_template, make_link, rm, rm_link

MAVEN_CONFIG_PATH = CONFIG_PATH.joinpath("maven")
M2_PATH = HOME.joinpath(".m2")


class Maven(BaseSoft):
    def get_dependency_program_name(self) -> list[str]:
        return []

    def check(self):
        pass

    def install(self):
        logging.warning("maven install")
        create_file_from_template(
            MAVEN_CONFIG_PATH.joinpath("settings.xml.jinja").absolute(),
            MAVEN_CONFIG_PATH.joinpath("settings.xml").absolute(),
            SETTINGS["maven"],
        )
        make_link(MAVEN_CONFIG_PATH.joinpath("settings.xml").absolute(), M2_PATH.joinpath("settings.xml").absolute(), True)

    def clean_link(self):
        rm_link(M2_PATH.joinpath("settings.xml").absolute())

    def clean_gen_file(self):
        rm(MAVEN_CONFIG_PATH.joinpath("settings.xml").absolute())
