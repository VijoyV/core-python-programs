# Program to add three numbers and find their average

# Input: three numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Calculate sum
total = num1 + num2 + num3

# Calculate average
average = total / 3

# Output the results
print(f"Sum of the numbers: {total}")
print(f"Average of the numbers: {average}")