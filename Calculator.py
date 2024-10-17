# Program to make a simple calculator

# Addition of two numbers
def add(x, y):
    return x + y

# Subtraction of two numbers
def subtract(x, y):
    return x - y

# Multiplication of two numbers
def multiply(x, y):
    return x * y

# Division of two numbers
def divide(x, y):
    return x / y

print("Select operation!!")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    # Enter the input
    choice = input("Enter the choice from 1 to 4: ")

    # Check if choice is valid
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            # Check to prevent division by zero
            if num2 != 0:
                print(num1, "/", num2, "=", divide(num1, num2))
            else:
                print("Error! Division by zero is not allowed.")

        break  # Exit the loop after a valid operation

    else:
        print("Invalid input, please enter a valid option (1 to 4).")
