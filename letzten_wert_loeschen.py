import numpy as np 
import os
import sys

try:
    liste_kosten = np.genfromtxt('build/kosten.txt')# actually lists in a list (like a matrix)
    liste_monat = np.genfromtxt('build/monat.txt')
    liste_date = np.genfromtxt('build/date.txt', dtype = str)

    if  liste_kosten.shape == (3,):            # only if one entry is in txt.
        os.remove('build/kosten.txt')
        os.remove('build/monat.txt')
        os.remove('build/date.txt')
        print('Letzer Eintrag wurde erfolgreich gelöscht.')
        
    else:
        np.savetxt('build/kosten.txt',liste_kosten[0:-1],fmt='%3.2f')
        np.savetxt('build/monat.txt',liste_monat[0:-1],fmt='%3.2f')
        np.savetxt('build/date.txt',liste_date[0:-1],fmt = '%10s')
        print('Letzer Eintrag wurde erfolgreich gelöscht.')

    
except OSError:
    print('Es kann kein Wert gelöscht werden, da keine Daten existiern.')