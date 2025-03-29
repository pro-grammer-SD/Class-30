class Bank:
    def __init__(self, balance, password):
        self.__balance = balance  # Private balance
        self.__password = password  # Private password

    def get_balance(self, password):
        if password == self.__password:
            return f"Your balance is: {self.__balance}"
        else:
            raise PermissionError("Access denied! Wrong password.")

    @property
    def balance(self):
        raise PermissionError("Access denied! You ain't gettin' this info.")

    def deposit(self, amount, password):
        if password == self.__password:
            self.__balance += amount
            return f"Deposited {amount}. New balance: {self.__balance}"
        else:
            raise PermissionError("Nice try, but wrong password.")

    def withdraw(self, amount, password):
        if password == self.__password:
            if amount > self.__balance:
                return "Insufficient funds!"
            self.__balance -= amount
            return f"Withdrew {amount}. New balance: {self.__balance}"
        else:
            raise PermissionError("Access denied! Wrong password.")

# 🔥 Example Usage
bnk = Bank(45274, "secure123")  # Set an initial balance and password

try:
    print(bnk.get_balance("wrongpass"))  # Should deny access
except PermissionError as e:
    print(e)

print(bnk.get_balance("secure123"))  # Correct password, shows balance
print(bnk.deposit(5000, "secure123"))  # Deposit money
print(bnk.withdraw(20000, "secure123"))  # Withdraw money
