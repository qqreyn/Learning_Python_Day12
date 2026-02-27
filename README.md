# Learning_Python_Day12

Today's topic is error handling!

**Goal:** Use try-except blocks to handle errors gracefully and build robust programs

**Exercises:**

1. Wrap `int(input())` in try-except to catch `ValueError`  

2. Handle `ZeroDivisionError` in a division function  

3. Use multiple `except` blocks for different error types  

4. Implement a full `try-except-else-finally` structure  

5. Create a function that raises custom error messages using `raise`  

**mini-project:**
Safe Calculator:  
Build a simple calculator program that:

- Asks the user for two numbers  
- Asks for an operation (+, -, *, /)  
- Uses try-except to handle:
  - Invalid number input (`ValueError`)  
  - Division by zero (`ZeroDivisionError`)  
- Uses `else` to display the result if no error occurs  
- Uses `finally` to print a message like "Program finished"  
