# -*- coding: utf-8 -*-
"""
Created on: 29/05/2020

@author: Rohan Kumara
"""


class VendingMachine:
    stock=[]
    def __init__(self, itemID,price,iname,quantity):
        stock = []
        self.itemID = itemID
        self.price = price
        self.iname = iname
        self.quantity = quantity
        stock=stock.append([itemID, price, quantity, iname])

    

