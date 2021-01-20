import pickle, os

# Runs the code in the loop three times.
# In the first loop the pickle won't initially exist.
# The second loop will then load the data from the;
# pickle and save new data at the end of the loop.
# This will continue for the third loop.
for runs in range(0, 3):
    print("loop {}".format(runs +1))
    # Creates a list with a few default values
    data = [0, 1, 2, 3]

    # Test if the pickle exits. If it exits,
    # this mean the program has been run before &;
    # there is data to load.

    if os.path.isfile("MyPickle.dat"):
        print("Loading pickle")
        # If it does, open the pickle file
        the_saved_pickle = open("MyPickle.dat", "rb")
        # Use pickle to read the data from the file.
        # Since it was (hopefully) stored as a list,
        # it will be loaded as a list.
        data = pickle.load(the_saved_pickle)
        the_saved_pickle.close()
    else:
        print("No pickle to load")

    print("Data before modification:")
    print(data)

    for i in range(0, 4):
        data[i] = data[i] +1

    print("Data after modification:")
    print(data)

    print("Pickling the data")
    the_new_pickle = open("MyPickle.dat", "wb")
    # Use the dump() method to save the data to the file
    pickle.dump(data, the_new_pickle)
    the_new_pickle.close()
    print("_" * 30)
