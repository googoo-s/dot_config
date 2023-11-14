import ctypes
import distutils.spawn as spawn
import os
import sys

import click
from jinja2 import Template

from dot import error

is_windows = bool(sys.platform == "win32")
is_mac = bool(sys.platform == "darwin")


def check_executable(name):
    """check if executable exists. (raise exeception if not)"""
    if not spawn.find_executable(name):
        raise error.DotError(f"there is no {name} executable")


def find_executable(name):
    return spawn.find_executable(name)


def check_file(path):
    """check if file exists. (raise exeception if not)"""
    if not os.path.exists(path):
        raise error.DotError(f"there is no {path} file")


def full_path(*paths):
    """接收一系列路径（path）作为输入，并返回这些路径的绝对路径"""

    def _f(p):
        return os.path.abspath(os.path.expanduser(str(p)))

    if len(paths) == 1:
        return _f(paths[0])
    return map(_f, paths)


def is_superuser():
    if is_windows:
        return bool(ctypes.windll.shell32.IsUserAnAdmin())
    return os.getuid() == 0


def make_link(target, link_path, force=False):
    error.LinkError.check(is_windows and not is_superuser(), "必须使用管理员权限来建立文件软链接")

    target, link_path = full_path(target, link_path)
    if os.path.lexists(link_path):
        if force:
            rm(link_path)
        else:
            raise error.LinkError(f"{link_path} 已经存在, 请指定 --force ")

    kwargs = {}
    if is_windows and os.path.isdir(target):
        kwargs["target_is_directory"] = True
    os.symlink(target, link_path, **kwargs)


def rm_link(path):
    if not os.path.lexists(path):
        return
    rm(path)


def rm(path):
    if not os.path.exists(path):
        return
    if os.path.isdir(path):
        os.rmdir(path)
    else:
        os.remove(path)


def run(*commands):
    """run commands"""
    for command in commands:
        click.echo(f"(Running)> {command}")
        os.system(command)


def create_file_from_template(template_path: str, output_path: str, data: dict):
    check_file(template_path)
    template = Template(open(template_path).read())

    with open(output_path, "w") as file:
        file.write(template.render(data))
