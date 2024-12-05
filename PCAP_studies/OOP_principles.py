# Create a Car class with attributes for the model, make, and year. Add a drive() method that returns "The car is driving.".
class Car:
    def __init__(self, model, make, year) -> None:
        self.model = model
        self.make = make
        self.year = year

    def drive(self):
        return "The car is driving"

# Create a Rectangle class. Then create a Square class that inherits from it. Ensure the Square class has a method to calculate the area.

class Rectangle:
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self, side) -> None:
        super().__init__(side, side)

# Modify the Account class so users can only withdraw money if their balance after withdrawal is at least $10.
class Account:
    def __init__(self, balance) -> None:
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if self.__balance - amount < 10:
            return "Not allowed to withdraw: Minimum balance must be $10"
        else:
            self.__balance -= amount
            return f"Withdraw of ${amount} successful. Remaining balance: ${self.__balance}."
        
    def get_balance(self):
        return self.__balance