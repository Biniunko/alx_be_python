num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
valid_operation = True

match operation:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Cannot divide by zero!")
            valid_operation = False
    case _:
        print("invalid operation")

if valid_operation:
    print(f"The result is {operation}.")
