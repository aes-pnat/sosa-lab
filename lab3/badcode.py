import os

import getpass

import ast

import hashlib

def hash_password(password):

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    return hashed_password

class OperationsManager():
    def __init__(self, a: float, b: float) -> None:

        self.a = a

        self.b = b

  

    def perform_division(self) -> float:

        """Divides a with b. If b is zero, returns NaN."""
        if self.b != 0 :
            return self.a / self.b 
        return float('nan')
  
  

def login_success():
    try:
        a = float(input("A = "))
        b = float(input("B = "))
        ops_manager = OperationsManager(a, b)
        print(ops_manager.perform_division())
    except ValueError:
        print("Invalid input for A or B")

    
    expression = input('Enter a mathematical formula to calculate: ')

    try:
        result = eval(expression)
        print("Result: ", result)
    except (SyntaxError, NameError, ZeroDivisionError):
        print("Invalid expression.")


  
  

if __name__ == "__main__":

    user = input("Username: ")

    password = getpass.getpass("Password: ")

    if user != "root" or hash_password(password) != 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3':

        print("Wrong username or password!")

        exit(0)

    else:

        print("Login success!")

        login_success()