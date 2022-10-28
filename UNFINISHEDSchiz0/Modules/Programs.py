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

def menu():
  CC()
  print(Style.BRIGHT + Fore.RED +'''
    ---------------|Programs|---------------
    1. Minesweeper |
    2. Calculator |
    3. �☒��☒���☒ |
    4. Tunnel.EXE  |
    5. Exit |
    -------------------------------
    ''')
  menu_opt = input('Enter your choice: ')
  if menu_opt == '1':
      from Programs import Minesweeper as Programs_Minesweeper
      Programs_Minesweeper.main()
  if menu_opt == '2':
      from Programs import Calculator as Programs_Calculator
      Programs_Calculator.main()
  if menu_opt == '3':
      from Programs import Three as Programs_Three
      Programs_Three.menu()
  if menu_opt == '4':
      from Programs import Tunnel as Programs_Tunnel
      Programs_Tunnel.menu()
  if menu_opt == '5':
      CC()
      input("Are you sure? (y/n) ")
      input("Are you sure? (y/n) ")
      input("Do you want to exit? (y/n) ")
      input("Say I want to exit (I want to exit) ")
      print("No.")
      input("Find a way out (Enter)")
      menu()
  else:
      CC()
      print(Style.BRIGHT + Fore.RED + 'Invalid choice!')
      menu()

