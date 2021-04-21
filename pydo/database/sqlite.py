import sqlite3
from pathlib import Path
from .database import Database
from ..config.config import dump_config


class SqliteDatabase(Database):
    """
    SQL Database
    """

    def __init__(self, db_path, config_path=None):
        super().__init__(db_path, config_path)
        self._cursor = None
        self._connection = None

    def initialise(self):
        """
        Initialise a new sql database at self.db_path and save configuration within itself
        The configuration for the session is also dumped to a temporary json file
        :return: None
        """
        self.load()  # Connecting to non-existent db file creates a new db file
        self._cursor.execute("""CREATE TABLE tasks (
        id TEXT PRIMARY_KEY,
        name TEXT,
        description TEXT,
        due DATETIME
        );""")

        self.save()
        self.close()
        self.dump_config()
        self.commit_config()

    def load(self):
        """Load self.complete_path"""
        self._connection = sqlite3.connect(self._db_path)
        self._cursor = self._connection.cursor()

    def save(self):
        """save the database to file"""
        self._connection.commit()

    def close(self):
        """sever connection to database and reset"""
        self._connection.close()
        self._connection = None
        self._cursor = None

    def dump_config(self):
        """save configuration to temporary json file"""
        dump_config(self.to_dict(), self._config_path)

    def to_dict(self):
        """dictionary representation of database configuration"""
        return {"db_name": self.path.name,
                "db_path": str(self.path.resolve()),
                "config_path": str(self.config_path)}

    def commit_config(self):
        """save database configuration to itself"""
        pass
