import pickle, os

# Runs the code in the loop three times.  In the first loop the pickle
# won't initially exist.  It will be created at the end of the
# first loop.  The second loop will then load the data from the
# pickle and save new data at the end of the loop.  This will
# continue for the third loop.
for runs in range(0, 3):
    print("Loop {}".format(runs + 1))
    # Create a list with a few default values
    data = [0, 1, 2, 3]

    # Test if the pickle exists.  If it exists,
    # it means the program has been run before and
    # there is data to load.

    if os.path.isfile("../../../Downloads/0302_Python_fileshela_1/0302 Python fileshela/mypickle.dat"):
        print("Loading pickle")
        # If it does, open the pickle file
        the_saved_pickle = open("../../../Downloads/0302_Python_fileshela_1/0302 Python fileshela/mypickle.dat", "rb")
        # Use pickle to read the data from the file.
        # Since it was (hopefully) stored as a list,
        # it will be loaded as a list.
        data = pickle.load(the_saved_pickle)
        the_saved_pickle.close()
    else:
        print("No pickle to load")

    print("Data before modification:")
    print(data)

    # Update the data

    for i in range(0, 4):
        data[i] = data[i] + 1

    print("Data after modification:")
    print(data)

    print("Pickling the data")
    the_new_pickle = open("../../../Downloads/0302_Python_fileshela_1/0302 Python fileshela/mypickle.dat", "wb")
    # Use the dump() method to save the data to the file
    pickle.dump(data, the_new_pickle)
    the_new_pickle.close()
    print("-" * 30)
