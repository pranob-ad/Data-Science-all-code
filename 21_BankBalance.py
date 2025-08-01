class Bank_Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance 
        # double underscore make the variable private. we can't use it direatly from out side

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0< amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.__balance
    
#out side
account = Bank_Account("Tony Stak", 5000)
a = int(input("deposit amount:"))
b = int(input("withdew amount:"))
account.deposit(a)
account.withdraw(b)
print("final Balance:", account.get_balance())
#print(account.__balance) #This will give AttributeError due to private variable