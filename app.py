# app.py
def add_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(num1, num2):
    return num1 - num2

def multiply_numbers(num1, num2):
    return num1 * num2

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None

def calculator():
    while True:
        print("\nCalculator Menu:")
        print("1. Add two numbers")
        print("2. Subtract two numbers")
        print("3. Multiply two numbers")
        print("4. Divide two numbers")
        print("5. Quit")

        user_choice = input("Enter your choice (1-5): ")

        if user_choice == '5':
            print("Goodbye!")
            break

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Error: Please enter valid numeric values.")
            continue

        if user_choice == '1':
            result = add_numbers(num1, num2)
            print(f"Result: {result}")
        elif user_choice == '2':
            result = subtract_numbers(num1, num2)
            print(f"Result: {result}")
        elif user_choice == '3':
            result = multiply_numbers(num1, num2)
            print(f"Result: {result}")
        elif user_choice == '4':
            result = divide_numbers(num1, num2)
            if result is not None:
                print(f"Result: {result}")

        run_again = input("Do you want to run the calculator again? (yes/no): ")
        if run_again.lower() != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    calculator()
