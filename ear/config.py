"""
Configuration constants
"""
import os

DATA_DIRECTORY = os.path.expanduser('~/src/ear/data')
def data_path(*args):
    """
    generate a full path under the data directory
    """
    return os.path.join(DATA_DIRECTORY, *args)

G014B2B_FST = data_path('g014b2b/g014b2b.fst')
