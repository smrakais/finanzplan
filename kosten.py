from class_kosten import kosten
from datetime import date
from datetime import datetime
from time import sleep
import numpy as np
import os.path
from os import path

#***************************************
# das programm aufrüfen wenn
# ein neuen eintrag anlegen möchtest 
# also neue kosten eintragen willst
#***************************************


# TODO exception
porto = 1.0#float(input ('Portokosten : '))
buero = 23.42#float(input ('Büroartikelkosten : '))
stuff = 333.45#float(input ('Sonstige Kosten:  '))

neueKosten = kosten(porto,buero,stuff)
sleep(1)
neueKosten2 = kosten (4,5,6)

##funzt summe aus zwei eingelesenen objekten
##********************************
#data = neueKosten.get_all()
#data2 = neueKosten2.get_all()
#
#liste = np.array = ([])
#liste.append(data)
#summe_total= np.sum(liste, axis=0)
#print(summe_total)
##********************************

#einlesen per eingabe
#...

#erstellen
neueKosten = kosten(porto,buero,stuff)
value = neueKosten.get_all()
print('normale liste ' + str(value))

# in numpy 1x1 matrix
new_array = np.array([value])
print ('numpy 1x1 matrix '+ str(new_array))


#*********************************************
#check ob kosten.txt existiert
path = bool(path.exists('kosten.txt'))

if not path:
    np.savetxt('kosten.txt',new_array,fmt='%3.2f')
    print('Was False')
elif path:
    tfile=open('kosten.txt','a')
    np.savetxt(tfile,new_array,fmt='%3.2f')
    tfile.close()
    print('Was True')
else:
    print('fehler bei dem einlesen des pfades')
#**********************************************