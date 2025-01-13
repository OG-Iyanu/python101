def calculator():
    print("Welcome to the Calculator App!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    while True:
        choice = input("\nEnter your choice (1/2/3/4/5): ")  # User inputs operation choice

        if choice == '5':  # Exit the program
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4'):  # Valid choices
            try:
                # Prompt user for numeric inputs
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                # Perform the chosen operation
                if choice == '1':
                    print(f"The result is: {num1 + num2}")
                elif choice == '2':
                    print(f"The result is: {num1 - num2}")
                elif choice == '3':
                    print(f"The result is: {num1 * num2}")
                elif choice == '4':
                    if num2 == 0:
                        print("Error: Division by zero is not allowed.")
                    else:
                        print(f"The result is: {num1 / num2}")
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid choice. Please select a valid operation.")
