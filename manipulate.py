import numpy as np 
from class_kosten import kosten
import os
import os.path 
from os import path
import sys
from abrechnung import fix_sum
from texutils.table import TexTable


#TODO nachträglich kosten hinzufügen von vergangenem monat 

#TODO idee: fixkosten reinladen (wehe wenn die sich ändern MAMA!)  und dann ergebnis ausrechenen vgl abrechnunng.pxy line 7
def re_run():
    ergebnis = np.array([round(np.sum(porto), 2),round(np.sum(buero),2),round(np.sum(stuff),2)])
    return ergebnis

# eingabe des monats 
while True:
    try:
        monat = int(input('Bitte die Zahl des Monats eingeben, der verändert werden soll! '))  
        break
    except ValueError:
        print('Eingabe fehlerhaft bitte wiederholen! Der Monat muss als Zahl eingegeben werden! ')


# check ob es den monat gibt
try:
    kosten_old = np.genfromtxt('build/kosten_%i.txt' %monat)
except OSError:
    print('Für diesen Monat liegen keine manipulierbaren Daten vor. ')
    sys.exit(1)


# kosten eintragen
while True:     #TODO check if number has more than two digits after komma
    try:
        porto = float(input ('Portokosten : '))
        buero = float(input ('Büroartikelkosten : '))
        stuff = float(input ('Sonstige Kosten:  '))
        break
    except ValueError:
        print('Bitte nur Zahlen eingeben! ')


#create obj
neueKosten = kosten(porto,buero,stuff)
# to numpy 1x1 matrix
new_array = np.array([neueKosten.get_all()])

tfile = open('build/kosten_%i.txt' %monat,'a')
np.savetxt(tfile,new_array,fmt='%3.2f')
tfile.close()
print('Daten wurden erfolgreich manipuliert.')


#gesamtkosten neu
gesamtkosten = round(np.sum(re_run(),axis=0) + fix_sum,2)
#**************************************************************** BIS HIER ALLES OKE    

#TODO also  ich muss mir sowieso noch überlegne wie ich die abrechnugen speicher
#evtl über ein extra skript move_pdf.py? der die pdf's nach jedem Monat verschiebt


#create a list for the table input
liste  = [fix_sum]
liste2 = [gesamtkosten_ohne_fixkosten]
liste3 = [gesamtkosten]


#Tab 1 NEU
        tab1 = TexTable([porto, buero ,stuff],
                                [r'Portokosten / \euro',
                                 r'Büroartikel / \euro',
                                 r'Sonstige Ausgaben / \euro'],
                                label='monatsabrechnung_1',
                                caption='Tabelle der variablen Kosten.'#TODO mit date 
                        )

        tab1.setRowRounding(0,2)
        tab1.setRowRounding(1,2)
        tab1.setRowRounding(2,2)
        tab1.writeFile('build/tab_monatsabrechnung_drucken_part_1.tex')


        #Tab 2
        tab2 = TexTable([liste, liste2 ,liste3],
                                [r'Fixkosten / \euro',
                                 r'Gesamtkosten (o.F.) / \euro',
                                 r'Gesamtkosten / \euro'],
                                label='monatsabrechnung_2',
                                caption='Tabelle der Fix- und Gesamtkosten.'
                        )

        tab2.setRowRounding(0,2)
        tab2.setRowRounding(1,2)
        tab2.setRowRounding(2,2)
        tab2.writeFile('build/tab_monatsabrechnung_drucken_part_2.tex')


        #executes the given command in the terminal
        #os.system('touch protokoll.tex') #lel ich hab nicht ganz verstanden warum das damit jetzt geht XD
        #os.system('make')

#TODO jetzt muss noch ein neues pdf erzeugt werden
#TODO datum in kosten .txt und kosten_i.txt speichern