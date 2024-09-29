def perform_operation(num1 , num2, operation):
    if operation=="add":
        return num1+num2
    elif operation=="subtract":
        return num1-num2
    elif operation=="multiply":
        return num1*num2
    elif operation=="divide":
        if num2==0:
            print("Division by zero is undefined")
        return num1/num2
    else:
        return ValueError(f"Invalid operation: {operation}")
