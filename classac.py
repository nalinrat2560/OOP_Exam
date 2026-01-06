class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print (f"ฝากเงิน : {amount} สำเร็จ")
        else:
            print(f"ยอดเงินไม่พอ")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"ถอนเงิน: {amount} สำเร็จ")
        else:
            print(f"ถอนเงินไม่สำเร็จ ยอดเงินไม่เพียงพอต่อการถอน {amount} บาท")

    def check_balance(self):
        return self.__balance