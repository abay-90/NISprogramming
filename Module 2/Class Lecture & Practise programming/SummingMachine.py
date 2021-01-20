def summing_machine():
    total = 0
    user_input = input("Please enter a number: ")

    # The exercise does not require error checking
    # so assume that the user will enter either a number
    # or s.
    while user_input != "s":
        total += int(user_input)
        user_input = input("Please enter a number: ")

    return total


if __name__ == "__main__":
    print(summing_machine())

