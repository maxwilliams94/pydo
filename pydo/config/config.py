import tempfile
import os
import json


def load_config(path=None):
    if path is None:
        cf_path = default_cf_path()
        try:
            with open(cf_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError


def dump_config(configuration: dict, cf_path=None):
    if cf_path is None:
        cf_path = default_cf_path()
    try:
        with open(cf_path, 'w') as f:
            json.dump(configuration, f)
    except FileNotFoundError as e:
        print("Invalid configuration path")
        exit(1)


def default_cf_path():
    return os.path.join(tempfile.gettempdir(), 'pydo.ini')
