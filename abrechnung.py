import numpy as np 


porto, buero, stuff = np.genfromtxt('kosten.txt', unpack = True)

#array porto buero stuff
ergebnis = np.array([round(np.sum(porto), 2),round(np.sum(buero),2),round(np.sum(stuff),2)])
print('Array der variablen Kosten: ' + str(ergebnis))
#fixkosten
miete  = 100
strom   = 11
telefon = 15
steuerberater = 20
kontofuehrungsgebuehren = 4.95

#array fixkosten
fixkosten = np.array([miete,strom,telefon,steuerberater,kontofuehrungsgebuehren])
fix_sum= round(np.sum(fixkosten), 2)
print('Die Fixkosten sind '+ str(fix_sum))

#gesamtkosten
gesamtkosten = round(np.sum(ergebnis,axis=0) + fix_sum,2)

#Ausgabe der Kosten
print('Die Kosten betragen für das Porto: ' + str(ergebnis[0]) )
print('für Büroartikel ' + str(ergebnis[1])) 
print('und für sonstige  Ausgaben ' + str(ergebnis[2]))

print('Die monatlichen Gesamtkosten belaufen sich auf '+ str(gesamtkosten))
