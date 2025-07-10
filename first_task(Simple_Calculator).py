#SIMPLE CALCULATOR
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
    
print("Which operation you want to perform:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")
    
operation = input("Enter your choice (+, -, *, /,%): ") 
    
if operation == '+':
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
elif operation == '-':
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
elif operation == '*':
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
elif operation == '%':
    result = num1 % num2
    print(f"Result: {num1} % {num2} = {result}")
    
else:
        print("Invalid operation. Please choose from (+, -, *, / or %).")
