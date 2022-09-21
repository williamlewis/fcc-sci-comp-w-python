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

    # get sum of all WITHDRAWALS  by category(check for negative values only)
    spend_percentages = []
    for cat in categories:
        cat_spend = 0
        ledger = Category(cat).ledger
        for item in ledger:
            if item['amount'] < 0:
                cat_spend += item['amount']
        cat_spend *= -1
        spend_percentages.append([cat.name, cat_spend])
    
    # establish overall spend to calculate percentages
    overall_spend = 0
    for n in spend_percentages:
        overall_spend += n[1]

    # calculate rounded down percentage for each category
    for n in spend_percentages:
        cat_spend = n[1]
        cat_perc = cat_spend / overall_spend
        cat_perc_rounded = (math.floor(cat_perc * 10)) * 10
        n.append(cat_perc_rounded) # [cat_name, cat_spend, cat_perc_rounded]

    # build primary chart components including vertical bars of 'o'
    row_val = 100
    chart_title = 'Percentage spent by category\n'
    chart_graph = ''
    for i in range(0, 11):
        row_label = (' ' * (3 - len(str(row_val)))) + str(row_val) + '|' # 3 or 6 spaces where number is shorter?
        
        row_bars = ''
        for cat in spend_percentages:
            if cat[2] >= row_val:
                row_bars += ' o '
            else:
                row_bars += '   '
        
        full_graph_row = row_label + row_bars + ' \n'
        chart_graph += full_graph_row
        
        row_val -= 10

    chart_base = '    ' + ('-' * len(categories) * 3) + '-\n'


    # build labels at base of chart by pivoting category names to be vertical
    chart_labels = ''

    max_name_len = 0
    for cat in spend_percentages:
        name = cat[0]
        if len(name) > max_name_len:
            max_name_len = len(name)
    
    letter_i = 0

    for i in range(0, max_name_len):
        pivot_letters = ''
        for cat in spend_percentages:
            name = cat[0]
            if len(name) > letter_i:
                pivot_letters += ' ' + name[letter_i] + ' '
            else:
                pivot_letters += '   '
        
        full_label_row = '    ' + pivot_letters + ' \n'
        chart_labels += full_label_row
        letter_i += 1
    
    chart_labels = chart_labels[:-2] + ' ' # remove final line break and match end spaces


    # combine all chart components to return as single variable
    output = chart_title + chart_graph + chart_base + chart_labels
    return output



























        # spend_percentages.append([n, cat_perc_rounded, cat_perc])
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
    

