import os
import sys
import random
import datetime
import time
import colorama
from colorama import Fore, Back, Style

# Functions
CC = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
now = datetime.datetime.now()