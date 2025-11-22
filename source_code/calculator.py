print("Simple Calculator")
print("-----------------")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

while True:
    choice = input("\nEnter choice (1/2/3/4) or 'q' to quit: ")

    if choice == 'q':
        print("Exiting calculator. Goodbye!")
        break

    if choice not in ('1', '2', '3', '4'):
        print("Invalid choice. Please choose 1, 2, 3, 4 or q.")
        continue

    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = num1 + num2
        print("Result:", result)

    elif choice == '2':
        result = num1 - num2
        print("Result:", result)

    elif choice == '3':
        result = num1 * num2
        print("Result:", result)

    elif choice == '4':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print("Result:", result)
