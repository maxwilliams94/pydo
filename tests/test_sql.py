import os
from pathlib import PurePath

from pydo.config.config import default_cf_path
from pydo.database.database_factory import DatabaseFactory
from pydo.database.database import Database


class TestSqlInit:

    def test_init_sql(self):
        """
        initialise a new sql database
        """

        db: Database = DatabaseFactory.database(db_type='sqlite',
                                                db_name='test_sql',
                                                db_path='.')
        db.initialise()
        db_full_path = PurePath(os.path.join('.', 'test_sql.db'))
        assert os.path.exists(db_full_path)
        assert db.complete_path == db_full_path
        assert os.path.exists(default_cf_path())

        try:
            os.remove(db_full_path)
            os.remove(default_cf_path())
        except FileNotFoundError:
            pass

    def test_load_invalid_config(self):
        pass

    def test_load_invalid_db(self):
        pass

    def test_config_stored_in_db(self):
        pass
