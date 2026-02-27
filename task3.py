try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)

except ValueError:
    print("Error: Please enter valid integers.")

except ZeroDivisionError:
    print("Error: You cannot divide by zero.")