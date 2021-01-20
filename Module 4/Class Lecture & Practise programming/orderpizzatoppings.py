import cgi

data = cgi.FieldStorage()

# Create an unordered (bulleted) list to display the toppings
toppings = "<ul>"
price = 0

# Check if the checkbox was checked, i.e. if it has a value
if data.getvalue("cheese"):
	# Using the value from the checkbox
	# Each bulleted list item must be enclosed in li tags
	toppings += "<li>" + data.getvalue("cheese") + ":  0.50</li>"
	price += 0.50

if data.getvalue("bacon"):
	# Not using the value from the checkbox
	toppings += "<li>bacon:  0.90</li>"
	price += 0.90

if data.getvalue("pineapple"):
	toppings += "<li>pineapple:  0.70</li>"
	price += 0.70

if data.getvalue("avocado"):
	toppings += "<li>avocado:  0.80</li>"
	price += 0.80

toppings += "</ul>"

print("Content-Type: text/html")
print()
print("<!DOCTYPE HTML>")
print("<html>")
print("<head>")
print("<title>Pizza order</title>")
print("</head>")
print("<body>")
print("<h1>List of toppings:</h1>")
print(toppings)
print("Price:  {0:.2f}<br/><br/>".format(price))
print("<a href=\"pizzatoppings.html\">Back</a>")
print("</body>")
print("</html>")