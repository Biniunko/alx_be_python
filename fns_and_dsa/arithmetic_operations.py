def perform_operation(num1: float, num2: float, operation: str):
    operation = operation.lower()
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        raise ValueError(f"Invalid operation: {operation}")
