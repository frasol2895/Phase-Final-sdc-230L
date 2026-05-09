# calculator.py
# Project Week 2: Software Design and Control Statements
# Author: Frank (your name)

class Calculator:
    def print_header(self):
        """Prints the required informative header line."""
        print("Project Week 2: Software Design and Control Statements - Basic Calculator by Frank")

    def print_welcome(self):
        """Prints a welcome message with instructions."""
        print("\nWelcome to my Basic Calculator!")
        print("Choose an option from the menu below.")
        print("You can add, subtract, multiply, divide, or enter a simple formula.")

    def display_menu(self):
        """Displays the menu and returns the user's choice."""
        print("\n=== MENU ===")
        print("1. Add two numbers")
        print("2. Subtract two numbers")
        print("3. Multiply two numbers")
        print("4. Divide two numbers")
        print("5. Enter a formula for evaluation (e.g. 6 - 9)")
        print("6. Quit")
        while True:
            try:
                choice = int(input("Enter your choice (1-6): "))
                if 1 <= choice <= 6:
                    return choice
                else:
                    print("Please enter a number between 1 and 6.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def get_two_numbers(self):
        """Asks for two numbers and returns them as floats."""
        while True:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                return num1, num2
            except ValueError:
                print("Invalid number. Please try again.")

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero!"
        return a / b

    def evaluate_formula(self):
        """Allows user to enter a simple formula and evaluates it safely."""
        formula = input("Enter a simple formula (e.g. 6 - 9 or 12 * 3): ")
        try:
            # Safe evaluation for basic math only
            result = eval(formula, {"__builtins__": {}}, {"abs": abs, "round": round})
            return result
        except:
            return "Error: Invalid formula!"

    def run(self):
        """Main program loop – runs until user quits."""
        self.print_header()
        self.print_welcome()
        
        while True:
            choice = self.display_menu()
            
            if choice == 6:
                break
            elif choice in [1, 2, 3, 4]:
                num1, num2 = self.get_two_numbers()
                if choice == 1:
                    result = self.add(num1, num2)
                    print(f"Result: {num1} + {num2} = {result}")
                elif choice == 2:
                    result = self.subtract(num1, num2)
                    print(f"Result: {num1} - {num2} = {result}")
                elif choice == 3:
                    result = self.multiply(num1, num2)
                    print(f"Result: {num1} * {num2} = {result}")
                elif choice == 4:
                    result = self.divide(num1, num2)
                    print(f"Result: {num1} / {num2} = {result}")
            elif choice == 5:
                result = self.evaluate_formula()
                print(f"Result: {result}")
        
        print("\nThank you for using my calculator! Goodbye.")


# Run the program
if __name__ == "__main__":
    calc = Calculator()
    calc.run()