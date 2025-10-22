# Function to perform calculation
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
            print("Error: Division by zero.")
            return None
    else:
        print(f"Error: Unsupported operator '{operator}'")
        return None

# Main program
def main():
    print("Simple Calculator")
    arg1 = float(input("Enter the first number: "))
    arg2 = float(input("Enter the second number: "))
    op = input("Enter an operator (+, -, *, /): ")

    result = calculate(arg1, arg2, op)

    if result is not None:
        print(f"Result: {arg1} {op} {arg2} = {result}")
    else:
        print("Calculation failed.")

if __name__ == "__main__":
    main()