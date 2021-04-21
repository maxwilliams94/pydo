import unittest
import os

from pydo.database.database_factory import DatabaseFactory
from pydo.database.database import Database


class TestSQLDataBaseInitialisation(unittest.TestCase):

    def setUp(self) -> None:
        """set up test sql database object"""
        self.database: Database = DatabaseFactory.database('sqlite', "./test_sql.py")
        self.database.initialise()

    def tearDown(self) -> None:
        """remove database (.db) and configuration file"""
        os.remove(self.database.path)
        os.remove(self.database.config_path)

    def test_db_file(self):
        self.assertEqual(self.database.path.exists(), True)

    def test_config_file(self):
        self.assertEqual(self.database.config_path.exists(), True)


if __name__ == '__main__':
    unittest.main()
