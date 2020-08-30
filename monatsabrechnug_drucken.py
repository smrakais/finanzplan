#creates a latex tab with monthly expenses

import sys #wird zum abrechen des programs gebraucht fall beim importieren von porto etc. ein exception geworfen wird

try:
        from abrechnung import porto, buero, stuff, fix_sum, gesamtkosten 
        #imports the variable porto, buero , etc. NOTE!--> this runs the .py file! 
        #which makes sense because I want to have the value of a variable
except ImportError:
        print('Für den Monat kann keine Abrechnung erstellt werden, da keine Daten vorliegen. ')
        sys.exit(1) #program is canceled

import numpy as np
import os    
#import os.path
#from os import path          
from datetime import date

from texutils.table import TexTable

# for tab entry
gesamtkosten_ohne_fixkosten = round(gesamtkosten - fix_sum,2)


#create a list for the table input
liste  = [fix_sum]
liste2 = [gesamtkosten_ohne_fixkosten]
liste3 = [gesamtkosten]

#check
print(np.shape(porto))
print(porto)
print(liste3)

#date:
#datelist =   

try:
        #Tab 1
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
        os.system('touch protokoll.tex') #lel ich hab nicht ganz verstanden warum das damit jetzt geht XD
        os.system('make')
except TypeError:

        #because it does not make it a list if it is only one value
        porto = [porto]
        buero = [buero]
        stuff = [stuff]

        #Tab 1
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
        os.system('touch protokoll.tex') #lel ich hab nicht ganz verstanden warum das damit jetzt geht XD
        os.system('make')