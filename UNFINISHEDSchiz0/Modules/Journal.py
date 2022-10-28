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

CC()
def main():
# create a function to write a new entry
  def new_entry():
    # get the current date
    date = datetime.datetime.now()
    # get the current date in a string format
    date_string = date.strftime("%d/%m/%Y")
    # get the current time in a string format
    time_string = date.strftime("%H:%M:%S")
    # get the title of the entry
    title = input("Enter the title of the entry: ")
    # get the entry
    entry = input("Enter your entry: ")
    # create a new file with the title of the entry
    file = open(title + ".txt", "w")
    # write the date and time to the file
    file.write(date_string + " " + time_string + "\n")
    # write the entry to the file
    file.write(entry)
    # close the file
    file.close()

# create a function to view an entry
  def view_entry():
    # get the title of the entry
    title = input("Enter the title of the entry: ")
    # open the file
    file = open(title + ".txt", "r")
    # read the file
    print(file.read())
    # close the file
    file.close()

# create a function to view all entries
  def view_all_entries():
    # get the current date
    date = datetime.datetime.now()
    # get the current date in a string format
    date_string = date.strftime("%d/%m/%Y")
    # get the current time in a string format
    time_string = date.strftime("%H:%M:%S")
    # create a new file with the title of the entry
    file = open("all_entries.txt", "w")
    # write the date and time to the file
    file.write(date_string + " " + time_string + "\n")
    # close the file
    file.close()
    # open the file
    file = open("all_entries.txt", "a")
    # get the number of entries
    number_of_entries = int(input("Enter the number of entries: "))
    # loop through the number of entries
    for i in range(number_of_entries):
        # get the title of the entry
        title = input("Enter the title of the entry: ")
        # open the file
        entry_file = open(title + ".txt", "r")
        # read the file
        file.write(entry_file.read())
        # close the file
        entry_file.close()
    # close the file
    file.close()

# create a function to delete an entry
  def delete_entry():
    # get the title of the entry
    title = input("Enter the title of the entry: ")
    # open the file
    file = open(title + ".txt", "w")
    # close the file
    file.close()

# create a function to delete all entries
  def delete_all_entries():
    # get the number of entries
    number_of_entries = int(input("Enter the number of entries: "))
    # loop through the number of entries
    for i in range(number_of_entries):
        # get the title of the entry
        title = input("Enter the title of the entry: ")
        # open the file
        file = open(title + ".txt", "w")
        # close the file
        file.close()

# create a function to edit an entry
  def edit_entry():
    # get the title of the entry
    title = input("Enter the title of the entry: ")
    # open the file
    file = open(title + ".txt", "w")
    # get the entry
    entry = input("Enter your entry: ")
    # write the entry to the file
    file.write(entry)
    # close the file
    file.close()

# create a function to edit all entries
  def edit_all_entries():
    # get the number of entries
    number_of_entries = int(input("Enter the number of entries: "))
    # loop through the number of entries
    for i in range(number_of_entries):
        # get the title of the entry
        title = input("Enter the title of the entry: ")
        # open the file
        file = open(title + ".txt", "w")
        # get the entry
        entry = input("Enter your entry: ")
        # write the entry to the file
        file.write(entry)
        # close the file
        file.close()

# create a function to search for an entry
  def search_entry():
    # get the title of the entry
    title = input("Enter the title of the entry: ")
    # open the file
    file = open(title + ".txt", "r")
    # read the file
    print(file.read())
    # close the file
    file.close()

# create a function to search for all entries
  def search_all_entries():
    # get the number of entries
    number_of_entries = int(input("Enter the number of entries: "))
    # loop through the number of entries
    for i in range(number_of_entries):
        # get the title of the entry
        title = input("Enter the title of the entry: ")
        # open the file
        file = open(title + ".txt", "r")
        # read the file
        print(file.read())
        # close the file
        file.close()

# create a function to exit the program
  def exit_program():
    # exit the program
    exit()

# create a function to display the menu
  def display_menu():
    # display the menu
    print(Fore.RED+"Journal")
    print(Fore.BLUE+"---------------------")
    print(Fore.RED+"1. New Entry")
    print(Fore.BLUE+"2. View Entry")
    print(Fore.RED+"3. View All Entries")
    print(Fore.BLUE+"4. Delete Entry")
    print(Fore.RED+"5. Delete All Entries")
    print(Fore.BLUE+"6. Edit Entry")
    print(Fore.RED+"7. Edit All Entries")
    print(Fore.BLUE+"8. Search Entry")
    print(Fore.RED+"9. Search All Entries")
    print(Fore.BLUE+"10. Exit")

# create a function to get the user's choice
  def get_choice():
    # get the user's choice
    choice = int(input(Fore.RED+"Enter your choice: ")+Fore.GREEN)
    # return the user's choice
    return choice

# create a function to run the program
  def run_program():
    # display the menu
    display_menu()
    # get the user's choice
    choice = get_choice()
    # create a dictionary of functions
    functions = {1: new_entry, 2: view_entry, 3: view_all_entries, 4: delete_entry, 5: delete_all_entries, 6: edit_entry, 7: edit_all_entries, 8: search_entry, 9: search_all_entries, 10: exit_program}
    # run the function
    functions[choice]()

# run the program
  run_program()