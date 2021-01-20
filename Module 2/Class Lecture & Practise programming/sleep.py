from time import *

start = time()
start_time = localtime(start)
print("Started at: ", strftime("%X",start_time))

for i in range(0,10):
    print(i + 1)
    sleep(1) # Pauses for a second

end = time()
difference = end - start
print("The loop ran for", difference, "seconds.")
