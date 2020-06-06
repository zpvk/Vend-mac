# -*- coding: utf-8 -*-
"""
Created on: 29/05/2020
@author: Rohan Kumara
"""
import threading
import contents

items=[]
def load_vm(): #LETS PUT SOME DEFAULT ITEMS IN THE VENDING MACHINE
    vm1=contents.VendingMachine("A1",10,"Water",2)
    items.append(vm1)  
    vm2=contents.VendingMachine("A2",20,"Chips",4)
    items.append(vm2)

    
def add_item():   
    print("       ADD Item")
    itemID = input("Emter itemID: ")
    ind = search(itemID)
    if ind == None:
        price = int(input("Price: $"))
        iname = input("Enter item Name: ")
        quantity = int(input('How many items are you adding? '))
        items.append(contents.VendingMachine(itemID, price, iname, quantity))
    else:

        ind[0] = int(input("Price: $"))
        ind[1] = input("Enter item Name: ")
        i = int(input('How many items are you adding? '))
        ind[2] = ind[2]+i

     
def buy_item(s):
    total = 0
    print("       Purchase Item")  
    ###
    itemId = input("Enter item ID:")
    ind = search(itemId)
    if ind[2]==0:
        print(f"\nEmpty Item Slot: {itemId}")
    else:
        print(f"\nItem Slot: {itemId}")
        print(f"price:{ind[0]}")
        ind[2] = ind[2]-1
        total = ind[0]
        timer = threading.Timer(5.0,calculate(s,total))
        timer.cancel()


def calculate(s,total):
    if s == 's':
        Ntotal = total-((total/100)*20)
    else:
        Ntotal = total
    print("Please pay : $ ", Ntotal)
    paid = int(input(""))
    if paid == Ntotal:
        print("Successful")
    else:
        change = paid-Ntotal
        print(f"Your change is: {change}")

        
def disp():
    print("\tContents of VM")
    print("-"*40)
    print("\n\nItems in VM (Total : {})\n".format(len(items)))
    print("NO#\tItem ID \tPrice\tItem Name\tQuantity")
    k_list = list(contents.VendingMachine.items.keys())
    for i in range(len(k_list)):
        id = search(k_list[i])
        print(f"{i+1}.\t{k_list[i]}\t\t ${id[0]}\t{id[1]}\t\t{id[2]}")


    
    
def quit_vm():
     print() 
     print("Terminating ... \n\n")

def search(itemID):
    dict = contents.VendingMachine.items
    for i in items:
        if(i.itemID==itemID):
            return dict.get(itemID)


def getList(dict):
    list = []
    for key in dict.keys():
        list.append(key)

    return list

