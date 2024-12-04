# Creating a Custom Exception
# Define a custom exception NegativeBalanceError.

# Create a BankAccount class with methods deposit() and withdraw().
# Raise NegativeBalanceError in the withdraw() method if the balance goes below zero.

class NegativeBalanceError(Exception):
    def __init__(self, message="Balance cannot be negative!"):
        self.message = message
        super().__init__(self.message)

def withdraw(balance, amount):
    if balance - amount < 0:
        raise NegativeBalanceError(f"Insufficiente funds! Your current balance is {balance}.")
    return balance - amount

try:
    print(withdraw(100, 150))
except NegativeBalanceError as e:
    print(e)

# Custom Exception with Arguments
# Create a custom exception InvalidScoreError.

# Write a program that asks the user to input a score between 0 and 100.
# If the user enters a score outside this range, raise InvalidScoreError with a message showing the invalid score.

class InvalidScoreError(Exception):
    def __init__(self, message="The score is invalid."):
        self.message = message
        super().__init__(self.message)

def input_score():
    res = int(input("Enter a score between 0 and 100: "))
    if res < 0 or res > 100:
        raise InvalidScoreError(f"You entered {res} which is an invalid number.")
    return res

try:
    print(input_score())
except InvalidScoreError as e:
    print(e)


# Custom Exceptions in a Hierarchy
# Create a hierarchy of custom exceptions for a library system:

# LibraryError: Base exception.
# BookNotAvailableError: Raised when a requested book is unavailable.
# MemberLimitExceededError: Raised when a member tries to borrow more than the allowed number of books.
# Simulate scenarios to raise and handle these exceptions.

class LibraryError(Exception):
    def __init__(self, message="An error occurred in the library system"):
        self.message = message
        super().__init__(self.message)

class BookNotAvailableError(LibraryError):
    def __init__(self, message="The requested book is not available"):
        self.message = message
        super().__init__(self.message)

class MemberLimitExceededError(LibraryError):
    def __init__(self, message="You have exceeded the maximum number of borrowed books"):
        self.message = message
        super().__init__(self.message)

def borrow_book(book, member_books, max_books=2):
    if book not in available_books:
        raise BookNotAvailableError(f"'{book}' is not available.")
    if len(member_books) >= max_books:
        raise MemberLimitExceededError(f"Cannot borrow more than {max_books} books.")

    member_books.append(book)
    available_books.remove(book)
    return f"You have borrowed '{book}'."

available_books = ["Python 101", "Data Structures", "Machine Learning"]
member_books = []

try:
    print(borrow_book("Data Structures", member_books)) # should succeed
    print(borrow_book("Machine Learning", member_books)) # should succeed
    print(borrow_book("Deep Learning", member_books)) # should raise BookNotAvailableError
except LibraryError as e:
    print(e)

try:
    for book in available_books:
        member_books.append(book)
    print(borrow_book("Python 101", member_books)) # should raise MemberLimitExceededError
except LibraryError as e:
    print(e)