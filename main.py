"""
Main Module - Entry point for Linux Utilities Menu Application
This module creates and runs the menu-driven interface for Linux utilities
"""

from menu import Menu


def main():
    """
    Main function that serves as the public interface for the application.
    
    Creates a Menu instance, establishes menu options, and runs the menu loop
    to allow users to execute Linux utilities.
    """
    # Create an instance of the Menu class
    menu = Menu()
    
    # Establish the menu options
    menu.addOption("Display running processes (ps)")
    menu.addOption("Display disk usage (df)")
    menu.addOption("Display system uptime")
    menu.addOption("Exit")
    
    # Main menu loop
    while True:
        # Get user input
        choice = menu.getInput()
        
        # Execute the command or exit
        if choice == 4 or choice == len(menu._options):
            print("\nThank you for using Linux Utilities Menu!")
            break
        else:
            menu.run_bash_cmd(choice)


if __name__ == "__main__":
    main()
