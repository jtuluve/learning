import cgitb
cgitb.enable()

form = cgi.FieldStorage()

username = form.getvalue("username")

print(f"{username}")
