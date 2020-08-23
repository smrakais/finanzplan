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



#************************************************************************
#funzt
#executes the given command in the terminal
#import os              
#os.system("python kosten.py")
#************************************************************************



#************************************************************************
#**************EINE TABELLE**********************************************
#************************************************************************

#from texutils.table import TexTable
#from texutils.table import Combined
#
#tab1 = TexTable([T8,T7,dt],
#                        [r'$T_\text{nah}$ / $\si{\celsius}$',#FUCKING KLEINES si!!!!!!! VERFICKTE SCHEISSE
#                        r'$T_\text{fern}$ / $\si{\celsius}$',
#                        r'$\Delta t$ / $\si{\second}$'],
#                        label='amplituden',
#                        caption='Amplitudenwerte der Temperatur und der Zeit des Edelstahls'
#                )
#
#tab1.setRowRounding(0,0)
#tab1.setRowRounding(1,0)
#tab1.setRowRounding(2,0)
#
#tab1.writeFile('build/tab_T8_T7.tex')   #amplitudenwerte und zeit




#************************************************************************
#*****************ZWEI TABELLEN KOMBINIERT*******************************
#************************************************************************

#tabelle hysterese ohne neukurve
#t1 = TexTable([i,b], [r'$I$ / $\si{\ampere}$',
#                      r'$B$ / $\si{\milli\tesla}$'], label='tab:hysterese',
#             caption='Messdaten zum erstellen der Hysteresekurve ohne Neukurve')
#t1.setRowRounding(1, 0)
#t1.setRowRounding(0, 0)
#
# #eig. würde hier jetzte noch ein  t.writeFile('build/tabHysterese.tex') stehen und unten auch aber so würde er ja 2 einzelne listen machen aber wir nehmen combined und er verinigt 2 in eine
#
##tabelle hysterese neukurve
#t2 = TexTable([i2,b2], [r'$I$ / $\si{\ampere}$',
#                      r'$B$ / $\si{\milli\tesla}$'], label='tab:hysterese2',
#             caption='Messdaten zum erstellen der Neukurve')
#t2.setRowRounding(1, 0)
#t1.setRowRounding(0, 0)
#
#
#
## zwei listen in einem
#Combined([t1, t2], caption='Messdaten').writeFile('build/tabHystereseAll.tex')