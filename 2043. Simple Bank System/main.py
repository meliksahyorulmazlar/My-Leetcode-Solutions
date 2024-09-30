class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if len(self.balance) < account1:
            return False
        if len(self.balance) < account2:
            return False
        amount_money = self.balance[account1 - 1]
        if amount_money < money:
            return False
        else:
            self.balance[account1 - 1] -= money
            self.balance[account2 - 1] += money
            return True

    def deposit(self, account: int, money: int) -> bool:
        if len(self.balance) < account:
            return False
        else:
            self.balance[account - 1] += money
            return True

    def withdraw(self, account: int, money: int) -> bool:
        if len(self.balance) < account:
            return False
        amount = self.balance[account - 1]
        if amount >= money:
            self.balance[account - 1] -= money
            return True
        return False

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)