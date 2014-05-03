"""
Configuration constants
"""
import os
from getpass import getpass

DATA_DIRECTORY = os.path.expanduser('~/src/ear/data')
TMP_DIRECTORY = '/tmp'

def data_path(*args):
    """
    generate a full path under the data directory
    """
    return os.path.join(DATA_DIRECTORY, *args)

def tmp_path(*args):
    """
    generate a full path under the tmp directory
    """
    return os.path.join(TMP_DIRECTORY, *args)

G014B2B_FST = data_path('g014b2b/g014b2b.fst')
DEFAULT_DICT = data_path('dictionary.dic')
DEFAULT_LANG = data_path('languagemodel.lm')
PERSONA_DICT = data_path('persona_dictionary.dic')
PERSONA_LANG = data_path('persona_languagemodel.lm')

PERSONA = 'TEEVEEDEE'

def wit_token():
    token  = os.environ['WIT_ACCESS_TOKEN']
    if not token:
        token = getpass('Wit.ai access token: ')

    return token
