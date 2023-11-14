import logging

from dot.soft import BaseSoft
from dot.utils import find_executable, is_mac, is_windows, run


class Package(BaseSoft):
    def get_dependency_program_name(self) -> list[str]:
        if not is_windows:
            return []
        # todo 这里find_executable 无法 windows 是否安装了scoop
        # return ["scoop"]
        return []

    def check(self):
        pass

    def install(self):
        logging.warning("package install")
        if is_windows:
            if not find_executable("7zip"):
                run("scoop install 7zip")
            if not find_executable("aria2"):
                run("scoop install aria2")
            if not find_executable("ctags"):
                run("scoop install ctags")
            if not find_executable("curl"):
                run("scoop install curl")
            if not find_executable("fzf"):
                run("scoop install fzf")
            if not find_executable("gcc"):
                run("scoop install gcc")
            if not find_executable("goneovim"):
                run("scoop install goneovim")
            if not find_executable("grep"):
                run("scoop install grep")
            if not find_executable("grpcurl"):
                run("scoop install grpcurl")
            if not find_executable("kind"):
                run("scoop install kind")
            if not find_executable("lazygit"):
                run("scoop install lazygit")
            if not find_executable("less"):
                run("scoop install less")
            if not find_executable("lf"):
                run("scoop install lf")
            if not find_executable("neofetch"):
                run("scoop install neofetch")
            if not find_executable("neovim"):
                run("scoop install neovim")
            if not find_executable("openssh"):
                run("scoop install openssh")
            if not find_executable("pyenv"):
                run("scoop install pyenv")
            if not find_executable("sed"):
                run("scoop install sed")
            if not find_executable("sudo"):
                run("scoop install sudo")
            if not find_executable("tldr"):
                run("scoop install tldr")
            if not find_executable("touch"):
                run("scoop install touch")
            if not find_executable("vagrant"):
                run("scoop install vagrant")
            if not find_executable("wget"):
                run("scoop install wget")
            if not find_executable("which"):
                run("scoop install which")
            if not find_executable("emacs"):
                run("scoop install emacs")
        elif is_mac:
            if not find_executable("fd"):
                run("brew install fd")
            if not find_executable("fzf"):
                run("brew install fzf")
            if not find_executable("lazygit"):
                run("brew install lazygit")
            if not find_executable("lf"):
                run("brew install lf")
            if not find_executable("neofetch"):
                run("brew install neofetch")
            if not find_executable("neovim"):
                run("brew install neovim")
            if not find_executable("pyenv"):
                run("brew install pyenv")
            if not find_executable("sudo"):
                run("brew install sudo")
            if not find_executable("tldr"):
                run("brew install tldr")
            if not find_executable("wget"):
                run("brew install wget")
            if not find_executable("emacs"):
                run("brew install emacs")

    def clean_link(self):
        pass

    def clean_gen_file(self):
        pass
