def division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Division with 0 is impossible")


print("Enter 2 numbers for division!")

try:
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))
except ValueError:
    print("NOT A NUMBER!")

print(num1, "/", num2, "=", division(num1, num2))