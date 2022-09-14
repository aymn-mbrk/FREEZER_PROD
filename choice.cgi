#!/usr/bin/python3
import cgi, cgitb
import mariadb
import sys
import platform
import subprocess
import os


print ("Content-Type: text/html")
print ("")

print("""<!DOCTYPE html>
<html>
<meta charset="utf-8">
 <body>""")


cgitb.enable()
input_data = cgi.FieldStorage()
print('<h1>Machine a  ajouter</h1>')
try:
    music = str(input_data["music"].value)
    print('<output> Vous avez choisi : {0}</output><br>'.format(music,))
except:
    print('<output>Erreur</output>')



# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="root",
        host="149.50.0.4",
        database="Music2"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
try:
    cur = conn.cursor()
except:
    print("not ok")

try:
    cur.execute("SELECT * FROM playlist WHERE User=waleed")
except:
    print("execute pas ok")

conn.commit()

cur.execute("SELECT * FROM connexion;")
for line in cur:
    print(line)
    print("""<br>""")

os.system("bash mainscript.sh aymn "+music+"")

print("""<figure>
    <figcaption>Listen to the :</figcaption>
    <audio
        controls
        src="/home/aymn/Music/'PNL - Mexico.mp3'">
            Your browser does not support the
            <code>audio</code> element.
    </audio>
</figure>""")



print(""" <form action="afficher.cgi" method="POST">
   <button>Retour</button>
  </form>""")

print("""</body></html>""")
