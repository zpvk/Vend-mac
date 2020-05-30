# -*- coding: utf-8 -*-
"""
Created on: 29/05/2020

@author: Rohan Kumara
"""
import userFunctions


def login():
    user=input("\n\nPlease enter your \n\t> MIT Employee ID exxx\n\tor \n\t> MIT Student ID sxxx:")
    if 'e' in user:
        menuStaff()
    elif 's' in user:
        menuStudent()
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
    option = input("Your option[E1-E4] : ")
    if option == "E1":
        userFunctions.buy_item('e')
    elif option == "E2":
        userFunctions.add_item()
    elif option == "E3":
        userFunctions.disp()
    elif  option == "E4":
        userFunctions.quit_vm()
        




def menuStudent():

    print("*"*40)
    print("     Employee Vending Machine    ")
    print("*"*40)
    print("S1. Buy")
    print("S2. Display items")
    print("S3. Quit")
    option = input("Your option[S1-S3] : ")
    if option == "S1":
        userFunctions.buy_item('s')
    elif option == "S2":
        userFunctions.disp()
    elif option == "S3":
        userFunctions.quit_vm()
       
        


while (True):
    userFunctions.load_vm()
    userFunctions.disp()
    login()
