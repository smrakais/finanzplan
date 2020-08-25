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
datum = date.today()
monat = datum.month
#brauche ich später als numpy array 
monat_array = np.array([monat])
#print(monat_array)

# exception and user input
while True:     #TODO check if number has more than two digits after komma
    try:
        porto = float(input ('Portokosten : '))
        buero = float(input ('Büroartikelkosten : '))
        stuff = float(input ('Sonstige Kosten:  '))
        break
    except ValueError:
        print('Bitte nur Zahlen eingeben! ')


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
#path = bool(path.exists('kosten.txt'))

if not bool(path.exists('kosten.txt')):
    np.savetxt('kosten.txt', new_array,fmt='%3.2f')
    print('kosten.txt hat noch nicht existiert und wurde jetzt erzeugt.')
elif bool(path.exists('kosten.txt')):
    tfile=open('kosten.txt','a')
    np.savetxt(tfile,new_array,fmt='%3.2f')
    tfile.close()
    print('kosten.txt existiert. Neue Kosten wurden hinzugefügt.')
else:
    print('Fehler bei dem einlesen des Pfades. Raphael anrufen!')
#**********************************************

#*******************************************
#******TEST*****

print('angekommen')
if not bool(path.exists('monat.txt')):
    np.savetxt('monat.txt',monat_array,fmt='%d')
    print('monat.txt hat noch nicht existiert und wurde jetzt erzeugt.')
    print('Neuer Monat wurde erstellt.')
elif bool(path.exists('monat.txt')):
    print('Pfad existiert.')
    #monat in txt auslesen
    value = np.genfromtxt('monat.txt',unpack=True)
    #print('hinter value')
    #print(value)
    #letzten eintrag der liste nehmen
    try:
        if monat == value[-1]:
            tfile=open('monat.txt','a')
            np.savetxt(tfile,monat_array,fmt='%d')
            tfile.close()
            print('normaler durchgang')
            print('Wir sind noch im gleichen Monat.')
        elif monat != value[-1]:
        
            print('Wir sind nicht mehr im gleichen Monat. Neuer Monat wird erstellt.')

            #**************************************************************************
            # speichern der kosten mit monat
            kosten = np.genfromtxt('kosten.txt')
            #letzten wert nicht reinladen da der für den nächten monat ist
            np.savetxt('build/kosten_%i.txt' %monat, kosten[0:-1],fmt='%3.2f')
            #***************************************************************************

            #***************************************************************************
            #kosten.txt überschreiben
            tfile=open('kosten.txt','w')
            np.savetxt('kosten.txt',new_array,fmt='%3.2f')
            tfile.close()
            #***************************************************************************

            np.savetxt('monat.txt',monat_array,fmt='%d')
        else:
            print('Fehler im Abschnitt:  monat =! value[-1]')
    except IndexError:          
        #wtf war das kompliziert. muss hier rein falls monat.txt nur aus einer zahl besteht. sonst ist value[-1] nicht ausführbar
        if monat == value:      
            tfile=open('monat.txt','a')
            np.savetxt(tfile,monat_array,fmt='%d')
            tfile.close()
            print('exception aufgetreten')
            print('Wir sind noch im gleichen Monat.')

        elif monat != value:
        
            print('Wir sind nicht mehr im gleichen Monat. Neuer Monat wird erstellt.')

            #**************************************************************************
            # speichern der kosten mit monat
            kosten = np.genfromtxt('kosten.txt')
            #letzten wert nicht reinladen da der für den nächten monat ist
            np.savetxt('build/kosten_%i.txt' %monat, kosten[0:-1],fmt='%3.2f')
            #***************************************************************************

            #***************************************************************************
            #kosten.txt überschreiben
            tfile=open('kosten.txt','w')
            np.savetxt('kosten.txt',new_array,fmt='%3.2f')
            tfile.close()
            #***************************************************************************

            np.savetxt('monat.txt',monat_array,fmt='%d')
        else:
            print('Fehler im Abschnitt:  monat =! value[-1]')
    print('done!')
else:
    print('fehler bei dem einlesen des pfades')