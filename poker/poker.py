"""
Modulok használata
  Importálni kell a modulokat:  import

Random modul:   import random
"""

#kockapóker 5 dobással
import random
szam1=random.randrange(6)+1
szam2=random.randrange(6)+1
szam3=random.randrange(6)+1
szam4=random.randrange(6)+1
szam5=random.randrange(6)+1
print("%10s" % "Ember: " "%d" % szam1, "%d" % szam2,"%d" % szam3,"%d" % szam4,"%d" % szam5)

sz1=random.randrange(6)+1
sz2=random.randrange(6)+1
sz3=random.randrange(6)+1
sz4=random.randrange(6)+1
sz5=random.randrange(6)+1
print("%10s" % "Gép: " "%d" % sz1, "%d" % sz2,"%d" % sz3,"%d" % sz4,"%d" % sz5)
