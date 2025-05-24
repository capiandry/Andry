class Car:
    # Class variable
    total_cars = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_cars += 1

    def get_details(self):
        """Returns car details as a formatted string."""
        return f"Car: {self.brand} {self.model}"

    @classmethod
    def get_total_cars(cls):
        """Returns the total number of cars created."""
        return cls.total_cars


class Student:
    # Class variable
    total_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.total_students += 1

    def get_info(self):
        """Returns student details."""
        return f"Student: {self.name}, Age: {self.age}"

    @classmethod
    def get_total_students(cls):
        """Returns the total number of students."""
        return cls.total_students


class BankAccount:

    bank_name = "Global Bank"

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """Adds the amount to the balance."""
        self.balance += amount
        return f"{amount} deposited. New balance: {self.balance}"

    def withdraw(self, amount):
        """Deducts the amount from the balance if possible."""
        if amount <= self.balance:
            self.balance -= amount
            return f"{amount} withdrawn. Remaining balance: {self.balance}"
        else:
            return "Insufficient funds"