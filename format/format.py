"""
"formátum sztring" % változó_kifejezés_állandó
formátum sztring mindig % karakterrel kezdődik
formátum sztring mindig formátum karakterrel végződik
formátum karakterek:
* d decimális egész
* f float (lebegőpontos szám)
* s string  (karaktersorozat esetén)
* c character

kettő között
  jelzők szélesség .pontosság
  0 vezető nulla
  + előjeles kiíratás
  - balra igazítás
"""

szam=35.123
print("%f" % szam)
print("%20f" % szam)

szam2=3425.1234
print("%20f" % szam2)
print("|%20f|" % szam2)
print("|%20.2f|" % szam2)
print("|%020.2f|" % szam2)
print("|%+20.2f|" % szam2)
print("|%-20.2f|" % szam2)

nev="Frantal Attila"
print("%s" % nev)
print("|%20s|" % nev)

ar=340480.005
print("Ár: %.2f Ft" % ar)

betu="a"
print("%c" % betu)

"""
Modulok használata
  Importálni kell a modulokat:  import

Matematikai modul:   import math
"""
import math
val = math.sqrt(18)
print(val)
