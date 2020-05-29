# -*- coding: utf-8 -*-
"""
Created on 

@author:
"""
import time
from threading import Thread
from contents import VendingMachine


class userFunction(VendingMachine):
    total = 0
    items = VendingMachine.stock
    def load_vm(self): #LETS PUT SOME DEFAULT ITEMS IN THE VENDING MACHINE
        VM1 = VendingMachine(["A1", 10, "Water", 2])
        VM2 = VendingMachine(["A2", 20, "Chips", 4])

    def disp():
        items = userFunction.items
        print("\tContents of VM")
        print("-"*40)
        print("\n\nItems in VM (Total : {})\n".format(len(items)))
        print("NO#\tItem ID \tPrice\tQuantity\tItem Name")
        
        for i in range(len(items)):
            print(f"{i+1}.\t{items[i][0]}\t\t ${items[i][1]}\t{items[i][3]}\t\t{items[i][2]}")

    def add():
        items = userFunction.items
        itemID = input("Enter Item ID : ")
        price = input("price : $ ")
        iname = input("Item Name : ")
        quantity = int(input("How many Items are you adding?"))
        if userFunction.search(itemID):
            ind = items.index(itemID)
            items[ind][1] = price
            items[ind][2] = iname
            items[ind][3] = items[ind][3] + quantity
        else:
            items.append([itemID, price,iname, quantity])
        print("-"*40)
        print("Item added: {}".format(itemID))

    def buy_item():
        items= userFunction.items
        print("       Purchase Item")
        print("-"*40)
        item = input("Enter item ID: ")
        if userFunction.search(item) == True:
            s_i = items.index(item)
            print(f"\nItem Slot: {item}\nItem Sell price: ${items[s_i][1]}")
            print(f"Please Pay : ${items[s_i][1]}")
            items[s_i][2] = items[s_i][2] - 1
            total = items[s_i][1]
        else:
            print("Invalid input")
        
        

            
    def calculate(price):
        print("Please pay : $ ",price)
        amount = int(input())
        print(f"You Balance is : {amount-price}")
        print("Transaction Complete ....")

    
    def search(itemId):
        items = userFunction.items          
        if itemId in items:
            return True
        else:
            return False

    def quit_vm():
        print("Terminating ... ")
        quit_vm = False
    
    def timeout(self,Answer):
        time.sleep(2)
        if Answer != None:
            return
        print ("Too Slow")
    

