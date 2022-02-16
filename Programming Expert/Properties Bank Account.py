class BankAccount: ## Private attributes (get and set methods)
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name
        self._balance = 0.0

    def get_balance(self):
        return round(self._balance)

    def set_balance(self, balance):
        if type(balance) not in [int, float]:
            return 

        if balance < 0 or balance >= 100000:
            return 
        
        self._balance = balance


class BankAccount: ## Private attributes (@property decorator)
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name
        self._balance = 0

    @property
    def balance(self):
        return round(self._balance)

    @balance.setter
    def balance(self, balance):
        if type(balance) not in [int, float]:
            return 

        if balance < 0 or balance >= 100000:
            return
        
        self._balance = balance
 

account = BankAccount('Tehran')
print(account.balance)

account.balance = 17.3
print(account.balance)
print(account)


























