'''
- create a class for Category
- instantiate instances based on category
- ledger variable (instance-based)
- methods:
    - deposit
    - withdraw
    - get_balance
    - transfer
    - check_funds
- format printed output
    - 30-char title line, centered category
    - item list, 23-char max
    - item amount, right-aligned, 2 decimals, 7-char max
    - bottom line showing total
- function outside class to print as a % bar chart
'''


class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.balance = 0
    
    def deposit(self, amount, description=''):
        # takes an amount & a description
        # default to empty string if no description is given
        # append an object ot the ledger list as {'amount': amount, 'description': description}
        self.category.ledger.append({'amount': amount, 'description': description})
    
    def withdraw(self, amount, description=''):
        # convert passed amount to a negative value
        # check if enough funds are in balance; if not, don't add transaction to the ledger
        # return True if withdrawal transaction occurred, or False if it didn't occur
        if self.check_funds(amount) is True:
            amount *= -1
            self.balance += amount
            self.category.ledger.append({'amount': amount, 'description': description})
            return True
        else:
            return False
    
    def get_balance(self):
        # return the current balance of a budget category based on deposits & withdrawals (pull these based on the categories that were passed in when instantiating the objects)
        # i.e. filter down to budget of the particular category
        print(self.balance)

    def transfer(self, amount, destination_category):
        # accept an amount & another budget category
        # create a withdrawal w/ the amount & description 'Transfer to [destination category]'
        # then deposit that amount into the destination category w/ description 'Tranfer from [source category]'
        # check if enough funds to make transfer; if not, add nothing to ledger
        # return True if tranfer transaction occurred, False if not
        if self.check_funds(amount) is True:
            withdraw_descrip = 'Transfer to ' + str(destination_category)
            self.withdraw(amount, withdraw_descrip)
            deposit_descrip = 'Transfer from ' + str(self.category)
            self.deposit(amount, deposit_descrip)
            return True
        else:
            return False

    
    def check_funds(self, amount):
        # accept an amount
        # return False if passed amount is greater than balance in the budget category, otherwise True
        # use within the withdraw & transfer methods to check for sufficient funds before continuing
        if amount > self.balance:
            return False
        else:
            return True




