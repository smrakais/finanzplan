from datetime import date
from datetime import datetime

import numpy as np

#*********************************************
datum = date.today()
#print(datum)
#
#tag = datum.day
#print(tag)
#
#monat = datum.month
#print(monat)
#
#jahr = datum.year
#print(jahr)
#*********************************************


##*********************************************
#funzt
#stringZeit = datetime.now().strftime('%H:%M:%S')
#sekunde = datetime.now().strftime('%S')
#print(stringZeit)
#print(sekunde)
##*********************************************

#--> jetzt  die strings vergleichen

##**************************************************************
#funzt
#while True:
#    try:
#        x = float(input("Bitte Zahlen eingeben: "))
#        print('Danke')
#        break
#    except ValueError:
#        print("Ich sagte du sollst eine Zahl eingeben... , nochmal! ")
##**************************************************************

##**********************************************************
##aber nicht zu gebrauchen, da keine schleife
#a = input('zahle eingeben ')
#if a.isnumeric():
#    print('zahl')
#elif not a.isnumeric():
#    print('keine zahl') 
##**********************************************************

#datum = date.today()
#monat = datum.month
#
#path_monat = bool(path.exists('monat.txt'))
#
#if not path_monat:
#    np.savetxt('monat.txt',monat,fmt='%3.2f')
#    print('Pfad hat noch nicht existiert und wurde jetzt erzeugt.')
#elif path:
#    print('Pfad existiert.')
#    #monat in txt auslesen
#    value = np.genfromtxt('monat.txt',unpack = True)
#    #letzten eintrag der liste enehmen
#    if monat == value[-1]:
#        tfile=open('monat.txt','a')
#        np.savetxt(tfile,monat,fmt='%3.2f')
#        tfile.close()
#        print('Wir sind noch im gleichen Monat.')
#    elif monat =! value[-1]:
#        
#        print('Wir sind nicht mehr im gleichen Monat. Neuer Monat wird erstellt.')
#                
#        #**************************************************************************
#        # speichern der kosten mit datum
#        kosten = np.genfromtxt('kosten.txt',unpack=True)
#        #letzten wert nicht reinladen da der für den nächten monat ist
#        np.savetxt('build/kosten_%i.txt' %datum, kosten[0:len(kosten)],fmt='%3.2f')
#        #***************************************************************************
#    
#        #***************************************************************************
#        #kosten.txt überschreiben
#        tfile=open('kosten.txt','w')
#        np.savetxt(kosten.txt,new_array,fmt='%3.2f')
#        tfile.close()
#        #***************************************************************************
#
#        np.savetxt('monat.txt',monat,fmt='%3.2f')
#    else:
#        print('Fehler im Abschnitt:  monat =! value[-1]')
#
#else:
#    print('fehler bei dem einlesen des pfades')

i=np.genfromtxt('kosten.txt', unpack=True)
print(i)