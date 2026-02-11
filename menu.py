"""
Menu Module - Implements a Menu class for running Linux utilities
This module provides a menu-driven interface to execute common Linux commands
"""

import os


class Menu:
    """
    A class to display a menu and execute Linux utilities based on user selection.
    
    The Menu class maintains a list of menu options and provides methods to:
    - Add menu options
    - Display the menu to the user
    - Collect and validate user input
    - Execute corresponding Linux commands
    """
    
    def __init__(self):
        """
        Constructor for Menu class.
        Initializes an empty list to store menu options.
        """
        self._options = []
    
    def addOption(self, option):
        """
        Add a menu option to the options list.
        
        Args:
            option (str): The menu option text to add
        """
        self._options.append(option)
    
    def displayMenu(self):
        """
        Display the menu options to the user.
        Shows all available options with their corresponding numbers.
        """
        print("\n" + "="*50)
        print("Linux Utilities Menu")
        print("="*50)
        for i, option in enumerate(self._options, 1):
            print(f"{i}. {option}")
        print("="*50)
    
    def getInput(self):
        """
        Collect and validate user input.
        
        Continuously prompts the user for input until a valid option is selected
        or the user chooses to quit. Validates that input is numeric and within
        the valid range of menu options.
        
        Returns:
            int: The user's valid menu selection (1-based index)
        """
        while True:
            self.displayMenu()
            try:
                user_input = input("\nEnter your choice (or 'Q' to quit): ").strip()
                
                # Check if user wants to quit
                if user_input.upper() == 'Q':
                    print("\nExiting program. Goodbye!")
                    return len(self._options)  # Return the quit option number
                
                # Convert to integer and validate
                choice = int(user_input)
                
                # Validate the choice is within range
                if 1 <= choice <= len(self._options):
                    return choice
                else:
                    print(f"\n*** Invalid choice! Please enter a number between 1 and {len(self._options)} ***")
                    input("Press Enter to continue...")
            
            except ValueError:
                print("\n*** Invalid input! Please enter a number or 'Q' to quit ***")
                input("Press Enter to continue...")
    
    def run_bash_cmd(self, choice):
        """
        Execute a Linux utility based on the user's choice.
        
        This method uses a dictionary-based approach (refactored from if/elif)
        for improved readability, maintainability, and reduced complexity.
        
        Args:
            choice (int): The user's menu selection
        """
       
        commands = {
            1: {
                'cmd': 'ps aux',
                'description': 'Displaying running processes'
            },
            2: {
                'cmd': 'df -h',
                'description': 'Displaying disk usage'
            },
            3: {
                'cmd': 'uptime',
                'description': 'Displaying system uptime'
            }
        }
        
        if choice in commands:
            print(f"\n{commands[choice]['description']}...")
            print("-" * 50)
            os.system(commands[choice]['cmd'])
            print("-" * 50)
            input("\nPress Enter to continue...")
        elif choice == 4:
            print("\nExiting program. Goodbye!")
        else:
            print(f"\n*** Invalid choice: {choice} ***")
