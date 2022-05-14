import cgitb
cgitb.enable(display=1, logdir=None, context=5, format='html')

form = cgi.FieldStorage()

username = form.getvalue("username")

print(f"<h1>{username}</h1>")
