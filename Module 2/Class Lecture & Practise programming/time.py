from datetime import *

now = datetime.today()
print("Today: ",now)
print("Current time:  ", now.hour, ":", now.minute, sep="")
print("Today is a ", now.strftime("%A"),sep="")#a for datename
print("The month is ", now.strftime("%B"),sep="")# b for monthname
