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

def main():
  print("")
CC()
def add(x,y):
    return x + y;
def subtract(x,y):
    return x - y;
def multiply(x,y):
    return x * y;
def divide(x,y):
    return x / y;
def power(x,y):
    return x ** y;
def remainder(x,y):
    return x % y;

while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
    
    choice = input("Enter Choice : ")
    if choice in ('1','2','3','4','5','6','7','8'):
        if choice == '7':
            break
        if choice == '8':
            reset()
        num1 = int(input("Enter First Number = "))
        num2 = int(input("Enter 2nd Number = "))
    
        if choice == '1':
            print(num1, "+", num2, "=", add(num1,num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1,num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1,num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1,num2))
        elif choice == '5':
            print(num1, "^", num2, "=", power(num1,num2))    
        elif choice == '6':
            print(num1, "%", num2, "=", remainder(num1,num2))