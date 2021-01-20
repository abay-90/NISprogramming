import mymodules

start_time = mymodules.create_time()

guess_another = "y"

while guess_another == "y":
    user_value = int(input("Enter a number in the range 1 to 9:  "))
    random_number = mymodules.generate_random(10)

    if user_value == random_number:
        print("Congratulations, you guessed correctly!")
    else:
        print("Better luck next time, the answer was {0}.".format(random_number))

    guess_another = input("Do you want to try again?  Enter y for Yes or any other key to end the game:  ")

end_time = mymodules.create_time()
print("You started playing at {0}.".format(mymodules.output_local_time(start_time)))
print("You played for {0} seconds.".format(mymodules.calculate_difference(start_time, end_time)))

