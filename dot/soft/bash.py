from dot.const import CONFIG_PATH, HOME
from dot.settings import SETTINGS
from dot.soft import BaseSoft
from dot.utils import create_file_from_template, make_link, rm, rm_link, run

OH_MY_BASH_PATH = HOME.joinpath(".oh-my-bash")

BASH_CONFIG_PATH = CONFIG_PATH.joinpath("bash")


class Bash(BaseSoft):
    def get_dependency_program_name(self) -> list[str]:
        # neofetch
        return ["git"]

    def check(self):
        pass

    def install(self):
        if not OH_MY_BASH_PATH.exists():
            run(f"git clone -o o --recursive https://github.com/ohmybash/oh-my-bash.git {OH_MY_BASH_PATH}")
        # else:
        #     run(f"git -C {OH_MY_BASH_PATH} pull --rebase")

        create_file_from_template(
            BASH_CONFIG_PATH.joinpath("oh_my_bash.sh.jinja").absolute(),
            BASH_CONFIG_PATH.joinpath("oh_my_bash.sh").absolute(),
            SETTINGS["bash"],
        )
        create_file_from_template(
            BASH_CONFIG_PATH.joinpath("ssh.sh.jinja").absolute(),
            BASH_CONFIG_PATH.joinpath("ssh.sh").absolute(),
            SETTINGS["bash"],
        )
        make_link(BASH_CONFIG_PATH.joinpath(".bashrc").absolute(), HOME.joinpath(".bashrc").absolute(), True)

    def clean_link(self):
        rm_link(HOME.joinpath(".bashrc").absolute())

    def clean_gen_file(self):
        """重写建软链接"""
        rm(BASH_CONFIG_PATH.joinpath("oh_my_bash.sh").absolute())
        rm(BASH_CONFIG_PATH.joinpath("ssh.sh").absolute())
