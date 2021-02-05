# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 19:28:19 2021
@author: JObeng-Berkyaw

SHOPPING LIST APP
"""


# Code refactoring

# Have a SHOW command
def show_list():
    print("Here is your list ")
    for item in Shopping_list:
        #Print out the list
        print(item)
        
def add_to_list(new_item):
       #Add new items to our list
    Shopping_list.append(new_item)
    print("Added {}. list now has {} items".format(new_item, len(Shopping_list)))
    # This shows what was added and the length of the shopping list

#Have a HELP command
def show_help():
    # Print out instruction on how to use app
    print("What should we pick up at the store?")
    print("Enter 'DONE' to stop adding items")
    print("Enter 'SHOW' to show added items")
    print("Enter 'HELP' to help in using the app")

 # Make a list to hold onto our items
Shopping_list = []
    
show_help()
    
while True:
    #ask for new items
    new_item =input(">")
    
    #Be able to quit the app
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue 
    elif new_item == 'SHOW':
        show_list()
        continue
    add_to_list(new_item)

show_list()
