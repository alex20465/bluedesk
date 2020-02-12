from os import getenv, makedirs
from os.path import realpath, join, exists, dirname
import configparser


class Config:

    FILENAME = 'bluedesk.conf'

    def __init__(self):
        self._config = configparser.ConfigParser()

        self._config['default'] = {
            "addr": ""
        }

        if exists(self.directory) is False:
            makedirs(self.directory)
        elif exists(self.filepath) is True:
            self._config.read(self.filepath)

    @property
    def directory(self):
        return realpath(join(getenv("HOME"), '.config'))

    @property
    def filepath(self):
        return join(self.directory, self.FILENAME)

    def set(self, name, value, section="default"):
        self._config[section][name] = value
        self.__save()
        return value

    def get(self, name, section="default"):
        return self._config[section].get(name, None)

    def has(self, name, section="default"):
        value = self.get(name, section).strip()

        if not value or value == "":
            return False
        else:
            return True

    def __save(self):
        with open(self.filepath, 'w') as configfile:
            self._config.write(configfile)

