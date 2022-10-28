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

def screen():
    CC()
    print('''
        __________|... . -.-. .-. . - / .--. .-. --- - --- -.-. --- .-..|__________
    1. Journal 
    2. Binary 
    3. Programs
    4. Files
    5. 0ROJ96IT0
    6. X-0_X-0_X-0_X-0_X
    ''')
    scr_opt=input('Enter your option: ')
    if scr_opt== '1':
      from Modules import Journal as Modules_Journal
      Modules_Journal.main()
    if scr_opt== '2':
      from Modules import Binary as Modules_Binary
      Modules_Binary.menu()
    if scr_opt== '3':
      from Modules import Programs as Modules_Programs
      Modules_Programs.menu()
    if scr_opt== '4':
      from Modules import Files as Modules_Files
      Modules_Files.main()
    if scr_opt== '5':
      from Modules import OROJ96IT0ROJ96IT0 as Modules_Misc1
      Modules_Misc1.main()
    if scr_opt== '6':
      from Modules import Misc as Modules_Misc2
      Modules_Misc2.main()
    
RorN=input('Display menu? (y/n): ')
if RorN=='y':
  screen()
else:
  exit()

# End of script
