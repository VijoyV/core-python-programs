# Define a function to perform calculation
def calculate(a: float, b: float, operator: str) -> float:
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

# --- Main Program Starts Here ---

# Get user input for the two numbers and the operator
arg1 = float(input("Enter the first number: "))
arg2 = float(input("Enter the second number: "))
op = input("Enter an operator (+, -, *, /): ")

# Call the function and store the result
result = calculate(arg1, arg2, op)

# Display the result if calculation was successful
if result is not None:
    print(f"Result: {arg1} {op} {arg2} = {result}")