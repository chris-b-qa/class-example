#!/usr/bin/python

class Account:
    num_created = 0

    def __init__(self, initial):
        self._balance = initial
        Account.num_created += 1

    def deposit(self, amt):
        self._balance += amt
        return

    def withdraw(self, amt):
        self._balance -= amt
        return

    def getbalance(self):
        return self._balance
