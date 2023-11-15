import os

import click

import dot.const as dot_const
import dot.error as dot_error
import dot.soft as dot_soft
import dot.utils as dot_utils
from dot.soft import BaseSoft


@click.group()
def entry():
    """命令group"""


def precheck():
    if os.path.abspath(dot_const.PROJECT_PATH) != os.getcwd():
        raise dot_error.DotError(f"当前目录不是{dot_const.PROJECT_PATH}")
    if not dot_const.PROJECT_SETTINGS_PATH.exists():
        raise dot_error.DotError(f"配置文件{dot_const.PROJECT_SETTINGS_PATH}不存在")


def get_soft_list(soft: str, all_soft: bool) -> list[BaseSoft]:
    if all_soft is True:
        return dot_soft.get_soft_list()
    soft_config = dot_soft.get_soft_by_name(soft)
    if soft_config is None:
        return []
    else:
        return [soft_config]


SOFT_PROMPT = 'some config'
SOFT_HELP = 'some config ,such as bash,emacs,git,idea,maven,package,wezterm,windows_terminal '
ALL_SOFT_PROMPT = 'install all config'
ALL_SOFT_Help = 'install all config'


@entry.command()
@click.option("-s", "--soft", help=SOFT_HELP)
@click.option("-a", "--all_soft", is_flag=True, default=False, help=ALL_SOFT_PROMPT)
def install(soft, all_soft):
    print(soft, all_soft)
    """install config"""
    if soft is None and all_soft is None:
        print("option is necessary")
    precheck()
    for soft in get_soft_list(soft, all_soft):
        soft.must_install()


@entry.command()
@click.option("-s", "--soft", help=SOFT_HELP)
@click.option("-a", "--all_soft", is_flag=True, default=False, help=ALL_SOFT_PROMPT)
def uninstall(soft, all_soft):
    """uninstall config """
    if soft is None and all_soft is None:
        print("option is necessary")
    precheck()
    for soft in get_soft_list(soft, all_soft):
        soft.uninstall()


@entry.command()
@click.option("-s", "--soft", help=SOFT_HELP)
@click.option("-a", "--all_soft", is_flag=True, default=False,
              help=ALL_SOFT_PROMPT)
def clean_gen_file(soft, all_soft):
    """delete gen file"""
    if soft is None and all_soft is None:
        print("option is necessary")
    precheck()
    for soft in get_soft_list(soft, all_soft):
        soft.clean_gen_file()


@entry.command()
def rebase():
    """rebase this repo"""
    precheck()
    dot_utils.run(f"git -C {dot_const.PROJECT_PATH} pull --rebase")


@entry.command()
@click.argument("target")
@click.argument("link_path")
@click.option("-f", "--force", is_flag=True, default=False)
def link(target, link_path, force):
    """link target to link_path

    Examples:
        lki link /usr/bin/python3 /usr/bin/python
    """
    dot_utils.make_link(target, link_path, force=force)
