
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

        print_list = ''

        row_width = 30
        asterisk_flank = '*' * int(((row_width - len(self.name)) / 2))
        title_row = asterisk_flank + self.name + asterisk_flank + '\n'
        print_list += title_row

        descr_width = 23
        amount_width = 7
        for n in self.ledger:
            i = self.ledger.index(n)
            row_descr = self.ledger[i]['description'][:23]
            # row_amount = str(round(float(self.ledger[i]['amount']), 2))
            row_amount = format(self.ledger[i]['amount'], '.2f')

            # max_descr = self.ledger[i]['description'][:23]
            # descr_leftover = ' ' * (descr_width - len(max_descr))
            descr_leftover = ' ' * (descr_width - len(row_descr))

            # amount_leftover = ' ' * (amount_width - len(str(float(self.ledger[i]['amount']))))
            # ledger_row = self.ledger[i]['description'][:23] + descr_leftover + amount_leftover + str(float(self.ledger[i]['amount'])) + '\n'
            # amount_leftover = ' ' * (amount_width - len(str(round(float(self.ledger[i]['amount'])), 2)))
            # ledger_row = self.ledger[i]['description'][:23] + descr_leftover + amount_leftover + str(round(float(self.ledger[i]['amount']), 2)) + '\n'
            
            amount_leftover = ' ' * (amount_width - len(row_amount))
            # ledger_row = self.ledger[i]['description'][:23] + descr_leftover + amount_leftover + str(round(float(self.ledger[i]['amount']), 2)) + '\n'
            ledger_row = row_descr + descr_leftover + amount_leftover + row_amount + '\n'
            
            print_list += ledger_row

        total_row = 'Total: ' + str(float(self.get_balance()))
        print_list += total_row

        output = print_list

        return output


# outside of Category class
