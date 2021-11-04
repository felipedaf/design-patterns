"""
Memento Design Pattern

Motivation:
 - An object system goes through changes

 - There are different ways of navigating those changes

 - One way is to record every change and teach a command to undo itself

 - Another is to simply save snapshots of the system
"""


class Memento:
    def __init__(self, balance) -> None:
        self.balance = balance


class BankAccount:
    def __init__(self, balance=0) -> None:
        self.balance = balance
        self.changes = [Memento(self.balance)]
        self.current = 0

    def deposit(self, amount):
        self.balance += amount
        m = Memento(self.balance)
        self.changes.append(m)
        self.current += 1
        return m

    def restore(self, memento):
        if memento:
            self.balance = memento.balance
            self.changes.append(memento)
            self.current = len(self.chages) - 1

    def undo(self):
        if self.current > 0:
            self.current -= 1
            m = self.changes[self.current]
            self.balance = m.balance
            return m

        return None

    def redo(self):
        if len(self.changes) > self.current + 1:
            self.current += 1
            m = self.changes[self.current]
            self.balance = m.balance
            return m

    def __str__(self) -> str:
        return f"Balanace = {self.balance}"


if __name__ == '__main__':
    ba = BankAccount(100)
    m1 = ba.deposit(50)
    m2 = ba.deposit(25)
    print(ba)

    ba.undo()
    print(f'Undo 1: {ba}')
    ba.undo()
    print(f'Undo 2: {ba}')
    ba.redo()
    print(f'Undo 3: {ba}')
