# Function to perform calculation based on operator
def calculate(a: float, b: float, operator: str) -> float | None:
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            print("Error: Division by zero is not allowed.")
            return None
    else:
        print(f"Error: Unsupported operator '{operator}'")
        return None

# Function to get user input
def get_input() -> tuple[float, float, str]:
    try:
        arg1 = float(input("Enter the first number: "))
        arg2 = float(input("Enter the second number: "))
        op = input("Enter an operator (+, -, *, /): ").strip()
        return arg1, arg2, op
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return 0.0, 0.0, '+'

# Function to display result
def show_result(a: float, b: float, op: str, result: float | None) -> None:
    if result is not None:
        print(f"Result: {a} {op} {b} = {result}")
    else:
        print("Calculation could not be completed.")

# Entry point of the program
def main() -> None:
    a, b, op = get_input()
    result = calculate(a, b, op)
    show_result(a, b, op, result)

# Run the program only if this file is executed directly
if __name__ == "__main__":
    main()