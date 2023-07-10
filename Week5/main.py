import argparse

from calculator import Calculator

# Check to see that current module is being ran as a script
if __name__ == '__main__':
    # Define parser and brief explanation of what it does
    parser = argparse.ArgumentParser(description="Perform the following potential math operations"
                                             " on two numbers: +, -, x, /, %, ^")
    # Add parser arguments for the first number, operator and second number
    parser.add_argument("firstNumber", help="Enter your first number", type=float)
    parser.add_argument("operand", help="enter your operator", type=str)
    parser.add_argument("secondNumber", help="Enter your first number", type=float)
    args = parser.parse_args()

    # create a calculator instance
    calculator = Calculator()

    try:
        # which operator was entered and perform the appropriate operator
        if args.operand == "+":
            answer = calculator.add(args.firstNumber, args.secondNumber)
        elif args.operand == "-":
            answer = calculator.subtract(args.firstNumber, args.secondNumber)
        elif args.operand == "x":
            answer = calculator.multiply(args.firstNumber, args.secondNumber)
        elif args.operand == "/":
            answer = calculator.divide(args.firstNumber, args.secondNumber)
        elif args.operand == "%":
            answer = calculator.modulo(args.firstNumber, args.secondNumber)
        elif args.operand == "^":
            answer = calculator.exp(args.firstNumber, args.secondNumber)
        # Check for unexpected operator entry
        else:
            print("Invalid operation")
            exit(1)
        # Print the operation answer
        print(f"Answer: {answer}")
    # Check for value error
    except ValueError as e:
        print(f"Error: {e}")

