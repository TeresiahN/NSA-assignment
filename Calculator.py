def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y

# Prompt the user for input.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation.
if operation == "+":
  result = add(num1, num2)
elif operation == "-":
  result = subtract(num1, num2)
elif operation == "*":
  result = multiply(num1, num2)
elif operation == "/":
  result = divide(num1, num2)
else:
  print("Invalid operation.")

# Display the result.
print(result)