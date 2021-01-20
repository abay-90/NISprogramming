the_string = input('Please enter your string: ')  # Adding a string used
print('For menu, press \'m\'')


def __editor():
    __input = 0  # __input given the value '0' for the loop be valid
    while __input != 'e':  # Start of the loop
        print()
        print('Current text: ', the_string)
        print()
        __input = input('Enter choice: ')  # Input for choices given
        if __input.lower() == 'e':  # Exit program
            exit('Exiting program.')
        elif __input.lower() == 'm':  # Print menu, imported from the __menu function
            print(__menu())
        # # Couldn't manage to make the part under working
        elif __input.lower() == 'n':  # Add new string
            new_string = input('This is the new string: ')
            print(new_string)
        elif __input == '1':  # Input given to display the string as uppercase
            print(the_string.upper())
        elif __input == '2':  # Input given to display the string as lowercase
            print(the_string.lower())
        elif __input == '3':  # Input given to display the string as title case
            print(the_string.title())
        elif __input == '4':  # Input given to display the string stripped of whitespaces in front and behind
            print(the_string.strip())
        else:  # If a invalid option is given, return to beginning.
            print('Invalid choice, please try again.')


def __menu():  # Displaying the menu, with choices given
    print('1: Uppercase')
    print('2: Lowercase')
    print('3: Title case')
    print('4: Remove front and back whitespaces')
    print('e: Exit program')


print(__editor())