import cgi, os

data = cgi.FieldStorage()

# Get the uploaded file data
upload = data["imagefile"] 

# Find the name of the file without its entire path
filename = os.path.basename(upload.filename)

# Creates a writeable binary file in the same directory
# as where the script is.
with open(filename, "wb") as copy:
	# Read all the contents from the uploaded file
	# and write it to the newly created file.
	copy.write(upload.file.read())

print("Content-Type: text/html")
print()
print("<!DOCTYPE HTML>")
print("<html>")
print("<head>")
print("<title>Student details</title>")
print("</head>")
print("<body>")
print("<h1>{}</h1>".format(filename))
print("<img src=\"{}\"/><br/><br/>".format(filename))
print("<a href=\"imageupload.html\">Back</a>")
print("</body>")
print("</html>")