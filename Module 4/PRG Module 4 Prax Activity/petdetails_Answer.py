import cgi

data = cgi.FieldStorage()
pet_id = data.getvalue("pet_id")

pet_name = ""
html = ""

if pet_id == "1":
    pet_name = "Fluffy"
    html += "Our fluffiest pet"

if pet_id == "2":
    pet_name = "Spot"
    html += "Our spottiest pet"

if pet_id == "3":
    pet_name = "Snuffles"
    html += "A friendly little guy"


print("Content-Type: text/html")
print()
print("<!DOCTYPE HTML>")
print("<html>")
print("<head>")
print("<title>Pet details</title>")
print("</head>")
print("<body>")
print("<h1>{0}</h1>".format(pet_name))
print("<p>{}</p>".format(html))
print("<a href=\"login.html\">Log out</a>")
print("</body>")
print("</html>")
