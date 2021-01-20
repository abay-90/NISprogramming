# Convert minutes to day, hour and seconds

time = float(input("Input time in minutes: "))
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 28800
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))
