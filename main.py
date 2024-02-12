from data_preprocessing import load_dataset, explore_data

from colorama import init, Fore

from menu import display_menu, get_user_choice

import os

from exploratory_analysis import (
    descriptive_statistics,
    gender_analysis,
    academic_year_analysis,
    correlation_analysis,
    score_distribution
)

from term_performance import term_performance

from insights_and_recommendations import generate_insights

from dashboard import create_dashboard


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def cmd_execute(function, *args):
    terminal_choice = input("Do you want to clear the terminal? (y/n): ").lower()
    if terminal_choice == 'y':
        clear_terminal()
    elif terminal_choice != 'n':
        print("Invalid input. Continuing without clearing the terminal.")

    try:
        function(*args)
    except Exception as e:
        print(f"Error executing {function.__name__}: {e}")


if __name__ == "__main__":
    init(autoreset=True)
    print(Fore.MAGENTA + "**Student Performance Analysis App (v1.0)**\n" + Fore.RESET)
    print(Fore.YELLOW + "Data Loading & Exploration Started" + Fore.RESET)

    file_path = 'Students Data.xlsx'
    try:
        df = load_dataset(file_path, file_type='xlsx')
        explore_data(df)
        print(Fore.GREEN + "DONE\n" + Fore.RESET)
    except Exception as e:
        print(f"Error loading dataset: {e}")
        exit()

    input("Press a key to continue to the menu")
    clear_terminal()

    while True:
        display_menu()
        user_choice = get_user_choice()

        analysis_functions = {
            1: descriptive_statistics,
            2: gender_analysis,
            3: academic_year_analysis,
            4: correlation_analysis,
            5: score_distribution,
            6: generate_insights,
            7: term_performance,
            8: create_dashboard,
        }

        if user_choice in analysis_functions:
            cmd_execute(analysis_functions[user_choice], df)
        elif user_choice == 9:
            print("Exiting the program. Goodbye!")
            break

    # APP VERSION : BETA

# TODO : UPDATE THE APP TO VERSION 1.0
