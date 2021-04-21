import json
from pathlib import Path
import tempfile


def load_config(path=None):
    if path is None:
        cf_path = default_cf_path()
        with open(cf_path, 'r') as f:
            return json.load(f)


def dump_config(configuration: dict, cf_path=None):
    if cf_path is None:
        cf_path = default_cf_path()
    try:
        with open(cf_path, 'w') as f:
            json.dump(configuration, f)
    except FileNotFoundError:
        print("Invalid configuration path")


def default_cf_path():
    return Path(tempfile.gettempdir()).with_name('pydo.json')
