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
