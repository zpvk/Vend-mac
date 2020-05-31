"""
Created on: 29/05/2020
@author: Rohan Kumara
"""


class VendingMachine:
    items = {}
    stock= items.keys()
    def __init__(self, itemID,price,iname,quantity):
        items = VendingMachine.items
        self.itemID = itemID
        self.price = price
        self.iname = iname
        self.quantity = quantity
        items[self.itemID]=[self.price,self.iname,self.quantity]
 
    def description(self):
        return "Item:{} Price:{} Quantity:{} Item Name:{}".format(self.itemID,self.price,self.quantity,self.iname)
