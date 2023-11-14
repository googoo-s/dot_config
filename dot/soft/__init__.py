from dot.soft.basesoft import BaseSoft
from dot.soft.bash import Bash
from dot.soft.git import Git
from dot.soft.idea import IDEA
from dot.soft.maven import Maven
from dot.soft.package import Package
from dot.soft.wezterm import Wezterm
from dot.soft.windows_terminal import WindowsTerminal


def get_soft_list() -> list[BaseSoft]:
    return [Git(), Package(), Bash(), Maven(), Wezterm(), IDEA(), WindowsTerminal()]
