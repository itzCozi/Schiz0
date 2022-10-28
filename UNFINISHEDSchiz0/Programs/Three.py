import os
import sys
import random
import datetime
import time
import math
import colorama
from colorama import Fore, Back, Style


# Functions
CC = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
now = datetime.datetime.now()
sym = random.choice(['⊢', '⊤', '⊩', '⋋', '⊕', '⊡', '∐', '⊘', '', '≖', '⊟', '⍕', '⏂', '⏦', '⍲', '⍳', '⌭', '�', '⌜', '⍎', '⍘'])


  
def menu():
    CC()
    print(Fore.RED +'---** -**** ***--/Corrupt File Directory\----* **--- --*** '+ Fore.RESET)
    print("Error: Directory is corrupt... although some files are still intact.\n")
    print("Type help for a list of commands.")
    print('''
    1. 〿〿〿〿
    2. 〩々丁么 丝乷乄上
    3. Man〿c Wr〿tt〿ngs
    4. 侈佹以伈 伌仝 伫了乿
    5. 乗乆亡交
    6. 〿〿〿〿〿〿〿
    ''')
    three_opt=input("|: ")
    if three_opt == 'help':
      print('''
      ------------Command List------------
      1. ls (Type ls then a directoy name to list files)
      2. cd (Type cd then a directoy name to change directory)
      3. sel (Type sel then a file name to select a file)
      4. rm (Type rm then a file name to remove a file)
      5. cp (Type cp then a file name to copy a file)
      Enter to go back to the previous directory...
      ''')
      input("Press enter to continue...")
      menu()
    if three_opt == 'sel 3':
      input("Press enter to open directory...")
      with open('Resources/encryptedmsg.txt', 'r') as f:
        for line in f:
          print(line)
        input("Press enter to continue...")
        menu()
    if three_opt =='cd 3':
      input("Open only file in directory? (y/n) ")
      with open('Resources/encryptedmsg.txt', 'r') as f:
        for line in f:
          print(line)
        input("Press enter to continue...")
        menu()
    if three_opt == '863927':
      print(Fore.GREEN+Style.BRIGHT+"CORRECT")
      print(Fore.GREEN+Style.BRIGHT+"Module Unlocked... ")
      print(Fore.GREEN+Style.BRIGHT+"You can now use the module.")
      input("Press enter to continue..."+Fore.RESET)
      SevenNumberCode()
    else:
      print(Fore.RED+"Invaild use of command, please try again..."+Fore.RESET)
      menu()


def SevenNumberCode():
  CC()
  print('''
  |-------------------|
  |1. Document        |
  |2. Number Sequence |
  |-------------------|
  ''')
  seven_opt=input("|: ")
  if seven_opt == 'sel 1':
    with open('encryptedmsg.txt', 'r') as f:
      for line in f:
        print(line)
        input("Press ene to continue...")
        SevenNumberCode()
  if seven_opt =='sel 2':
    print(Fore.BLUE+Style.BRIGHT+"-----------------------------")
    print(Fore.RED+Style.NORMAL+"|  Enter the 21 digit code  |")
    print(Fore.GREEN+Style.DIM+"-----------------------------"+Fore.RESET+Style.BRIGHT)
    print("")
    print(Fore.BLUE+'XXX-'+Fore.RED+'XXX-'+Fore.GREEN+'XXX-'+Fore.MAGENTA+'XXX-'+Fore.YELLOW+'XXX-'+Fore.LIGHTRED_EX+'XXX-'+Fore.GREEN+'XXX')
    s_ans=input("Code: ")
    if s_ans == '003 023 384 200 459 895 542':
      print(Fore.GREEN+Style.BRIGHT+"CORRECT...")
      print("ACCSESS GRANTED!"+Fore.RESET)
      print("SECRET NUMBER: 397-")
      input("Press enter to leave...")
      quit()
      