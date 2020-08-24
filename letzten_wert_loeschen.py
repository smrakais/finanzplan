import numpy as np 

#TODO
'''
    muss noch überarbeitet werden
    funktioniert bis jetzt nur wenn 
    in kosten.txt mehr als ein eintrag ist 
    und kosten.txt bereits existiert 

    fehler bei nur einem eintrag da er nicht
    dann eine zeile der matrix löscht 
    sondern dann die eine zeile als liste mit 3 einträgen
    identifiziert.

    Evtl fix mit readlines??

    am einfachsten zeile irgwie als 1x1 matrix auffassen
    und durch löschen dann leere matrix erzeugen
    oder file komplett löschen
'''
try:
    liste = np.genfromtxt('kosten.txt')
    print(liste)
    np.savetxt('kosten.txt',liste[0:-1],fmt='%3.2f')
    print('Letzer Eintrag wurde erfolgreich gelöscht.')
except OSError:
    print('Es kann kein Wert gelöscht werden, da keine Daten existiern.')
   
     