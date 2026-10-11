def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def modulus(a, b):
    return a % b


while True:
    first = float(input("\nEnter first number: "))
    second = float(input("Enter second number: "))
    operation = input("Choose operation (+, -, *, /, %): ")

    if operation == "+":
        answer = add(first, second)
        print("Result:", answer)
    elif operation == "-":
        answer = subtract(first, second)
        print("Result:", answer)
    elif operation == "*":
        answer = multiply(first, second)
        print("Result:", answer)
    elif operation == "/":
        if second == 0:
            print("Cannot divide by zero.")
        else:
            print("Result:", divide(first, second))
    elif operation == "%":
        if second == 0:
            print("Cannot use modulus with zero as the second number.")
        else:
            print("Result:", modulus(first, second))
    else:
        print("Invalid operation.")

    again = input("Do you want another calculation? (yes/no): ").lower()
    if again != "yes":
        print("Calculator closed.")
        break
