#!/usr/bin/python3

print ("Content-Type: text/html")
print ("")

print("""<!DOCTYPE html>
<html>
<meta charset="utf-8">

<body>
   <form action="afficher.cgi" method="POST">
     <legend> Se connecter a la base de donnes !  </legend>
     <label>Username: <input type="text" name="username"></label><br/>
     <label>Password: <input type="text" name="password"></label><br/>
    </fieldset>
    <button>Sign in</button>
   </form>


 </body>
</html>""")

