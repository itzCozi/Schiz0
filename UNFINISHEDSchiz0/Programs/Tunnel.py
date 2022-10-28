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
num = random.randint(1, 10000)


CC()
def menu():
  print("-_-_-_-_-_-_-_-_-_-_-_-_-_-/ RAT  Tunnel \-_-_-_-_-_-_-_-_-_-_-_-_-_-")
  print('''
  1. Go Under.
  2. Go Back. 
  ''')
  Tun_opt=input("\n\nSelect an option: ")
  if Tun_opt=='1':
    CC()
    print("|-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-|")
    print("|Into the tunnel...                                   |")
    print("|Menu                                                 |")
    print("|1. Buying                                            |")
    print("|2. Selling                                           |")
    INTUN_opt=input("|Your choice(1,2):                                    |")
    if INTUN_opt=='1':
      CC()
      Buying()
    if INTUN_opt=='2':
      CC()
      Selling()
    else:
      CC()
      print("|Invalid option!                                      |")
      menu()

def Buying():
  CC()
  print("|-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-|")
  print("|Buying:                                              |")
  print("|--------                                             |")
  print("|1. Buy Drugs                                         |")
  print("|2. Buy Guns                                          |")
  BUY_opt=input("|Your choice(1,2):                                    |")
  if BUY_opt=='1':
    CC()
    Buy_Drugs()
  if BUY_opt=='2':
    CC()
    Buy_Guns()
  else:
    CC()
    print("|Invalid option!                                       |")
    menu()

def Buy_Drugs():
  CC()
  print("|-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-|")
  print("|Buy Drugs:                                           |")
  print("|----------                                           |")
  print("|1. Meth                                              |")
  print("|2. Weed                                              |")
  print("|3. Molly                                             |")
  print("|4. LSD                                               |")
  print("|5. Psilocybin Mushrooms                              |")
  Buy_opt=input("|Your choice(1-5):                                  |")
  if Buy_opt=='1' or '2' or '3' or '4' or '5':
    input("|How much:                                        |")
    print("|Done!                                               |")
    input("|Press any key to continue...                   |")
    quit()
    
def Sell_Drugs():
  CC()
  print("|-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-|")
  print("|Sell Drugs:                                          |")
  print("|------------                                         |")
  print("|1. Meth                                              |")
  print("|2. Weed                                              |")
  print("|3. Molly                                             |")
  print("|4. LSD                                               |")
  print("|5. Psilocybin Mushrooms                              |")
  Sell_opt=input("|Your choice(1-5):                                 |")
  if Sell_opt=='1' or '2' or '3' or '4' or '5':
    input("|How much:                                          |")
    print("|Done!                                              |")
    print(num+"Dollars Made!                                   |")
    input("|Press any key to continue...                       |")
    quit()
          
def Selling():
  CC()
  print("|-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-|")
  print("|Selling:                                             |")
  print("|---------                                            |")
  print("|1. Sell Drugs                                        |")
  print("|2. Sell Guns                                         |")
  SELL_opt=input("|Your choice(1,2):                                  |")
  if SELL_opt=='1':
    CC()
    Sell_Drugs()
  if SELL_opt=='2':
    CC()
    Sell_Guns()
  else:
    CC()
    print("|Invalid option!                                       |")
    menu()

def Buy_Guns():
  print("|-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-|")
  print("|Buy Guns:                                            |")
  print("|----------                                           |")
  print("|1. AR15                                              |")
  print("|2. Colt1911                                          |")
  print("|3. RPG                                               |")
  Bg_opt=input("Your choice(1,3) ")
  if Bg_opt =='1' or '2' or '3':
    CC()
    print("Purchase Complete")
    input("Any key to leave")
    quit()
    