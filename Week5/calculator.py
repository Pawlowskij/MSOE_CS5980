# Creates a calculator class for performing math operations

class Calculator:
    def add(self, first_number, second_number):
        # Adds two numbers together
        value = first_number + second_number
        return value

    def subtract(self, first_number, second_number):
        # Subtracts two numbers
        value = first_number - second_number
        return value

    def multiply(self, first_number, second_number):
        # Multiplies two numbers
        value = first_number * second_number
        return value

    def divide(self, first_number, second_number):
        # Divides two numbers
        value = first_number / second_number
        return value

    def modulo(self, first_number, second_number):
        # Returns the modulo of two numbers
        value = first_number % second_number
        return value

    def exp(self, first_number, second_number):
        # Raises the first number to the power of the second
        value = first_number ** second_number
        return value
