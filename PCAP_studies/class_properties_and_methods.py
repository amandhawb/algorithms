# Create a Student class with attributes for name, age, and grades. Add a method to calculate the average grade and another method to print all attributes using __dict__.
class Student:
    def __init__(self, name, age, grades) -> None:
        self.name = name
        self.age = age
        self.grades = grades
    
    def average_grade(self):
        total = sum(self.grades)
        grade_count = len(self.grades)
        result = total / grade_count
        return f"The average grade for {self.name} is {result:.2f}"
    
    def student_attributes(self):
        return self.__dict__

# TEST
obj = Student("Amandha", 24, [98.76, 96.00, 92.12, 99.23, 100.00])
print(obj.average_grade())
print(obj.student_attributes())

# Modify the Dog class to include an __init__ argument for color and use self to store it.
class Animal:
    def eat(self):
        return "Eating..."

class Dog(Animal):
    def __init__(self, color, breed) -> None:
        super().__init__()
        self.color = color
        self.breed = breed
    
    def details(self):
        return f"This dog is a {self.color} {self.breed}"

# Create a Bank class with self.bank_name initialized in the constructor. Add a method to display the bank name.
class Bank:
    def __init__(self, bank_name) -> None:
        self.bank_name = bank_name
    
    def display_bank_name(self):
        return f"The bank name is: {self.bank_name}"