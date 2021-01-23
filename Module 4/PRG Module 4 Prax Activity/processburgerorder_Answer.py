import cgi
import os

data = cgi.FieldStorage()

price = 0
patty = data.getvalue("patty")
bread = data.getvalue("bread")

burger = patty
burger += " on " + bread

if patty == "Beef":
    price += 15

if patty == "Chicken":
    price += 12

if patty == "Rib":
    price += 17

if patty == "Vegetarian":
    price += 10

if bread == "Normal bun":
    price += 1

if bread == "Ciabatta":
    price += 3

if bread == "Angus bun":
    price += 2

toppings = ""

if data.getvalue("cheese"):
    toppings += " cheese"
    price += 2

if data.getvalue("tomato"):
    toppings += " tomato"
    price += 1

if data.getvalue("egg"):
    toppings += " egg"
    price += 2

if data.getvalue("bacon"):
    toppings += " bacon"
    price += 3

if data.getvalue("onion"):
    toppings += " onion"
    price += 1

if len(toppings) > 0:
    burger += " with" + toppings

if data.getvalue("loyalty"):
    burger += " (points earned)"

upload = data["user_image"]

filename = os.path.basename(upload.filename)

with open(filename, "wb") as copy:
    copy.write(upload.file.read())

print("Content-Type: text/html")
print()
print("<!DOCTYPE HTML>")
print("<html>")
print("<head>")
print("<title>Pet details</title>")
print("</head>")
print("<body>")
print("<h1>Your burger order</h1>")
print("<p>{0} @ {1:.2f}</p><br/>".format(burger, price))
print("<img src=\"{}\"/><br/><br/>".format(filename))
print("</body>")
print("</html>")