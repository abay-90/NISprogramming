import cgi

data = cgi.FieldStorage()
username = data.getvalue("username")
password = data.getvalue("password")

html = ""
back_link_text = ""

if username == "JohnD" and password == "123456":
    back_link_text = "Log out"

    html += "<h1>User details</h1>"
    html += "John Doe<br/>johnd@somewhere.com<br/>123 456 7890<br/><br/>"
    html += "<h2>Pets</h2>"
    html += "<a href=\"petdetails.py?pet_id=1\">Fluffy</a><br/>"
    html += "<a href=\"petdetails.py?pet_id=2\">Spot</a><br/>"
    html += "<a href=\"petdetails.py?pet_id=3\">Snuffles</a><br/><br/>"
else:
    back_link_text = "Back"

    html += "<h1>Incorrect details entered</h1>"

print("Content-Type: text/html")
print()
print("<!DOCTYPE HTML>")
print("<html>")
print("<head>")
print("<title>Student details</title>")
print("</head>")
print("<body>")
print(html)
print("<a href=\"login.html\">" + back_link_text + "</a>")
print("</body>")
print("</html>")
