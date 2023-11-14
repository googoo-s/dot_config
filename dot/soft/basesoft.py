import logging
from abc import ABC, abstractmethod
from typing import Optional

from dot.utils import find_executable


class BaseSoft(ABC):
    def env_has_program(self) -> Optional[bool]:
        """环境是否有程序
        return None 表示不需要依赖的程序
        return True 表示需要且有依赖的程序
        return False 表示需要，但是依赖的程序
        """
        names = self.get_dependency_program_name()
        if len(names) == 0:
            return None

        for program_name in names:
            if not find_executable(program_name):
                return False

        return True

    @abstractmethod
    def get_dependency_program_name(self) -> list[str]:
        """获取依赖的程序名"""
        return []

    @abstractmethod
    def check(self):
        """检查是否合规"""
        pass

    @abstractmethod
    def install(self):
        """安装配置"""
        pass

    def uninstall(self):
        """解除安装，包括：
        1.清除生成的文件
        2.解除软链接
        """
        self.clean_link()
        self.clean_gen_file()

    @abstractmethod
    def clean_link(self):
        """清楚软连接"""

    @abstractmethod
    def clean_gen_file(self):
        """清除生成的文件"""
        pass

    def must_install(self):
        if self.env_has_program() is False:
            logging.warning(f"需要安装依赖程序{self.get_dependency_program_name()},跳过配置")
        else:
            self.check()
            self.install()
