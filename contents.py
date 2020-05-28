"""
Created on 

@author:
"""


class VendingMachine:
    stock=[]
    def __init__(self, itemID,price,iname,quantity):
        stock = []
        self.itemID = itemID
        self.price = price
        self.iname = iname
        self.quantity = quantity
        VendingMachine.stock.append([itemID, price, quantity, iname])

    

