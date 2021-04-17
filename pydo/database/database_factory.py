from .database import Database
from .sqlite import SqliteDatabase


class DatabaseFactory:
    @staticmethod
    def database(db_type, db_name, db_path) -> Database:
        if db_type == "sqlite":
            return SqliteDatabase(db_name, db_path)
