def division(x, y):
    if y == 0:
        raise ZeroDivisionError("Division by zero is impossible.")

    result = x / y

    if result < 0:
        raise ValueError("Result cannot be negative.")

    return result


print("Enter 2 numbers to divide them")

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    output = division(num1, num2)

except ValueError as e:
    print("Value Error:", e)

except ZeroDivisionError as e:
    print("Math Error:", e)

else:
    print("Result:", output)

finally:
    print("Program finished.")