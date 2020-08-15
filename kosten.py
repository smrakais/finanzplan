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

#***counter monat*** 
Monat = datetime.now().strftime('%M')
print(Monat)
#counter =

# exception and user input
while True:
    try:
        porto = float(input ('Portokosten : '))
        buero = float(input ('Büroartikelkosten : '))
        stuff = float(input ('Sonstige Kosten:  '))
        break
    except ValueError:
        print('Bitte nur Zahlen eigeben! ')


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


#create obj
neueKosten = kosten(porto,buero,stuff)

# to numpy 1x1 matrix
new_array = np.array([neueKosten.get_all()])

#*********************************************
#check if kosten.txt exists
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