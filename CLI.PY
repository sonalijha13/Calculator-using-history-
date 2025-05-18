
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "Error (divide by zero)"

def save_to_history(expr, result):
    with open("history.txt", "a") as f:
        f.write(f"{expr} = {result}\n")

def view_history():
    print("\n--- Calculation History ---")
    try:
        with open("history.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No history found.\n")

def main():
    while True:
        print("\n=== Simple Calculator ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. View History")
        print("6. Exit")
        choice = input("Choose operation (1-6): ")

        if choice == '6':
            print("Goodbye!")
            break
        elif choice == '5':
            view_history()
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        if choice == '1':
            result = add(num1, num2)
            op = "+"
        elif choice == '2':
            result = subtract(num1, num2)
            op = "-"
        elif choice == '3':
            result = multiply(num1, num2)
            op = "*"
        elif choice == '4':
            result = divide(num1, num2)
            op = "/"
        else:
            print("Invalid choice.")
            continue

        print(f"Result: {result}")
        save_to_history(f"{num1} {op} {num2}", result)

if __name__ == "__main__":
    main()
