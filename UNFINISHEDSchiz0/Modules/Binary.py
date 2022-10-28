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
me = ['0','1','|', '/', '-']
him = 0, 1
  
def talk_to_him():
    CC()
    # Get strings
    def rand_key(p):
   
      key1 = ""
 
    
      for i in range(p):
      
        temp = str(random.randint(0, 1))
 
        # Concatenation the random 0, 1
        # to the final result
        key1 += temp
         
      return(key1)
  
    # Displayer
    def display():
        CC() 
    print("Press Ctrl+C to exit")
    input("Press Enter to continue...")
    while True:  
      n = 7
      str1 = rand_key(n)
      str2 = rand_key(n)
      str3 = rand_key(n)
      str4 = rand_key(n)
      str5 = rand_key(n)
      str6 = rand_key(n)
      print(Fore.GREEN+ str1 +'  '+ str2 +'  '+ str3 +'  '+ str4 +'  '+ str5 +'  '+ str6 +''+Fore.RESET)
      time.sleep(1)
      

def talk_to_me():
  CC()
    # Get strings
  def rand_key(p):
   
      key1 = ""
 
    
      for i in range(p):
      
        temp = str(random.sample(me, 1))
 
        # Concatenation the random 0, 1
        # to the final result
        key1 += temp
         
      return(key1)
  
    # Displayer
  def display():
      CC() 
  print("Press Ctrl+C to exit...")
  input(Fore.RED+Style.BRIGHT+"Press any key to continue..."+Fore.RESET)
  while True:
    n = 7
    str1 = rand_key(n)
    str2 = rand_key(n)
    str3 = rand_key(n)
    str4 = rand_key(n)
    str5 = rand_key(n)
    str6 = rand_key(n)
    print(Fore.GREEN+ str1 +'  '+ str2 +'  '+ str3 +'  '+ str4 +'  '+ str5 +'  '+ str6 +''+Fore.RESET)
  

  

def menu():
  print("")
CC()
print(Fore.RED+"---------------------------------------------"+Fore.RESET)
print(Fore.YELLOW+Style.BRIGHT+'00110111_\|\\|\//\|'+Fore.RESET)
print(Fore.BLUE+Style.BRIGHT+'''
    |---------------|
    |1. Talk to him|
    |2. Talk to ME|
    |3. Exit|
    |------|
    ''')
menu_opt=input(Fore.RED+Style.BRIGHT+"Enter your choice: "+Fore.RESET)
if menu_opt=='1':
    talk_to_him()
if menu_opt=='2':
    talk_to_me()
if menu_opt=='3':
    quit()