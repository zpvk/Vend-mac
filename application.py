# -*- coding: utf-8 -*-
"""
Created on:

@author: 
"""
import userFunctions


def login():
    user=input("\n\nPlease enter your \n\t> MIT Employee ID exxx\n\tor \n\t> MIT Student ID sxxx:")
    if 'e' in user:
        application.menuStaff()
    elif 's' in user:
        application.menuStudent()
    else:
        print("Enter valid input again")

def menuStaff():

    print("*"*40)
    print("     Employee Vending Machine    ")
    print("*"*40)
    print("E1. Buy")    
    print("E2. Add")
    print("E3. Display items")
    print("E4. Quit")
    
print(application.menuStaff())