from .database import Database
import sqlite3
from os import path
from ..config.config import dump_config


class SqliteDatabase(Database):
    db_ext = '.db'

    def __init__(self, name, db_path, config_path=None):
        super().__init__(name, db_path, config_path)
        self.cursor = None
        self.connection = None

        if self.name.endswith(SqliteDatabase.db_ext):
            self.complete_path = path.join(self.path, self.name)
        else:
            self.complete_path = path.join(self.path,
                                           self.name + SqliteDatabase.db_ext)

    def initialise(self):
        self.load()  # Connecting to non-existent db file creates a new db file
        self.cursor.execute("""CREATE TABLE tasks (
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
        self.connection = sqlite3.connect(self.complete_path)
        self.cursor = self.connection.cursor()

    def save(self):
        self.connection.commit()

    def close(self):
        self.connection.close()

    def dump_config(self):
        dump_config(self.to_dict(), self.config_path)

    def to_dict(self):
        return {"db_name": self.name,
                "db_path": self.path}

    def commit_config(self):
        pass
