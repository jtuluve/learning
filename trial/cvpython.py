import cgitb
cgitb.enable()

form = cgi.FieldStorage()

username = form.getvalue("username")

print(f"<h1>{username}</h1>")
