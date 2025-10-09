class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Otillräcklig saldo!")
        else:
            self.balance -= amount
    def show_balance(self):
        print (f"Hi {self.owner}! Your balance is: {self.balance}")

    def transfer_to(self, other_account, amount):
        if amount > self.balance:
            print(f"Otillräcklig saldo för att överföra {amount} kr!")
        else:
            self.balance -= amount
            other_account.balance += amount
            print(f"{self.owner} överförde {amount} kr till {other_account.owner}.")
            print(f"{self.owner} saldo: {self.balance} kr.")
            print(f"{other_account.owner} saldo: {other_account.balance} kr")



#Skapar konton
Account1 = BankAccount("Adam", 100)
Account2 = BankAccount("Carlos", 40014)

#Testa metoder

Account1.deposit(500)
Account1.withdraw(244)
Account1.show_balance()

Account2.deposit(333)
Account2.withdraw(3777)
Account2.show_balance()

Account1.transfer_to(Account2, 357)
Account1.transfer_to(Account2, 20)