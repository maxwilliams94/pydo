import os
from pathlib import Path

from abc import abstractmethod, ABC
from ..config.config import default_cf_path


class Database(ABC):
    """
    Abstract Database class for managing access to and from the chosen database
    Supports initialisation of a new database file,
    loading,saving and closing of the current database
    Saving of configuration to itself, a temporary json (session) and
    its representation as a dictionary.
    """
    def __init__(self, path, config_path=None):
        """
        Generic Database initialisation
        :param db_path: path to database file
        :param config_path: path to temporary (session) configuration file
        """
        self._db_path = Path(path)
        self._config_path: Path = default_cf_path() if config_path is None else Path(config_path)

    @property
    def path(self):
        return self._db_path

    @property
    def config_path(self):
        return self._config_path

    @abstractmethod
    def initialise(self):
        pass

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def dump_config(self):
        pass

    @abstractmethod
    def to_dict(self):
        pass

    @abstractmethod
    def commit_config(self):
        pass
