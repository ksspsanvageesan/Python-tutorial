# calculator.py

def get_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("Simple Terminal Calculator")
    print("Operations: +  -  *  /")
    print("Type 'q' to quit.\n")

    while True:
        op = input("Enter operator (+ - * /) or q: ").strip().lower()
        if op in ("q", "quit", "exit"):
            print("Bye!")
            break

        if op not in ("+", "-", "*", "/"):
            print("Invalid operator. Try again.\n")
            continue

        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        else:  # "/"
            if b == 0:
                print("Error: division by zero.\n")
                continue
            result = a / b

        print(f"Result: {result}\n")

if __name__ == "__main__":
    main()