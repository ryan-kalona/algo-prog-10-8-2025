class bank_acc:
    bank_name = "bca prioritas"

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt
        print(f"{self.owner} deposited ${amt}. new balance: ${self.balance}")

    def withdraw(self, amt):
        if amt > self.balance:
            print("too poor bro")
        else:
            self.balance -= amt
            print(f"{self.owner} withdrew ${amt}. New balance: ${self.balance}")

    def show_balance(self):
        print(f"account owner: {self.owner}")
        print(f"bank: {bank_acc.bank_name}")
        print(f"current balance: ${self.balance}")


acc1 = bank_acc("ryan", 500)
acc2 = bank_acc("rich", 1000)

acc1.deposit(200)
acc1.withdraw(100)
acc1.show_balance()

print()

acc2.deposit(500)
acc2.withdraw(300)
acc2.show_balance()
