"""
Command-line interface functionality
"""
import argparse


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="pydo", description="pydo command line todo management")

    initialisation = parser.add_argument_group(title="initialisation")
    # I/O
    initialisation.add_argument("-d", "--database", help="database to load", dest="database")
    initialisation.add_argument("--init", help="Initialise a new database of type")
    initialisation.add_argument("--path", "-p", help="path to database")

    # Task Management

    return parser.parse_args()
