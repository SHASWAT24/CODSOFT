def calculate(num1, num2, operation):
    if operation == '1':
        return num1 + num2
    elif operation == '2':
        return num1 - num2
    elif operation == '3':
        return num1 * num2
    elif operation == '4':
        return num1 / num2
    else:
        return "Invalid operation"

print("Welcome to the simple calculator!")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("Choose the operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
operation = input("Enter the number corresponding to the operation (1/2/3/4): ")


result = calculate(num1, num2, operation)
print(f"The result of the calculation is: {result}")
