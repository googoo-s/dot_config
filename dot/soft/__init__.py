from dot.soft.basesoft import BaseSoft
from dot.soft.bash import Bash
from dot.soft.git import Git
from dot.soft.maven import Maven
from dot.soft.package import Package


def get_soft_list() -> list[BaseSoft]:
    return [Git(), Package(), Bash(), Maven()]
