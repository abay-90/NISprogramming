from random import random
import pickle, os

entries = dict()

if os.path.isfile("mypickle.dat"):
    the_saved_pickle = open("mypickle.dat", "rb")
    entries = pickle.load(the_saved_pickle)
    the_saved_pickle.close()
else:
    # This is a short cut to generating the database using ASCII values.
    # An alternative would have been
    # entries['a'] = int(random() * 1000)
    # entries['b'] = int(random() * 1000)
    # entries['c'] = int(random() * 1000)
    # ..... continue doing this until .....y
    # entries['z'] = int(random() * 1000)
    for current in range(97, 123):
        entries[chr(current)] = int(random() * 1000)

print(entries)

user_response = input("Do you wish to update an entry?  (y)es or (n)o:  ")

if user_response == "y":
    the_entry = input("Which entry, a to z:  ")
    the_value = int(input("Enter a new value:  "))
    entries[the_entry] = the_value

the_new_pickle = open("mypickle.dat", "wb")
pickle.dump(entries, the_new_pickle)
the_new_pickle.close()
