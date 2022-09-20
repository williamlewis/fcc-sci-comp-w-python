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
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0
    
    
    def deposit(self, amount, description=''):
        self.balance += amount
        self.ledger.append({'amount': amount, 'description': description})
    
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            amount *= -1
            self.balance += amount
            self.ledger.append({'amount': amount, 'description': description})
            return True
        else:
            return False
    
    def get_balance(self):
        return self.balance

    #def transfer(self, amount, destination):        
    def transfer(self, amount, destination: name@Category):
        if self.check_funds(amount):
            withdraw_descr = 'Transfer to ' + str(destination)
            self.withdraw(amount, withdraw_descr)
            
            deposit_descr = 'Transfer from ' + str(self.name)
            destination_cat = Category(destination) # necessary because argument was read as a str instead of another class instance
            # destination_cat.deposit(amount, deposit_descr) # the ledger note is NOT going through & being appended to the destination instance
            

            destination_cat.balance += amount
            destination_cat.ledger.append(deposit_descr)

            # print(self.ledger)
            print(Category(destination).balance)
            print(Category(destination).ledger)            
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True


'''
obj1 = Category('food')
obj1.deposit(900, 'deposit')
obj1.withdraw(45.67, 'milk, cereal, eggs, bacon, bread')
print(obj1.get_balance())
'''


obj = Category('food')
obj.deposit(900, 'deposit')
obj.withdraw(45.67, 'milk, cereal, eggs, bacon, bread')
obj.deposit(1200, 'just a test here')
print(obj.ledger)
#print(obj.get_balance())

obj_e = Category('entertainment')
obj_e.deposit(100, 'ent deposit')
#print(obj_e.get_balance())

obj_e.transfer(80, 'food')
print(obj.ledger)

#print(obj.get_balance())
#print(obj_e.get_balance())






'''
def test_transfer(self):
        self.food.deposit(900, "deposit")
        self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
        transfer_amount = 20
        food_balance_before = self.food.get_balance()
        entertainment_balance_before = self.entertainment.get_balance()
        good_transfer = self.food.transfer(transfer_amount, self.entertainment)
        food_balance_after = self.food.get_balance()
        entertainment_balance_after = self.entertainment.get_balance()
        actual = self.food.ledger[2]
        expected = {"amount": -transfer_amount, "description": "Transfer to Entertainment"}
        self.assertEqual(actual, expected, 'Expected `transfer` method to create a specific ledger item in food object.')
        self.assertEqual(good_transfer, True, 'Expected `transfer` method to return `True`.')
        self.assertEqual(food_balance_before - food_balance_after, transfer_amount, 'Expected `transfer` method to reduce balance in food object.')
        self.assertEqual(entertainment_balance_after - entertainment_balance_before, transfer_amount, 'Expected `transfer` method to increase balance in entertainment object.')
        actual = self.entertainment.ledger[0]
        expected = {"amount": transfer_amount, "description": "Transfer from Food"}
        self.assertEqual(actual, expected, 'Expected `transfer` method to create a specific ledger item in entertainment object.')
'''