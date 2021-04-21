"""
Factory classes for the creation of concrete isntances of Database.
Each concrete class of Database will implement its own domain specific functions and ideally
use a Command object for a consistent interface.
"""

from .database import Database
from .sqlite import SqliteDatabase


class DatabaseFactory:
    """
    Factory of concrete instances of Database
    database: return a Database instance of the required type, name and path
    """
    @staticmethod
    def database(db_type, db_path) -> Database:
        if db_type == "sqlite":
            return SqliteDatabase(db_path)
        else:
            raise NotImplementedError(f"{db_type} not yet implemented")
