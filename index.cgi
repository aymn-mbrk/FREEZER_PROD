#!/usr/bin/python3

print ("Content-Type: text/html")
print ("")

print("""<!DOCTYPE html>
<html>
<meta charset="utf-8">
 <body>
   <form action="afficher.cgi" method="POST">
    <fieldset>
     <legend> Hello ! .. Voulez-vous afficher les machines ? </legend>
    </fieldset>
    <button>Afficher les machines</button>
   </form>

   <img src="https://media1.giphy.com/media/Lk023zZqHJ3Zz4rxtV/giphy.gif?cid=790b7611fb4392712e9883e649ee0435ce4377214c338d6d&rid=giphy.gif&ct=g" alt="W3Schools.com" style="width:500px;height:544.218px;">

 </body>
</html>""")

