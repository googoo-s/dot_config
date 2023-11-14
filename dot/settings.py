import io
import logging

import yaml

import dot.utils as dot_utils


class Settings:
    def __init__(self, settings_file_path):
        self.settings_file_path = settings_file_path
        try:
            dot_utils.check_file(dot_utils.full_path(self.settings_file_path))
        except Exception as ex:
            print("配置文件错误")
            logging.error(ex)
        self._load_config()

    def __getitem__(self, item):
        return self.settings[item]

    def get_settings(self):
        return self.settings.__str__()

    def __str__(self):
        return self.settings.__str__()

    def _load_config(self):
        try:
            with io.open(dot_utils.full_path(self.settings_file_path), "r", encoding="utf-8") as f:
                self.settings = yaml.safe_load(f)
        except Exception as ex:
            logging.error(f"文件不存在,{dot_utils.full_path(self.settings_file_path)}")
            logging.error(ex)


_SETTINGS_FILE_PATH = "settings.yaml"
SETTINGS = Settings(_SETTINGS_FILE_PATH)
