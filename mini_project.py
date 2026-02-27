def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    
    elif operation == "-":
        return num1 - num2
    
    elif operation == "*":
        return num1 * num2
    
    elif operation == "/":
        if num2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return num1 / num2
    
    else:
        raise ValueError("Invalid operation. Use +, -, *, or /.")


print("=== SAFE CALCULATOR ===")

try:
    # Input numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    # Input operation
    operation = input("Enter operation (+, -, *, /): ")
    
    # Perform calculation
    result = calculate(num1, num2, operation)

except ValueError as e:
    print("Input Error:", e)

except ZeroDivisionError as e:
    print("Math Error:", e)

else:
    print("Result:", result)

finally:
    print("Calculator session finished.")