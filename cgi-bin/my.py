#!/usr/bin/python

# Импорт модулей для обработки CGI 
import cgi, cgitb 

# Создание экземпляра FieldStorage
form = cgi.FieldStorage() 


print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Поиграем в погромистов</title>")
print ("</head>")
print ("<body>")
print ("""
<form action = "/cgi-bin/lab2.py" method = "post" target = "_blank">
<textarea name = "textcontent" cols = "40" rows = "4">
Даша хочет кушать...
</textarea>
<input type = "submit" value = "Анализируй, машина!" />
</form>
  """)
print ("</body>")
print ("</html>")


