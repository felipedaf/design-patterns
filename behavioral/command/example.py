"""
Command Design Pattern

Motivation:
 - Ordinary statements are perishable
    Cannot undo member assignment
    Cannot directly serialize a sequence of actions

 - Want an object that represents an operation
    Person should change its age to value 22

 - Uses: GUI commands, multi-level undo/redo, macro reading and more
"""


from abc import ABC, abstractmethod
from enum import Enum


class BankAccount:
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited {amount}, '
              f'balance = {self.balance}')

    def withdraw(self, amount):
        if self.balance - amount >= BankAccount.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f'Withdrew {amount},'
                  f'balance = {self.balance}')

    def __str__(self):
        return f'Balance = {self.balance}'


class Command(ABC):
    @abstractmethod
    def invoke(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class BankAccountCommand(Command):
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, account, action, amount):
        self.invoked = False
        self.amount = amount
        self.account = account
        self.action = action

    def invoke(self):
        if self.action == self.Action.DEPOSIT:
            self.account.deposit(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.account.withdraw(self.amount)

        self.invoked = True

    def undo(self):
        if not self.invoked:
            return

        if self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.account.deposit(self.amount)


if __name__ == "__main__":
    ba = BankAccount()
    cmd = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 100)
    cmd.invoke()
    cmd.undo()
    print(f'After $100 deposit: {ba}')
