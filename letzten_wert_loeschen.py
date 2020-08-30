import numpy as np 
import os

try:
    liste_kosten = np.genfromtxt('build/kosten.txt')# actually lists in a list (like a matrix)
    liste_monat = np.genfromtxt('build/monat.txt')

    tdate = open('build/date.txt')#default is read,'r'
    liste_date  = [str(tdate.read())]
    print(liste_date)
    
    np.savetxt('build/kosten.txt',liste_kosten[0:-1],fmt='%3.2f')
    np.savetxt('build/monat.txt',liste_monat[0:-1],fmt='%3.2f')

    #np.savetxt('build/date.txt',tdate[0:-1])
    #read in eine liste packen --> bearbeiten und wieder in eine txt wandeln

    if  liste_kosten.shape == (3,):            # only if one entry is in txt. file gets deleted completely
        os.remove('build/kosten.txt')
        os.remove('build/monat.txt')
        os.remove('build/date.txt')
    print('Letzer Eintrag wurde erfolgreich gelöscht.')
except OSError:
    print('Es kann kein Wert gelöscht werden, da keine Daten existiern.')
   
     