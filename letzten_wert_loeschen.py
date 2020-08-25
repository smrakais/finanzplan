import numpy as np 
import os

try:
    liste = np.genfromtxt('kosten.txt')# actually lists in a list (like a matrix)
    print(liste)
    np.savetxt('kosten.txt',liste[0:-1],fmt='%3.2f')
    if  liste.shape == (3,):            # if only one entry is in txt file gets deleted completely
        os.remove('kosten.txt')
        os.remove('monat.txt')
    print('Letzer Eintrag wurde erfolgreich gelöscht.')
except OSError:
    print('Es kann kein Wert gelöscht werden, da keine Daten existiern.')
   
     