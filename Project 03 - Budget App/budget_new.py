
class Category:
    def __init__(self, cat_name):
        self.name = cat_name
        self.ledger = []
    
    def deposit(self, amount, descr = ''):
        self.ledger.append({'amount': amount, 'description': descr})
    
    def withdraw(self, amount, descr = ''):
        if self.check_funds(amount):
            amount = -amount
            self.ledger.append({'amount': amount, 'description': descr})
            return True
        else:
            return False
    def get_balance(self):
        balance = 0
        for n in self.ledger:
            balance += n['amount']
        return balance
    
    def transfer(self, amount, other_cat):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {other_cat.name}')
            other_cat.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False
    
    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        else:
            return False


# outside of Category class
