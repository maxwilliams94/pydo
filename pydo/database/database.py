from abc import abstractmethod, ABC
from ..config.config import default_cf_path


class Database(ABC):
    def __init__(self, name, path, config_path=None):
        self.name = name
        self.path = path
        self.connection = None
        self.complete_path = None
        self.config_path = default_cf_path() if config_path is None else config_path

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
