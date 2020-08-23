#creates a latex tab with monthly expenses

from abrechnung import porto, buero, stuff, fix_sum, gesamtkosten 
#imports the variable porto, buero , etc. NOTE!--> this runs the .py file! 
#which makes sense because I want to have the value of a variable

import numpy as np
import os              
from datetime import date

from texutils.table import TexTable


# for tab entry
gesamtkosten_ohne_fixkosten = round(gesamtkosten - fix_sum,2)


#create a list for the table input
liste  = [fix_sum]
liste2 = [gesamtkosten_ohne_fixkosten]
liste3 = [gesamtkosten]


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
tab1.writeFile('tab_monatsabrechnung_drucken_part_1.tex')


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
tab2.writeFile('tab_monatsabrechnung_drucken_part_2.tex')


#executes the given command in the terminal
os.system('make')