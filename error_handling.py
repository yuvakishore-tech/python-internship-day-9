import logging

logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    result = divide(x, y)
    print("Result:", result)

except ValueError as e:
    logging.error(e)
    print(e)

except ZeroDivisionError as e:
    logging.error(e)
    print("Cannot divide by zero")

except Exception as e:
    logging.error(e)
    print("Unexpected error occurred")

else:
    print("Execution successful")

finally:
    print("Program finished")
