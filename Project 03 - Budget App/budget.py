import math

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
    
    # format output when object is printed
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
            row_amount = format(self.ledger[i]['amount'], '.2f')

            descr_leftover = ' ' * (descr_width - len(row_descr))
            amount_leftover = ' ' * (amount_width - len(row_amount))

            ledger_row = row_descr + descr_leftover + amount_leftover + row_amount + '\n'            
            print_list += ledger_row

        total_row = 'Total: ' + str(float(self.get_balance()))
        print_list += total_row

        output = print_list

        return output


# build a simple bar chart to display categories by their percentage of overall spend (categories received as list argument)
test_input = ['Clothing', 'Food', 'Auto']
test_spending = {'Clothing': .2, 'Food': .6, 'Auto': .1}


def create_spend_chart(categories):
    categories = test_input

    # check for 4 values max in argument
    if len(categories) > 4:
        categories = categories[:4]
        print('Up to four categories allowed for bar chart; additional will not plot.')

    # establish overall spend to calculate percentages
    overall_spend = 0
    for n in categories:
        overall_spend += n.get_balance()
    
    # get balance & calculate rounded down percentage for each category
    spend_percentages = []
    for n in categories:
        cat_spend = n.get_balance()
        cat_perc = (cat_spend / overall_spend)
        cat_perc_rounded = (math.floor(cat_perc * 10)) * 10 # make a float, then round down with math.floor(), then multiply by ten
        spend_percentages.append([n, cat_perc_rounded, cat_perc])
        # include cat_perc unrounded value to reference in case total sum of percentages does not equal 100?
    
    # # check that rounded category percentages total up to 100; if not, add 10 to highest raw value & repeat if needed
    # sum_percentages = 0
    # for n in spend_percentages:
    #     sum_percentages += n[1]
    # if sum_percentages > 100:
    #     # for each cat, get diff between rounded & unrounded values (save into spend_percentages list as fourth item)
    #     # make copy list & sort by rounded-unrounded difference values
    #     delta = 100 - sum_percentages
    #     num_corrections = delta / 10
    #     for i in range(0, num_corrections):
    #         # get category name from sorted copy list
    #         # use category name to access sublist in main spend percentages list, cat_perc_rounded value item
    #         # add 10 to cat_perc_rounded value item (directly in main spend_percengtages list; overwrite)
    
