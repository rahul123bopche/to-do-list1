def calculator():
    print("Welcome to the Simple Calculator!")

    # Get user input
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    operation = input("Enter the number of the operation (1/2/3/4): ")

    # Perform the selected operation
    if operation == '1':
        result = num1 + num2
        op = '+'
    elif operation == '2':
        result = num1 - num2
        op = '-'
    elif operation == '3':
        result = num1 * num2
        op = '*'
    elif operation == '4':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
        op = '/'
    else:
        print("Invalid operation choice.")
        return

    # Display result
    print(f"\nResult: {num1} {op} {num2} = {result}")


# Run the calculator
calculator()
