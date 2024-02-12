from colorama import init, Fore

init(autoreset=True)


def display_menu():
    print(Fore.MAGENTA + "\n\nAnalysis App Menu" + Fore.RESET)
    print("1. Descriptive Statistics For The (AGE, SCORE, TERM)")
    print("2. Gender Analysis")
    print("3. Academic Year Analysis")
    print("4. Correlation Analysis")
    print("5. Score Distribution Analysis")
    print("6. Generate Insights")
    print("7. Term Performance Analysis")
    print("8. Dashboard")
    print(f"9. {Fore.RED + 'Exit' + Fore.RESET}")


def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= 10:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
