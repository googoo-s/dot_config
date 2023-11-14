import os

import click

import dot.const as dot_const
import dot.error as dot_error
import dot.soft as dot_soft
import dot.utils as dot_utils


@click.group()
def entry():
    """命令group"""


@entry.command()
def show():
    print(dot_const.CONFIG_PATH)
    print(os.getcwd())
    print(os.path.abspath(dot_const.PROJECT_PATH))
    print(os.path.abspath(dot_const.PROJECT_PATH) == os.getcwd())


def precheck():
    if os.path.abspath(dot_const.PROJECT_PATH) != os.getcwd():
        raise dot_error.DotError(f"当前目录不是{dot_const.PROJECT_PATH}")
    if not dot_const.PROJECT_SETTINGS_PATH.exists():
        raise dot_error.DotError(f"配置文件{dot_const.PROJECT_SETTINGS_PATH}不存在")


@entry.command()
def install():
    """安装配置"""
    precheck()
    for soft in dot_soft.get_soft_list():
        soft.must_install()


@entry.command()
def uninstall():
    """删除生成的文件"""
    for soft in dot_soft.get_soft_list():
        soft.uninstall()


@entry.command()
def clean_gen_file():
    """删除生成的文件"""
    for soft in dot_soft.get_soft_list():
        soft.clean_gen_file()


@entry.command()
def rebase():
    """重新建立软链接"""
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
