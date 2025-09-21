import os

from dotenv import load_dotenv

load_dotenv('.env')

SECRET_DATA = os.getenv('SECRET_DATA')

# Caesar cipher static data
OFFSET = int(os.getenv('OFFSET'))
ALFABET_POWER = int(os.getenv('ALFABET_POWER'))

# Permutation cipher static data
PERMUTATION_KEY = list(map(int, os.getenv('PERMUTATION_KEY')))

# Linear cipher secret data
LINEAR_KEY_A = int(os.getenv('LINEAR_KEY_A'))
LINEAR_KEY_B = int(os.getenv('LINEAR_KEY_B'))
