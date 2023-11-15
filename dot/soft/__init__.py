from typing import Optional

from dot.soft.basesoft import BaseSoft
from dot.soft.bash import Bash
from dot.soft.git import Git
from dot.soft.idea import Idea
from dot.soft.maven import Maven
from dot.soft.package import Package
from dot.soft.wezterm import Wezterm
from dot.soft.emacs import Emacs
from dot.soft.windows_terminal import WindowsTerminal


def get_soft_list() -> list[BaseSoft]:
    return [Git(),
            Package(),
            Bash(),
            Maven(),
            Wezterm(),
            Idea(),
            WindowsTerminal(),
            Emacs()
            ]


def get_soft_by_name(soft: str) -> Optional[BaseSoft]:
    # bash, emacs, git, idea, maven, package, wezterm, windows_terminal
    if soft == 'bash':
        return Bash()
    if soft == 'emacs':
        return Emacs()
    if soft == 'git':
        return Git()
    if soft == 'idea':
        return Idea()
    if soft == 'maven':
        return Maven()
    if soft == 'package':
        return Package()
    if soft == 'wezterm':
        return Wezterm()
    if soft == 'windows_terminal':
        return WindowsTerminal()
    return None
