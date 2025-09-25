# Demonstrate multiple exception handling (ValueError, TypeError).

try:
    num = int(input("Enter a number: "))   # May raise ValueError
    result = 10 / num                      # May raise ZeroDivisionError
    text = "hello" + num                   # Will raise TypeError
except ValueError:
    print("Error: Invalid input, please enter a number.")
except TypeError:
    print("Error: Cannot add string and integer.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print("Result is:", result)
finally:
    print("Execution finished.")
