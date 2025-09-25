# Handle division by zero gracefully.

try:
    numerator = int(input("Enter numerator"))
    denominator = int(input("Enter denominator"))
    result = numerator/denominator
except ZeroDivisionError:
    print("Error : cannot divide by zero")
else:
    print("Result: ", result) 
finally:
    print("Execution finished")
    