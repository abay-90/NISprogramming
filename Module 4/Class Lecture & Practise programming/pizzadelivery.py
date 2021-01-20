import cgi

data = cgi.FieldStorage()

location = data.getvalue("location")
address = ""

if location == "Home":
	address = "Home Street 1<br/>Hometown<br/>1234"

if location == "Holiday home":
	address = "Vacation lane 34<br/>Seaville<br/>5432"

if location == "Work":
	address = "Fatigue Road 55<br/>Tiredton<br/>4839"

print("Content-Type: text/html")
print()
print("<!DOCTYPE HTML>")
print("<html>")
print("<head>")
print("<title>Pizza delivery location</title>")
print("</head>")
print("<body>")
print("<h1>{}</h1>".format(location))
print("{}<br/><br/>".format(address))
print("<a href=\"pizzadelivery.html\">Back</a>")
print("</body>")
print("</html>")