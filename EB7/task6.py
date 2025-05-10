# class Car:
#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed = speed
    
#     def get_car_brand(self):
#         print("My car brand is ", self.brand)

# mycar = Car("bmw", "4okmph")

# mytoyotacar = Car("toyota", "50kmph")

# mycar.get_car_brand()
# mytoyotacar.get_car_brand()


"""
Problem 1
Bank Account

attribute - account_number, balance

methods - deposit() and withdraw()

subclass 1 - SavingsAccount

attribute - interest_rate

method - calculate interest

"""

class BankAccount:

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance # using encapsulated balance value

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.__balance -= amount

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.__balance * self.interest_rate / 100
    
mysaving = SavingsAccount("123", 3000, 12.5)

print(mysaving.calculate_interest())