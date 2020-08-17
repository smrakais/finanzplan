from class_lieferrand import lieferrand
import numpy as np
import os.path
from os import path

# exception and user input
while True:
    try:
        name = str(input ('Name des Lieferranden: '))
        artikel = str(input ('Artikel: '))
        preis= float(input ('Preis:  '))
        break
    except ValueError:
        print('Der Preis muss eine Zahl sein ! ')

#create obj
neuerLieferrand = lieferrand(name,artikel,preis)

# to numpy 1x1 matrix #TODO er speichert den preis auch als string
#new_array = np.array([neuerLieferrand.get_all()])
#print(new_array) 

# als liste gespeichert 
data = neuerLieferrand.get_all()
print(data) 



#*********************************************
#check if lieferrand.txt exists
#path = bool(path.exists('lieferrand.txt'))
#TODO die strings und die zahl müssen in eine datei gespeichert werden!





if not bool(path.exists('lieferrand.txt')):
    filename = 'lieferrand.txt'
    myfile = open(filename, 'a')
    myfile.write('Written with Python\n')
    myfile.close()

    print('lieferrand.txt hat noch nicht existiert und wurde jetzt erzeugt.')
elif bool(path.exists('lieferrand.txt')):
    tfile=open('lieferrand.txt','a')
    np.savetxt(tfile,data)
    tfile.close()
    print('lieferrand.txt existiert. Neue Kosten wurden hinzugefügt.')
else:
    print('Fehler bei dem einlesen des Pfades. Raphael anrufen!')
#**********************************************