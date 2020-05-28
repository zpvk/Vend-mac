# -*- coding: utf-8 -*-
"""
Created on:

@author: 
"""
from userFunctions import userFunction


class application(userFunction):
    def __init__(self, itemID, price, iname, quantity):
        super().__init__(itemID, price, iname, quantity)
        

    def login(self):
        user=input("\n\nPlease enter your \n\t> MIT Employee ID exxx\n\tor \n\t> MIT Student ID sxxx:")
        print("Hello - {}\n\nWelcome to MIT Vending Machine".format(user))
        if 'e' in user:
            while(True):
                application.menuStaff()
                userFunction.disp(userFunction)
        elif 's' in user:
            while(True):
                application.manuStudent()
                userFunction.disp(userFunction)
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
        choice = int(input("Your option[E1-E4] : "))
        if choice == 1:
            application.buy_item()
        elif choice == 2:
            application.add()
        elif choice == 3:
            application.view()
        elif choice == 4:
            application.quit_vm()
        else:
            print("Invalid Input")
    
    def manuStudent():
        print("*"*40)
        print("     Student Vending Machine    ")
        print("*"*40)
        print("E1. Buy")
        print("E2. Display items")
        print("E3. Quit")
        choice = int(input("Your option[E1-E4] : "))
        if choice == 1:
            print("Contents of VM")
            print("-"*40)
            application.buy_item()
        elif choice == 3:
            application.view()
        elif choice == 4:
            print("Contents of VM")
            print("-"*40)
            application.quit_vm() 
        else:
            print("Invalid Input")





VM01 = application("A3",20,"coc",10)
VM01.load_vm()
VM01.disp()
VM01.login()
