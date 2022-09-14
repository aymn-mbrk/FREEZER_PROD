#!/usr/bin/python3
import cgi, cgitb
import mariadb
import sys


print ("Content-Type: text/html")
print ("")

print("""<!DOCTYPE html>
<html>
<html>
<meta charset="utf-8">
 <body>""")

cgitb.enable()

input_data = cgi.FieldStorage()



try:
    username = str(input_data["username"].value)
    #password = str(input_data["password"].value)
    print('<output> Bienvenue : {0}</output><br>'.format(username,))
except:
    print('<output>Erreur</output>')




# Connect to MariaDB Platform        
try:
    conn = mariadb.connect(
    user="root",
    password="root",
    host="192.168.0.2",
    database="Music2"
    )
    print("\nConnexion a la base établie \n")
except:
    print(f"Error connecting to MariaDB Platform:")
    sys.exit(1)  
print("""    
<form action="choice.cgi" method="POST">
     <legend> make your choice !  </legend>
     <label>Music: <input type="text" name="music"></label><br/>
    </fieldset>
    <button>Sumbit</button>
   </form>""")


# Get Cursor
try:
    cur = conn.cursor()
 #   print("good")
except:
    print("not ok")

cur.execute("SELECT * FROM playlist;")
for line in cur:
    print(line)
    print("""<br>""")


print(""" <form action="index.cgi" method="POST">
   <button>Retour</button>
  </form>""")

print("""</body></html>""")
