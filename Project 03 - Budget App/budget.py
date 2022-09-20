
class Category:
    def __init__(self, cat_name):
        self.name = cat_name
        self.ledger = []
    
    # create required methods
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
    
    # customize output when object is printed
    def __str__(self):

        print_list = []

        row_width = 30
        asterisk_flank = '*' * int(((row_width - len(self.name)) / 2))
        title_row = asterisk_flank + self.name + asterisk_flank
        print_list.append(title_row)

        descr_width = 23
        amount_width = 7
        for n in self.ledger:
            ledger_index = self.ledger.index(n)
            descr_leftover = ' ' * (descr_width - len(self.ledger[ledger_index]['description']))
            amount_leftover = ' ' * (amount_width - len(str(float(self.ledger[ledger_index]['amount']))))
            ledger_row = self.ledger[ledger_index]['description'][:23] + descr_leftover + amount_leftover + str(float(self.ledger[ledger_index]['amount']))
            print_list.append(ledger_row)

        total_row = 'Total: ' + str(float(self.get_balance()))
        print_list.append(total_row)

        #output = for n in print_list: print(n)
        #output = print([row for row in print_list])
        output = [row for row in print_list]

        return output


# outside of Category class
