import cgi   #<------cgi allows to access the key:value pairs.


data = cgi.FieldStorage() #<-----Create field storage object and assign as data and takes query string chops up in key:value pairs
studentnumber = data.getvalue("studentnumber")

name = "Not"
surname = "found"
description = "This student could not be found."

if studentnumber == "1":
	name = "Shaq"
	surname = "O Neal"
	description = "Shaq is a very dominate student."

if studentnumber == "2":
	name = "Kobe"
	surname = "Bryant"
	description = "Kobe is our best student."

if studentnumber == "3":
	name = "Giannis"
	surname = "Antetokounmpo"
	description = "Giannis needs to work harder."


print("Content-Type: text/html")
print()
print("<!DOCTYPE HTML>")
print("<html>")
print("<head>")
print("<title>Student details</title>")
print("</head>")
print("<body>")
print("<h1>{} {}</h1>".format(name, surname))
print("<p>{}</p>".format(description))
print("<a href=\"studentlist.html\">Back</a>")
print("</body>")
print("</html>")