from flask_ini import FlaskIni
from configparser import NoSectionError, NoOptionError

class Config(FlaskIni):

    def _setting(self, section, key, default=None):
        try:
            return self.get(section, key)
        except (NoSectionError, NoOptionError):
            return default

    def _log_setting(self, key, default=None):
        return self._setting("log", key, default)

    @property
    def log_level(self):
        return self._log_setting("level", "INFO")

    @property
    def log_format(self):
        return self._log_setting("format")

    @property
    def log_datefmt(self):
        return self._log_setting("datefmt")

    @property
    def log_path(self):
        return self._log_setting("path")
