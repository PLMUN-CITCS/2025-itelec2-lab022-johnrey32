# John Rey Bulfa
# ITELEC2
# Laboratory #22 – Guided Coding Exercise:
# Variables, Literals, and Case-Sensitivity in Python (with Naming Conventions)

def display_menu():
    print("Menu:")
    print("1. Great User")
    print("2. Check EVen/Odd")
    print("3. Exit")
    print("Enter yout choice (1-3): ", end='')

def handle_menu_choice(choice: int) -> bool:
    if choice == 1:
        greet_user()
    elif choice == 2:
        even_odd_checker_action()
    elif choice == 3:
        print("Exiting program. Goodbye!")
        return True
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
    return False

def greet_user():
    print("Hello! Welcome!")

def even_odd_checker_action():
    number = get_integer_input("Enter an integer: ")
    if number % 2 == 0:
        print(f"{number} is an Even number. ")
    else:
        print(f"{number} is an Odd number. ")

def get_integer_input(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer. ")

def main():
    while True:
        display_menu()
        try:
            choice = int(input())
            if handle_menu_choice(choice):
                break
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 3. ")
        print("------------------------------------")
if __name__ == "__main__":
    main()