import os
import sys

def run_program():
    pass

def display_menu():
    print("What would you like to do? ")
    choice = input("""Chose one of the following: \n
    N -> Make a new entry \n
    S -> Search for an entry \n
    Q -> Quit""").lower().strip()
    if choice == 's':
        search_for_entry()
    elif choice == 'q':
        sys.exit()
    else:
        new_entry()

def new_entry():
    '''Make a new entry in the CSV file. New entry must include
    [Name], [Minutes Spent], [Date], and [Notes]'''

def search_for_entry():
    '''Display menu with options for searching for an entry these
    options include searching by [Date], [Time Spent], [Exact Search]
    and [Regex Pattern]'''

def search_by_date():
    '''Allows user to search for tasks by a date'''

def search_by_time_spent():
    '''Allows user to search for tasks by number of minutes spent on
    task'''

def search_exact():
    '''Allows user to search by the exact name of the task'''

def search_by_pattern():
    '''Allows user to provide a RegEx pattern to search for tasks'''

def display_entry():
    '''Displays one entry'''

def display_entries():
    '''Used for returning search results. Can be paged through. Also
    provides options to editing an entry, deleting an entry, and returning
    to the main menu'''

def delete_entry(entry):
    '''Removes a specified entry from the CSV file'''

def edit_entry(entry):
    '''Allows user to change any field of a passed in entry'''



if __name__ = "__main__":
    run_program()
