fo.write("Content-type:text/html\r\n\r\n")
fo.write("<html>")
fo.write("<head>")
fo.write("<title>Hello - Second CGI Program</title>")
fo.write("</head>")
fo.write("<body>")
fo.write("<h2>Your name is {}. {} {}</h2>".format("last_name", "first_name", "last_name"))

fo.write("</body>")
fo.write("</html>")

fo.close()
